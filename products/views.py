from django.shortcuts import render
from django.http import JsonResponse


from django.shortcuts import render, redirect
from .models import Product
from django.utils.timezone import now

def product_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        if name and price:
            Product.objects.create(name=name, price=price, timestamp=now())
            return redirect('product_view')

    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def truncate_product_data(request):
    # Allow both GET and POST requests
    if request.method in ["GET", "POST"]:
        try:
            Product.objects.all().delete()  # Deletes all Product records
            return JsonResponse({"message": "All Product data truncated successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only GET and POST requests allowed"}, status=400)
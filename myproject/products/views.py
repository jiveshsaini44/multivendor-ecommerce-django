from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from vendors.models import Vendor
from .decorators import vendor_required
from django.contrib.auth.decorators import login_required
from .forms import ProductForm



@login_required
def vendor_dashboard(request):
    if request.user.role != 'vendor':
        return redirect('login_')
    
    vendor = request.user.vendor_profile
    products = vendor.products.all()
    total_products = products.count()
    total_stock = sum([p.stock for p in products])
    if not Vendor.store_name:
        return redirect('complete_vendor_profile')


    return render(request, 'vendor_dashboard.html', {
        'products': products,
        'total_products': total_products,
        'total_stock': total_stock,
    })
    
    
@login_required
@vendor_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor_profile 
            product.save()

            return redirect('vendor_dashboard')
        else:
            print(form.errors)  # Debugging line to print form errors
    else:
        form = ProductForm()

    return render(request, 'add_products.html', {'form': form})

def complete_vendor_profile(request):
    vendor = request.user.vendor_profile

    if request.method == "POST":
        vendor.store_name = request.POST.get('store_name')
        vendor.store_description = request.POST.get('store_description')
        vendor.save()

        return redirect('vendor_dashboard')

    return render(request, 'complete_vendor_profile.html')

@vendor_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)


    if product.vendor != request.user.vendor_profile:
        return redirect('vendor_dashboard')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('vendor_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'add_products.html', {'form': form})

@vendor_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.vendor != request.user.vendor_profile:
        return redirect('vendor_dashboard')

    product.delete()
    return redirect('vendor_dashboard')

def vendor_not_approved(request):
    return render(request, 'vendor_not_approved.html')
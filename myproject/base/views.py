from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import *
from django.db.models import Q
from products.models import Product

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        cartProducts_count=CartModels.objects.filter(host=request.user).count()
    else:
        cartProducts_count=0

    no_match=False
    trend=False
    offer=False
    
    filter_type = request.GET.get('filter')
    
    if 'q' in request.GET:
            q = request.GET['q']
            products=Product.objects.filter(Q(name__icontains=q)|Q(description__icontains=q))
            if len(products)==0:
                no_match=True
    elif filter_type == 'trending':
        products = Product.objects.filter(trending=True)

    elif filter_type == 'offer':
        products = Product.objects.filter(offer=True)

    else:
        products = Product.objects.all()

    
    
    pcategory=[]
    a=Product.objects.all()
    for i in a:
        if i.category not in pcategory:
            pcategory+=[i.category]
        
    return render(request, 'home.html',{'products':products, 'no_match': no_match, 'category':pcategory,'cartProducts_count': cartProducts_count,'trend':trend,'offer':offer})
    

@login_required(login_url='login_')
def add_cart(request,id):
    product=Product.objects.get(id=id)
    try:
        cp=CartModels.objects.get(pname=product.name, host=request.user)
        cp.quantity+=1
        cp.totalprice=cp.quantity*cp.price
        cp.save()
        return redirect('home')
    except:
        CartModels.objects.create(
        pname=product.name, 
        pcategory=product.category,
        price=product.price,
        quantity=1,
        totalprice=product.price,
        host=request.user)
    
    
    return redirect('home')

def cart(request):
    cartProducts_count=CartModels.objects.filter(host=request.user)
    
    cartProducts=CartModels.objects.filter(host=request.user)
    total=0
    for i in cartProducts:
        total+=i.totalprice
        
    return render(request,'cart.html',{'cartProducts':cartProducts, 'total': total,'search_bar': True, 'cartProducts_count': cartProducts_count.count()})

def remove(request,id):
    cp=CartModels.objects.get(id=id)
    cp.delete()
    return redirect('cart')


def support(request):
    return render(request,'support.html',{'search_bar': True})


def knowus(request):
    return render(request,'knowus.html',{'search_bar': True})

def increment(request,id):
    cd=CartModels.objects.get(id=id)
    cd.quantity+=1
    cd.totalprice=cd.quantity*cd.price
    cd.save()
    return redirect('cart')

def decrement(request,id):
    cd=CartModels.objects.get(id=id)
    if cd.quantity>1:
        cd.quantity-=1
        cd.totalprice=cd.quantity*cd.price
        cd.save()
    else:
        cd.delete()
    return redirect('cart')




def product_details(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'product_details.html', {
        'product': product
    })
    
    
    
    
    
    
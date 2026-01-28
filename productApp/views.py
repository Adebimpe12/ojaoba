from django.shortcuts import render
from .models import Product, ProductFeatures
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductForm, ImageForm, FeatureForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# products =[
#     {   'name': 'Product 1',
#         'price': 100,
#         'description': 'Product 1 description',
#         'image':'https://tse4.mm.bing.net/th/id/OIF.jMp6cNMJwCbKDHwMN3Uqmw?rs=1&pid=ImgDetMain&o=7&rm=3'
#         },
#     {   'name': 'Product 2',
#         'price': 100,
#         'description': 'Product 2 description',
#         'image':'https://d2v5dzhdg4zhx3.cloudfront.net/web-assets/images/storypages/primary/ProductShowcasesampleimages/JPEG/Product+Showcase-1.jpg'
#         },
#     {   'name': 'Product 3',
#         'price': 100,
#         'description': 'Product 3 description',
#         'image':'https://tse2.mm.bing.net/th/id/OIP.WWJfnkziSFoYhdJ-3wDV9QHaLH?rs=1&pid=ImgDetMain&o=7&rm=3'
#         },
#     {
#             "name": "Product 4",
#             "price": 400,
#             "description": "Product 4 description",
#             "image": "https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?cs=srgb&dl=pexels-madebymath-90946.jpg&fm=jpg"
#         }
# ]
# def getHome(request):
#     username = 'Adebimpe'

    
#     return render(
#         request, 'index.html', 
#         context={'name':username, 'products':products}
#     )
    

def getHome(request):
    username = "Bolaji Ogunmola"
    
    products = ( Product.objects
                .all() 
                .prefetch_related(
                    "features",
                    "images",
                    "reviews"
                )
                .order_by("-created_at")
            )
    # Products = Product.objects.all()
    # products = Product.objects.filter(id=1)
    # products = Product.objects.filter(title='pRoDuct 2')
    # products = Product.objects.filter(title__iexact='pRoDuct 2')
    # products = Product.objects.filter(title__exact='pRoDuct 2')
    # products = Product.objects.filter(title__icontains='pRo')
    # products = Product.objects.filter(title__contains='pRo')
    # products = Product.objects.filter(quantity__gte=10)
    # product = Product.objects.get(id=1)
    # print(product.description)
    # print(products)
    # product.delete()
    
    return render(
        request,
        template_name="index.html",
        context={"name": username, "products": products[0:4]}
    )


def getProducts (request):
    products = ( Product.objects
                .all() 
                .prefetch_related(
                    "features",
                    "images",
                    "reviews"
                )
                .order_by("-created_at")
            )
    # print(products)
    # for prod in products:
    #     print(prod.images.all().first().image.url)
    return render(
        request,
        template_name='products.html',
        context={'products':products})

    
def getProductById(request, product_id): 
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, product_id=product_id)
    return render(
        request,
        template_name='single_product.html',
        context={'product':product}
    )
 
@login_required
def addProduct(request):
    # print(request.user.email)
    if request.method == 'POST':
        # print(request.POST.get('title'))
        # Product.objects.create(
        #     title = request.POST.get('title'),
        # )
        # form = ProductForm(request.POST,request.FILES )
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products')
    
    else:
        form = ProductForm()
        return render(
            request,
            template_name='product_form.html', 
            context={
                'form':form,
                'title':'Product Form'
            }
    )
        
def addImage(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            image = form.save(commit=False)
            image.product = product
            image.save()
        return redirect('get_product', product_id)
    else:
        form = ImageForm()
    return render(
        request,
        template_name='product_form.html',
        context={'form':form,
                 'title':'Upload Image'}
    )
    
@login_required   
def addFeature(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = FeatureForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.product = product
            feature.save()
            
        return redirect('get_product', product_id)
    else:
        form = FeatureForm()
    return render(
        request,
        template_name='product_form.html',
        context={'form':form,
                 'title':'Feature Form'
        }
    )


def editProduct(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = ProductForm( request.POST, instance=product)
        if form.is_valid():
            form.save()
            
        return redirect('get_product', product_id)
    else:
        form = ProductForm(instance=product)
    return render(
        request,
        template_name='product_form.html',
        context={'form':form,
                 'title':'Product Form'
        }
    )
    
    
@login_required
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("products")
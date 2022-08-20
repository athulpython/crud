from django.shortcuts import redirect, render
from . models import shop
from . forms import ShopForm

# Create your views here.


def demo(request):
    product = shop.objects.all()
    return render(request, "home.html", {'products': product})


def detail(request, book_id):
    product1 = shop.objects.get(id=book_id)
    return render(request, 'detail.html', {'product': product1})


def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        img = request.FILES['img']
        s = shop(name=name, description=description, img=img, price=price)
        s.save()
        print("product succsessfully added")
    return render(request, "add_product.html")


def update(request, id):
    obj = shop.objects.get(id=id)
    form = ShopForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'obj': obj})


def delete(request, id):
    if request.method == "POST":
        obj = shop.objects.get(id=id)
        obj.delete()
        return redirect(' /')
    return render(request, 'delete.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('catalog')
    page='login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('catalog')
        else:
            messages.error(request, 'Username or password is incorrect')

    context={'lr': page}
    return render(request, 'loginreg.html',context)

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('catalog')
    page='register'
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Customer.objects.create(user=request.user, FirstName=request.user.first_name, LastName=request.user.last_name)
            messages.success(request, "Registration successful." )
            return redirect("catalog")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context={'lr': page, "register_form":form}
    return render(request, 'loginreg.html',context)

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def account(request):
    customer = request.user.customer
    context={'customer':customer}
    return render(request, 'accnt.html',context)

@login_required(login_url='/login')
def catalog(request):
    item_list = item.objects.all()
    return render(request, 'catalog.html', {'item_list': item_list})

def home(request):
    context={}
    return render(request, 'home.html')

@login_required(login_url='/login')
def search(request):
    q = request.GET.get('q')
    items = item.objects.filter(itemName__icontains=q)
    context={"items":items, "qss":q}
    return render(request, 'search.html',context)

@login_required(login_url='/login')
def viewcart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,placed = Order.objects.get_or_create(customer = customer, placed = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total': 0}

    context ={'items': items, 'order': order}
    return render(request, 'cart.html', context)

def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='/login')
@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    # print(data.get('iID'))
    print(data)
    iID = data.get('iID')
    action = data.get('action')
    customer = request.user.customer
    it = item.objects.get(itemID=iID)
    order,placed = Order.objects.get_or_create(customer = customer, placed = False)

    orderItem,created= OrderItem.objects.get_or_create(order=order, product = it)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was Added", safe=False)

@login_required(login_url='/login')
def checkout(request):
    customer = request.user.customer
        
    try:
        order = Order.objects.get(customer = customer, placed = False)
        items = order.orderitem_set.all()
    except ObjectDoesNotExist:
        return redirect('/cart')
    

    if request.method == 'POST':
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        address = request.POST.get('address')
        ad2 = request.POST.get('address2')
        pin = request.POST.get('pincode')
        print(email, phno, pin, address, ad2, order.id, order.placed)

        orderAddress.objects.create(order=order, email=email, phno=phno, address=str(address + ' ' + ad2 + ', Tamilnadu' + ', India'), PIN=pin)

        order.placed=True
        # for item in items:
        #     item
        order.save()
        # print(order.id, order.placed)
        return redirect('/success')

    context={'order':order, 'orderItems': items}
    return render(request, 'address.html', context)

@login_required(login_url='/login')
def success(request):
    context = {}
    return render(request, 'success.html', context)
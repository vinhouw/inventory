from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from inventory import views
from .models import Item, Category
from django.contrib.auth.decorators import login_required
from .filters import ItemFilter
from inventory.forms import ItemForm, AddItemForm #ItemDetailsForm



# Create your views here.
def home(request):
    return render(request, 'inventory/home.html')
   
def signupuser(request):
    if request.method=='GET':
        return render(request, 'inventory/signupuser.html', {'form':UserCreationForm()})
    else:
        # Create a new user if it is a POST
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)  # login new user after saving it
                return redirect('home')  # prolly redirect to a new custom page 
            
            except IntegrityError:
                return render(request, 'inventory/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose another username.'} )
        else:
            # tell user the passwords are not matching
            return render(request, 'inventory/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})



def loginuser(request):
    if request.method == 'GET':
        return render(request, 'inventory/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'inventory/loginguser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def inventory(request):
    items = Item.objects.all().order_by('id')
    item_filters = ItemFilter(request.GET, queryset = items)
    items = item_filters.qs

    return render(request, 'inventory/view_inventory.html', {
        'items': items, 'item_filters': item_filters,
    })

@login_required 
def item_detail(request, item_id):
    item = Item.objects.get(id = item_id)

    # itemDetailsForm = ItemDetailsForm()
    return render(request, 'inventory/item_detail.html', {'item': item})


@login_required
def add_to_stock(request, pk):
    # issued_item = Item.objects.get(id = pk)
    form = AddItemForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # added_quantity = int(request.POST['received_quantity'])
            # issued_item.quantity += added_quantity
            # issued_item.save()

            # #To add to the remaining stock quantity is reducing
            # print(added_quantity)
            # print (issued_item.quantity)
            return redirect('home')

    return render (request, 'inventory/add_to_stock.html', {'form': form})



@login_required
def create_item(request):
    """ Create New Item for the Inventory """
    if request.method == 'GET':
        return render(request, 'inventory/create_item.html', {'form':ItemForm()})
    else:
        try:
            form = ItemForm(request.POST)
            newitem = form.save(commit=False)
            newitem.user = request.user 
            newitem.save()
            return redirect('inventory')
        except ValueError:
            return render(request, 'inventory/create_item.html', {'form':ItemForm(), 'error':'Bad Data Passed in, try again'})

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.template import loader
from .forms import Additemform, Contactsform, AdminForm


# Create your views here.
def firstview(request):
    item_list = Item.objects.all()
    #template = loader.get_template('food/index.html')
    contex ={
        'item':item_list

    }
    #return HttpResponse(template.render(contex,request))
    #or
    return render(request,'food/admin.html',contex)

def details(request,id):
    id = Item.objects.get(pk=id)
    return render(request,'food/details.html',{'id':id})

def ctreateItem(request):
    forms = Additemform()
    if request.method == 'POST':
        forms = Additemform(request.POST)
        if forms.is_valid():
            forms.save(commit=True)
            print('data saved')
            return redirect('foodapp:firstview')
        else:
            print(forms.errors)
    return render(request,'food/add-item-forms.html',{'forms':forms})


# def admin_view(request):
#     items = Item.objects.all()
#     return render(request, 'food/admin.html', {'items': items})


def update_item(request,id):
   
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        forms = Additemform(request.POST, instance=item)
        if forms.is_valid():
            forms.save(commit=True)
        return redirect('foodapp:firstview')
    return render(request,'food/updated_item.html',{'id':item})
def delete_item(request,id):
    items = Item.objects.get(id = id)
    
    if request.method == "POST":
        items.delete()
        return redirect('foodapp:firstview')
    return render(request,'food/delete.html',{'items':items})

def userdesc(request,id):
    id = Item.objects.get(pk=id)
    return render(request,'food/userdescription.html',{'id':id})

def home(request):
    return render(request,'food/home.html')


def userview(request):
    item = Item.objects.all()
    return render(request,'food/userview.html',{'items':item})


def contact(request):
    cont = Contactsform()
    if request.method == 'POST':
        cont = Contactsform(request.POST)
        if cont.is_valid():
            cont.save(commit=True) 
            print('data saved')
            return redirect('foodapp:contactsu')
        else:
            print(cont.errors)    
    return render(request,'food/contacts.html',{'cont':cont})



def about(request):
    
    return render(request,'food/aboutpage.html')

def contactview(request):
    data = Contact.objects.all()
    return render(request,'food/contactview.html',{'data':data})

def contactsu(request):
    return render(request,'food/contactsucc.html')
def items(request):
    return render(request,'food/testing.html')


#this not an standard way so we need to use an templates in html to render an templates
def items3(request):
    return HttpResponse('<h1>this an item views in an html</h1>')

def AdminLogIn(request):
    f = AdminForm()
    if request.method == "POST":
        f = AdminForm(request.POST)
        if f.is_valid():
            admin = f.cleaned_data['Admin']
            password = f.cleaned_data['Password']
            if admin != "Suhas":
                return render(request, 'food/adminLogIn.html', {'Form':f, 'AdminError':'Invalid Admin', 'PasswordError':None})
            elif password != "SuhasO@2002":
                return render(request, 'food/adminLogIn.html', {'Form':f, 'AdminError':None, 'PasswordError':'Incorrect Password'})
            else:
                return redirect('foodapp:firstview')
        return render(request, 'food/adminLogIn.html', {'Form':f, 'AdminError':None, 'PasswordError':None})
    return render(request, 'food/adminLogIn.html', {'Form':f, 'AdminError':None, 'PasswordError':None})
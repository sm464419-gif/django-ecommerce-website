from django.shortcuts import render,redirect
from app.models import Category,Product
from django.contrib.auth import authenticate,login
from app.models import UserCreateForm


# Create your views here.
def Base(request):
    return render(request,'base.html')


def Index(request):
    category= Category.objects.all()
    product= Product.objects.all()
    context={
        'category' : category,
        'product': product,
    }
    return render(request, 'index.html',context)

def signup(request):
    if request.method=='POST':
        form= UserCreateForm(request.POST)
        if form.is_valid():
            new_user= form.save()
            new_user= authenticate(
                username= form.cleaned_data['username'],
                password= form.cleaned_data['password1']
            )
            login(request,new_user)
            return redirect('index')

    else:
        form= UserCreateForm()

    context={
        'form': form,
    }

    return render(request,'registration/signup.html',context)
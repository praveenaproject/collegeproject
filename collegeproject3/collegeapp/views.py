from django.shortcuts import render
from  .models import Department,Branch,Applicationform
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout as deauth
from django.contrib.auth.models import User
# from .models import *





# Create your views here.


# Create your views here.


def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        print(username, password, cpassword)
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                print("else working")
                user = User.objects.create_user(username=username, password=password)
                print(user)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    deauth(request)
    messages.success(request , "You are Logout Successfully")
    return redirect('index')


def form(request):
    if not request.user.is_authenticated:
        return redirect('user-login')

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        #
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone= request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.get('materials')
        Branch_id = request.POST.get('Branch_id')
        Department_id = request.POST.get('department')

        user=request.user

        Department_id = Department.objects.get(id=Department_id)
        Branch_id = Branch.objects.get(id=Branch_id)

        Applicationform.objects.create(
            user=user,
            name=name,
            date=date,
            gender=gender,
            age=age,
            phone=phone,
            email=email,
            address=address,
            purpose=purpose,
            materials_provide=materials_provide,
            Branch_id=Branch_id,
            Department_id=Department_id
        )
        return redirect('message')

    department = Department.objects.all()
    context = {
        'department': department
    }
    return render(request, 'form.html',context)



def get_branches(request):

    get_department = request.GET.get('department')

    get_object = Department.objects.filter(id=get_department).first()


    all_branches = Branch.objects.filter(department=get_object)

    context = {

            'all_branches': all_branches
        }
    return render(request, 'partials/branches.html', context)

def newpage(request):
    return render(request,"newpage.html")

def message(request):
    return render(request, "message.html")

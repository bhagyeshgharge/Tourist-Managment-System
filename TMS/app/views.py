from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from app.models import Admin_Reg,Package,Book_Package
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from app.models import *
# Create your views here.

#User Index
def index(request):
    product_data=Package.objects.filter(is_active=True)
    context={'package':product_data}
    return render(request,'User-index.html',context)

#User Login
def UserLogin(request):
    if request.method=="GET":
        return render(request,'user_login.html')
    else:
        user_em=request.POST['Login_Username']
        user_ep=request.POST['Login_Password']
        a=authenticate(username=user_em,password=user_ep)
        if a is not None:
            login(request,a)
            return redirect('/')
        else:
            return redirect('/user_login')

#User Register
def register(request):
    if request.method=='GET':
        return render(request,'user_reg.html')
    else:
        Name=request.POST['Reg_Name']
        UserName=request.POST['Reg_UserName']
        Email=request.POST['Reg_Email']
        PassWord=request.POST['Reg_password']
        obj=User.objects.create(first_name=Name,username=UserName,email=Email)
        obj.set_password(PassWord)
        obj.save()
        return redirect('/user_login')
    
#User Logout
def User_logout(request):
    logout(request)
    return redirect('/')

#Admin Login
def admin_login(request):
    if request.method=="GET":
        return render(request,'admin_login.html')
    else:
        user_em=request.POST['Login_Username']
        user_ep=request.POST['Login_Password']
        a=authenticate(NameUser=user_em,Password=user_ep)
        if a is not None:
            login(request,a)
            return HttpResponse('Admin login successfully')
        else:
            return redirect('/admin_login')
        

#Admin Register
def admin_register(request):
    if request.method=='GET':
        return render(request,'user_reg.html')
    else:
        name=request.POST['Reg_Name']
        userName=request.POST['Reg_UserName']
        email=request.POST['Reg_Email']
        passWord=request.POST['Reg_password']
        obj=Admin_Reg.objects.create(Name=name,NameUser=userName,Email=email,Password=passWord)
        obj.save()
        return redirect('/login')
    
#Admin Index
def Admin_index(request):
    return render(request,'admin_index.html')



#admin add_package
def add_package(request):
    if request.method=='GET':
        return render(request,'add_package.html')
    else:
        place=request.POST['place']
        country=request.POST['country']
        state=request.POST['state']
        price=request.POST['Price']
        day=request.POST['day']
        night=request.POST['night']
        description=request.POST['description']
        image=request.POST['image']
        obj=Package.objects.create(Place=place,Country=country,State=state,Price=price,Days=day,Night=night,Description=description,Image=image)
        obj.save()
        return HttpResponse("Add Successfully")

#package details for user
def package(request,pid):
    obj=Package.objects.filter(id=pid)
    context={'package':obj}
    return render(request,'package.html',context)


#book pacakge for user
def book_package(request,tid):
        obj=Package.objects.filter(id=tid)
        context={'package':obj}  
        if request.method == 'POST':
            name = request.POST['first_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            place = obj.first().Place  # Assuming Place is a field in the Package model
            country = obj.first().Country  # Assuming Country is a field in the Package model
            price = obj.first().Price  # Assuming Price is a field in the Package model
            total_person = request.POST['total_person']
            total_price = request.POST['total_price']
            obj2 = Book_Package.objects.create(Name=name,Email=email,Phone_No=phone,Address=address,Place=place,Country=country,Price=price,Total_Person=total_person,Total_Price=total_price)
            obj2.save()
            return redirect('/')
        return render(request, 'book_package.html', context)

#chek my booking for user      
def my_booking(request):
    obj=Book_Package.objects.all()    
    context={'book_package':obj}
    return render(request,'my_booking.html',context)


        
#contact
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_message = request.POST['message'] 
        obj2 = Contact.objects.create(Name=name, Email=email, Phone_No=phone, Request=user_message)
        obj2.save()
        return redirect('/')
        

    
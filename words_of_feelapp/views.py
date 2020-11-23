from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from .models import Quotes
from .forms import RegistrationFrom
from .forms import QuotesFrom
from .forms import LoginFrom
from .forms import forgotpasswordform
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.mail import EmailMessage
import random
# Create your views here.
def user_info(request):

    reg = Registration.objects.all()
    print(reg)

    return render(request,"User_info.html",{"data":reg})

def Homepage(request):
    que = Quotes.objects.all()
    print(que)
    return render(request,"Homepage.html",{"data":que})


def registration(request):
    if request.method == "POST" :
        reg = RegistrationFrom(request.POST,request.FILES)
        if reg.is_valid():
            reg.save()
            return redirect('login')
    else:
        reg = RegistrationFrom()
        return render(request,"registration.html",{'registration':reg})

def mainpage(request):
    if "user" not in request.session:
        return redirect('login')
    else:
        que = Quotes.objects.all()
        print(que)
        return render(request,"mainpage.html",{"data":que})

def quotes(request):
    if "user" in request.session:
        if request.method == "POST":
            # q = Quotes.objects.get(id=id)use objects.get when you want to get data from back end side 
            que = QuotesFrom(request.POST,request.FILES)
            print("#######################################################################")
            print(que)
            if que.is_valid():
                img = que.cleaned_data['Quote_image']#use cleanes_data when you want to get data from user side
                cap = que.cleaned_data['Quote_caption']
                uid = Registration.objects.filter(user_email=request.session['user'])
                print(uid[0].id)
                a = Quotes(Quote_caption=cap,Quote_image=img,user_name_id=uid[0].id)
                a.save()
                return redirect('mainpage')
        else:
            que = QuotesFrom()
            return render(request,"quotes.html",{'quote':que})
    else:
        return redirect('login')

def quotesupadte(request,id):
    if "user" in request.session:
        if request.method == "POST":
            q = Quotes.objects.get(id=id)
            que = QuotesFrom(request.POST,request.FILES,instance=q)
            if que.is_valid():
                que.save()
                return redirect('mainpage')
        else:
            print("hello")
            q = Quotes.objects.get(id=id)
            que = QuotesFrom(instance=q)
            return render(request,"quotesupdate.html",{'quote':que})
    else:
        return redirect('login')


def quotesdelete(request,id):
    if "user" in request.session:
        que=Quotes.objects.get(id=id)
        que.delete()
        return redirect('mainpage')
    else:
        return redirect('login')

def login(request):
    log = LoginFrom(request.POST)
    if log.is_valid():
        email=request.POST['user_email']
        password=request.POST['user_password']
        print(email,password)
        try:
            valid = Registration.objects.get(user_email=email)
            if valid.user_password == password:
                request.session['user'] = valid.user_email
                return redirect('mainpage')
            else:
                return HttpResponse("Invalid Password")
        except:
            return HttpResponse("Invalid Email")
    else:
        log = LoginFrom()
        return render(request,"login.html",{'login':log})

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('Homepage')
    return redirect('Homepage')

def settings(request):
    if "user" in request.session:
        setting = Registration.objects.filter(user_email=request.session['user'])
        q1 = Quotes.objects.filter(user_name_id=setting[0].id)
        return render(request,"settings.html",{'setting':setting,'quotes':q1})
    else:
        return redirect('login')


def delete(request,id):
    if "user" in request.session:
        reg = Registration.objects.get(id=id)
        reg.delete()
        return redirect('Homepage')
    else:
        return redirect('login')

def update(request,id):
    if "user" in request.session:
        s1 = Registration.objects.filter(id=id)
        print(s1[0].user_email)
        if request.session['user'] == s1[0].user_email:
            if request.method == "POST":
                u = Registration.objects.get(id=id)
                upd = RegistrationFrom(request.POST,request.FILES,instance=u)
                if upd.is_valid():
                    upd.save()
                    return redirect('mainpage')
            else:
                u = Registration.objects.get(id=id)
                upd = RegistrationFrom(instance=u)
                return render(request,"update.html",{'user':u,'update':upd})
        else:
            return redirect('settings')
    else:
        return redirect('login')

def quotes_info(request):
    if "user" in request.session:
        setting = Registration.objects.filter(user_email=request.session['user'])
        q1 = Quotes.objects.filter(user_name_id=setting[0].id)
        return render(request,"quotes_info.html",{'setting':setting,'quotes':q1})
    else:
        return redirect('login')

def forgotpassword(request):
    if request.method == "POST":   
        forp = forgotpasswordform(request.POST)
        if forp.is_valid():
            email = request.POST['user_email']
            mobileno = int(request.POST['user_mobile'])
            print(email,type(mobileno))
            try:
                valid = Registration.objects.get(user_email=email)
                print(valid,type(valid.user_mobile))
                if valid.user_mobile == mobileno:
                    otp = random.randint(1000,9999)
                    request.session['otp'] = otp
                    request.session['email']= email
                    print(request.session['otp'])
                    email_send = EmailMessage('From Words_of_feel', 'Hi From Words_of_feel find your one time password {}' .format(otp), to=['devanshi.p.289@gmail.com'])
                    email_send.send()
                    return HttpResponse ('onetimepassword')
                else:
                    return HttpResponse("Invalid Mobile Number")
            except:
                return HttpResponse("Invalid Email Address")
    else:
        forp = forgotpasswordform()
        return render(request,"forgotpassword.html",{'forgotpassword':forp})

def onetimepassword(request):
    if request.method == "POST":
        user_otp = int(request.POST.get('uotp'))
        print(type(user_otp),type(request.session['otp']))
        if user_otp == request.session['otp']:
            return redirect('password')
        else:
            return HttpResponse('Please enter valid One Time Password')
    else:
        return render(request,"onetimepassword.html")

def password(request):
    if request.method == "POST":
        new_password = request.POST.get('unpassword')
        newp = Registration.objects.get(user_email=request.session['email'])
        newp.user_password = new_password
        newp.save()
        return redirect('mainpage')
    else:
        return render(request,"password.html")
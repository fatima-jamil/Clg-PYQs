from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
import smtplib
from django.core.mail import send_mail
from email.message import EmailMessage

# Create your views here.

def index(request):
    return render(request,"index.html")




def stud_login(request):
    eror = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        if user and not user.is_staff:
            login(request,user)
            eror = "yes"
        else :
            eror = "no"
    return render(request,"stud_login.html",locals())



def home(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    return render(request,"home.html")

def upload(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    eror = ""
    if request.method == "POST":
        fn = request.POST['subjectname']
        ln = request.POST['subjectcode']
        un = request.POST['session']
        em = request.POST['department']
        pwd = request.POST['sem123']
        sm = request.POST['semester']
        me = request.POST['midend']
        st = request.POST['subjecttype']
        fl = request.FILES['file']
        try:
            if st and pwd and sm and me:
                Upload.objects.create(usermail = request.user.email,sub_name=fn,sub_code=ln,dept=em,session=un,sem123=pwd,sem=sm,midend=me,pdf=fl,sub_type=st)
                eror="yes"
        except:
            eror="no"
    return render(request,"upload.html" ,locals())

def feedback(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    return render(request,"feedback.html")






def stud_signup(request):
    eror = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['emailid']
        pwd = request.POST['createpassword']

        try:
            if "@iitism.ac.in" in em:
                user = User.objects.create_user(first_name = fn,last_name = ln, username = un, password = pwd, email=em)
                eror = "yes"
            else:
                eror = "no"
        except:
            eror = "no"
    return render(request,"stud_signup.html" , locals())


def Logout(request):
    logout(request)
    return redirect("index")




def firstyear(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    
    paper = Firstyear.objects.all()
    
    if request.method == "POST":
        ses = request.POST['session']
        semester = request.POST['semester']
        midend = request.POST['midend']

        pap = Firstyear.objects.all().filter(session__contains = ses, sem__contains=semester , midend__contains=midend)
        paper = pap
    
    return render(request,"firstyear.html",locals())


def core(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    
    paper = Core.objects.all()
    
    if request.method == "POST":
        dept = request.POST['department']
        ses = request.POST['session']
        semester = request.POST['semester']
        midend = request.POST['midend']

        pap = Core.objects.all().filter(session__contains = ses, sem__contains=semester , midend__contains=midend,dept__contains=dept)
        paper = pap
    
    return render(request,"core.html",locals())


def eso(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    
    paper = ESO.objects.all()
    
    if request.method == "POST":
        dept = request.POST['department']
        ses = request.POST['session']
        semester = request.POST['semester']
        midend = request.POST['midend']

        pap = ESO.objects.all().filter(session__contains = ses, sem__contains=semester , midend__contains=midend,dept__contains=dept)
        paper = pap
    
    return render(request,"eso.html",locals())



def oe(request):
    if not request.user.is_authenticated:
        return redirect("stud_login")
    
    paper = OE.objects.all()
    
    if request.method == "POST":
        dept = request.POST['department']
        ses = request.POST['session']
        semester = request.POST['semester']
        midend = request.POST['midend']

        pap = OE.objects.all().filter(session__contains = ses, sem__contains=semester , midend__contains=midend,dept__contains=dept)
        paper = pap
    
    return render(request,"oe.html",locals())
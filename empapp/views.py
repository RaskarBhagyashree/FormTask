from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from empapp.models import EmpDetail
import string
import re
import datetime
from django.core.mail import send_mail

# Create your views here.
def dashboard(request):
    content={}
    pat=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if request.method=="POST":
        #fetch data from form
        fn=request.POST['fname']
        ln=request.POST['lname']
        bd=request.POST['dob']
        em=request.POST['email']
        ph=request.POST['phone']
        lstyear=bd.split('-')
        bdyear=lstyear[0]
        
        curdt=datetime.datetime.now().year
        diff=curdt-int(bdyear)
        #validation
        if fn=='' or ln=='' or bd=='' or em=='' or ph=='':
            content['errmsg']="Fields cannot be Empty"
            return render(request,'dashboard.html',content)
        elif fn.isalpha()!=True or ln.isalpha()!=True:
            content['errmsg']="Name must contain only letters"
            return render(request,'dashboard.html',content)
        elif not re.fullmatch(pat,em):
            content['errmsg']="Invalid Email"
            return render(request,'dashboard.html',content)
        elif diff<18:
            content['errmsg']="Not Elligible as age is below 18"
            return render(request,'dashboard.html',content)
        elif ph.isdigit()!=True or len(ph)!=10:
            content['errmsg']="Entered phone number is invalid"
            return render(request,'dashboard.html',content)
        else:
            
            emp=EmpDetail.objects.create(fname=fn,lname=ln,dob=bd,email=em,phone=ph)
            emp.save()
            subject="About Form Submission"
            msg="Your have successfully submitted your form "
            sender='kutebhagyashree92@gmail.com'
            send_mail(
                    subject,
                    msg,
                    sender,
                    [em],
                    fail_silently=False,
                    
                )
            return redirect('/empforms')
            
    else:
      
        return render(request,'dashboard.html',content)

def empdata(request):
    emp=EmpDetail.objects.all()
    return render(request,'empform.html',{'data':emp})



    


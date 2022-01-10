from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.urls import reverse 
from ticketSales import views
# Create your views here.

def loginView(request):
  # POST
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return HttpResponseRedirect(reverse(views.timeView))
    else:
      context={
        "username":username,
        "errorMessage":"کاربری با این مشخصات یافت نشد"
      }
      return render(request,"accounts/login.html",context)
    # GET
  else:
    return render(request,'accounts/login.html',{})
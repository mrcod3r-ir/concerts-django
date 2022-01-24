from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ticketSales.models import concertModel,locationModel,timeModel
from django.urls import reverse
import accounts 
from django.contrib.auth.decorators import login_required
from ticketSales.forms import SearchForm


# Create your views here.
def concertListView(request):
  searchForm = SearchForm(request.GET)
  if searchForm.is_valid():
    SearchText = searchForm.cleaned_data["SearchText"]
    concerts = concertModel.objects.filter(Name__contains=SearchText)
  else:
    concerts = concertModel.objects.all()
    
  context = {
    "concertlist":concerts,
    "concertcount":concerts.count(),
    "searchForm":searchForm
  }

  return render(request,"ticketSales/concertList.html",context)

@login_required
def locationListView(request):
  locations = locationModel.objects.all()
  context = {
    "locationlist":locations,
  }

  return render(request,"ticketSales/locationList.html",context)

def concertDetailsView(request,concert_id):
    
  concert=concertModel.objects.get(pk=concert_id)

  context={
      "concertdetails":concert
  }

  return render(request,"ticketSales/concertDetails.html",context)

@login_required
def timeView(request):
  # if request.user.is_authenticated and request.user.is_active:
    times = timeModel.objects.all()
    context = {
      "timeList":times,
    }

    return render(request,"ticketSales/timeList.html",context)
  # else:
    # return HttpResponseRedirect(reverse(accounts.views.loginView))
from django.shortcuts import render
from ticketSales.models import concertModel
from ticketSales.models import locationModel

# Create your views here.
def concertListView(request):
  concerts = concertModel.objects.all()
  context = {
    "concertlist":concerts,
    "concertcount":concerts.count()
  }

  return render(request,"ticketSales/concertList.html",context)

def locationListView(request):
  locations = locationModel.objects.all()
  context = {
    "locationlist":locations,
  }

  return render(request,"ticketSales/locationList.html",context)

def concertDetailsView(request,concert_id):
  concert = concertModel.objects.get(pk=concert_id)

  context = {
    "concertDetails":concert
  }
  
  return render(request,"ticketSales/concertDetails.html",context)
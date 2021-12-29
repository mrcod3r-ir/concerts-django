from django.shortcuts import render
from ticketSales.models import concertModel,locationModel,timeModel

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
    
  concert=concertModel.objects.get(pk=concert_id)

  context={
      "concertdetails":concert
  }

  return render(request,"ticketSales/concertDetails.html",context)

def timeView(request):
  times = timeModel.objects.all()
  context = {
    "timeList":times,
  }

  return render(request,"ticketSales/timeList.html",context)
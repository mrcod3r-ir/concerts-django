from django.shortcuts import render
from ticketSales.models import concertModel

# Create your views here.
def concertListView(request):
  concerts = concertModel.objects.all()
  context = {
    "concertlist":concerts,
    "concertcount":concerts.count()
  }

  return render(request,"ticketSales/concertList.html",context)

from django.shortcuts import render
from django.http import HttpResponse
from ticketSales.models import concertModel

# Create your views here.
def concertListView(request):
  concerts = concertModel.objects.all()

  text= """
  
  <!DOCTYPE html>
  <html>
    <head></head>
    <body>
      <h1>لیست کنسرت ها</h1>
      <ul>
        {}
      </ul>
    </body>
  </html>

  """.format('\n'.join('<li>{}</li>'.format(concert) for concert in concerts))
  return HttpResponse(text)


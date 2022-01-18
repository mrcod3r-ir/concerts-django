from django.urls import path
from accounts import views

urlpatterns = [
    path('login/',views.loginView),
    path('logout/',views.logoutView),
    path('profile/',views.profileView),
]
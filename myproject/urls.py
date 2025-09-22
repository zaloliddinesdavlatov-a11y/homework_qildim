from django.urls import path
from.views import salom_beruvchi, shahar_beruvchi, viloyat, users

urlpatterns = [
    path('salom_ber/', salom_beruvchi),
    path('shahar/', shahar_beruvchi),
    path('shahar/viloyat/davlat/', viloyat),
    path('users/', users)
]
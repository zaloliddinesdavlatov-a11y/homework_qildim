from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def salom_beruvchi(request):
    return HttpResponse("Valeykum asssalom")



def shahar_beruvchi(request):
    return HttpResponse("Termez")




def viloyat(request):
    return HttpResponse("Termez shahar, surxandaryo viloyati. O'zbekiston davlat")


def users(request):
    return HttpResponse("Ism:Jaloliddin , Familya: Eshdavlatov, Raqam:+998932601226, rasm:...., Avtobiografiyasi:Eshdavlatov Jaloliddin Xurshidovich, Tug'ilgan sana:26.06.2012")
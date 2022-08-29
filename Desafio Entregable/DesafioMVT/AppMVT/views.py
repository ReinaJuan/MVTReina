from django.shortcuts import render
from django.http import HttpResponse
from AppMVT.models import Familiar





# Create your views here.

def familiares(request):
    
    familiar1= Familiar(nombre="Susana", parentesco="Madre", dni=22526985, nacimiento="1970-05-25")
    familiar1.save()
    familiar2= Familiar(nombre="Federico", parentesco="Hermano", dni=22526985, nacimiento="1985-08-20")
    familiar2.save()
    familiar3= Familiar(nombre="Gustavo", parentesco="Padre", dni=22526985, nacimiento="1960-08-30")
    familiar3.save()
    lista=[familiar1, familiar2, familiar3]
    
    return render(request, "AppMVT/familiares.html",{"listita":lista})
    
    
    



    
    

    
   


    
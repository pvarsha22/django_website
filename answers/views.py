from django.shortcuts import render

# Create your views here.
from . import models


def video(request):
    obj6 = models.Item6.objects.all()
    obj7 = models.Item7.objects.all()
    obj8 = models.Item8.objects.all()
    obj9 = models.Item9.objects.all()
    obj10=models.Item10.objects.all()
    obj11=models.Item11.objects.all()
    obj12 = models.Item12.objects.all()
    return render(request,'video.html',{'obj6':obj6,'obj7':obj7,'obj8':obj8,'obj9':obj9,'obj10':obj10,'obj11':obj11,'obj12':obj12})
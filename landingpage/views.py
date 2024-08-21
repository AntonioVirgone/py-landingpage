from django.shortcuts import render
from django.http import HttpResponse
from .models import Landingpage


# Create your views here.
def index(request):
    landingpageList = Landingpage.objects.all()
    print(landingpageList[0].message)

    for landingpage in landingpageList:
        print(landingpage.message)

    # Modo uno per passare valori al template
    context = {}
    context['title'] = landingpageList[0].title
    context['message'] = landingpageList[0].message

    return render(request, 'landingpage/index.html', context)


def home(request):
    landingpageList = Landingpage.objects.all()

    # Modo due per passare valori al template
    context = { "landingpage" : landingpageList[1] }

    return render(request, 'landingpage/home.html', context)
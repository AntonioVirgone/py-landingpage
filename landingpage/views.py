from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
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


def test(request):
    return HttpResponse("Hello from HttpResponse!")


# Come usare le view con le classi
class LandingpageView(TemplateView):
    # questa è una property di TemplateView e va passato il nome del template html che si vuole usare
    template_name = 'landingpage/blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["landingpage"] = Landingpage.objects.all()[1]
        return context

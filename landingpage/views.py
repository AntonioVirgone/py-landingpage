from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator

from datetime import datetime

from articles.models import Article

from .models import Landingpage


# Create your views here.
def index(request):
    landingpageList = Landingpage.objects.all()
    print(landingpageList[0].message)

    for landingpage in landingpageList:
        print(landingpage.message)

    # Modo uno per passare valori al template
    context = {}
    context["title"] = landingpageList[0].title
    context["message"] = landingpageList[0].message

    return render(request, "landingpage/index.html", context)


def home(request):
    landingpageList = Landingpage.objects.all()

    # Modo due per passare valori al template
    context = {"landingpage": landingpageList[1]}

    return render(request, "landingpage/home.html", context)


def test(request):
    return HttpResponse("Hello from HttpResponse!")


# Come usare le view con le classi
class LandingpageView(TemplateView):
    # questa è una property di TemplateView e va passato il nome del template html che si vuole usare
    template_name = "landingpage/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["landingpage"] = Landingpage.objects.all()[1]

        articles = Article.objects.filter(status="PUBLISHED").order_by("-published")
        # Si ottiene lo stesso risultato di sopra
        # articles = Article.objects.exclude(status='DRAFT').order_by('-published')
        article_list = articles[3:]

        context["banner"] = articles[0]
        context["highlights"] = articles[1:3]
        # context['article_list'] = articles

        context["archives"] = self.get_previous_month()
        
        context["categories"] = Article.CATEGORIES

        paginator = Paginator(article_list, 3)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj

        return context

    def get_previous_month(self):
        previous_months = []

        for i in range(12):
            month = datetime.now().month - i
            year = datetime.now().year

            if month <= 0:
                month += 12
                year -= 1
            previous_months.append(
                {"month": month, "year": year, "date": datetime(year, month, 1)}
            )

        return previous_months

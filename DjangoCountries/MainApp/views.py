# from msilib.schema import ListView

from django.shortcuts import render
from django.views import View
import json
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from MainApp.models import Country, Language


class CountriesListView(View):
    def get(self, request, *args, **kwargs):
        countries = Country.objects.all().order_by('name')
        paginator = Paginator(countries, 10)
        num_page = request.GET['page'] if 'page' in request.GET else 1
        page_objects = paginator.get_page(num_page)
        return render(request, 'countries.html', {'country_list': page_objects,
                                                  'alfavit': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                  'paginator': page_objects.paginator})

# class CountriesListView(ListView):
#     template_name = 'countries.html'
#     paginate_by = 10
#     queryset = Country.objects.all().order_by('name')
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['alfavit'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         return context


class CountrySort(View):
    def get(self, request, *args, **kwargs):
        countries = Country.objects.filter(name__istartswith=kwargs['latter'])
        return render(request, 'countries.html', {'country_list': countries, 'alfavit': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'})


class RenderHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['test'] = 'DjangoCountries'
        return data


class CountriesNameView(View):
    def get(self, request, *args, **kwargs):
        country = Country.objects.get(pk=kwargs['pk'])
        return render(request, 'detale.html', {'text': country, 'languages': country.language.all()})


class LanguagesListView(View):
    def get(self, request, *args, **kwargs):
        languages = Language.objects.all()
        return render(request, 'languages.html', {'text': languages})


class LanguageCountries(View):
    def get(self, request, *args, **kwargs):
        language = Language.objects.get(pk=kwargs['pk'])
        return render(request, 'lang_countries.html', {'text': language.countries.all()})

from django.shortcuts import render
from django.views import View
import json
from django.views.generic import TemplateView

from MainApp.models import Country, Language


class CountriesListView(View):
    def get(self, request, *args, **kwargs):
        countries = Country.objects.all()

        return render(request, 'countries.html', {'test': countries})


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
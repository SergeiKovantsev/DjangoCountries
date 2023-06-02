from django.urls import path
from .views import *


urlpatterns = [
    path('', RenderHomeView.as_view(), name='home'),
    path('countries_list/', CountriesListView.as_view(), name='countries'),
    path('countries_name/<int:pk>/', CountriesNameView.as_view(), name='personal'),
    path('languages/', LanguagesListView.as_view(), name='languages'),
    path('lang_country/<int:pk>/', LanguageCountries.as_view(), name='name'),
    path('country_sort/<str:latter>/', CountrySort.as_view(), name='sort')

]
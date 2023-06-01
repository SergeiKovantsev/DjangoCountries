from django.urls import path
from .views import *


urlpatterns = [
    path('', RenderHomeView.as_view()),
    path('countries_list/', CountriesListView.as_view(), name='countries'),
    path('countries_name/<int:pk>/', CountriesNameView.as_view(), name='personal'),
    path('languages/', LanguagesListView.as_view(), name='languages'),

]
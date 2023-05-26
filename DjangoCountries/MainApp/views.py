from django.shortcuts import render

# Create your views here.
from django.views import View


# class RenderHomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html', {'test': 'Привет специалист!!!'})

from django.views.generic import TemplateView


class RenderHomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['test'] = 'Привет мир!'
        return data

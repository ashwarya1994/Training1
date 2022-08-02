from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import models
# Create your views here.

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('Class based View')

class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = '''BASIC INJECTION
#          def get_context_data(self,**kwargs):
#              context = super().get_context_data(**kwargs)
#             context['injectme'] = 'BASIC INJECTION'
#             return context'''
#         return context


class SchoolListView(ListView):
    # or u can use context to define variable manually
    context_object_name = 'schools'
    model = models.School
    template_name = 'basicapp/schoollist.html'

    # models.school retruns school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basicapp/schooldetail.html'

class SchoolCreateView(CreateView):
    fields = '__all__'
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basicapp:list')

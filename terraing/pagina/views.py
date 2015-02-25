from django.views import generic
from . import models
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from pagina.models import Entry
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

def first_view(request):
    return HttpResponse('Esta es mi primera vista!')
# Create your views here.

class BlogIndex(ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 9


class BlogDetail(DetailView):
    model = models.Entry
    template_name = "post.html"


# class BlogIndex(generic.ListView):
#     queryset = models.Entry.objects.published()
#     template_name = "home.html"
#     paginate_by = 9


# class BlogDetail(generic.DetailView):
#     model = models.Entry
#     template_name = "post.html"



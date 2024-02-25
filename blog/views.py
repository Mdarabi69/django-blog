from django.shortcuts import render

from django.views import generic


class BlogHomeView(generic.TemplateView):
    template_name = 'blog/index.html'
    

from multiprocessing import context
from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import (
    Userprofile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

# Create your views here.
from django.views import generic

from . forms import ContactForm

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def context(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
    testimonials = Testimonial.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    blogs = Blog.objects.filter(is_active=True)
    portfolio = Portfolio.objects.filter(is_active=True)
    context["testimonials"] = testimonials
    context["certificates"] = certificates
    context["blogs"] = blogs
    context["portfolio"] = portfolio
    def __str__(self):
             return context
    
class ContactView(generic.FormView):
      template_name = "main/contact.html"
      form_class = ContactForm
      success_url = "/"

      def form_valid(self, form):
           form.save()
           messages.success(self.request, 'Thank you. We will be in touch')
           return super().form_valid(form)
      
class PortfolioView(generic.ListView):
      model =Portfolio
      template_name = "main/portfolio.html"
      paginate_by = 10

      def get_queryset(self) -> QuerySet[Any]:
            return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.Detailview):
      model = Portfolio
      template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
      model= Blog
      template_name = "main/blog.html"
      paginate_by = 10

      def get_queryset(self):
            return super().get_queryset().filter(is_active=True)
       
      class BlogDetailView(generic.DetailView):
            model = Blog
            template_name = "main/blog-detail.html"

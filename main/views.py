from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.views.static import serve

# Create your views here.

def serve_static(request, path):
    return serve(request, path, document_root=settings.STATICFILES_DIRS[0])


# class Index(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, 'main/index.html', {})

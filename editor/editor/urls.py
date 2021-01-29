""" editor/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('editor/', include('apps.products.urls')),
]

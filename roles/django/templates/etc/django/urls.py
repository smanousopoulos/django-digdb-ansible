"""amyklaion URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('{{django.app}}.urls')),
]

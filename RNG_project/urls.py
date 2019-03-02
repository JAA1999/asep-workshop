"""RNG_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from RNG import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rng/', include('RNG.urls')),
    # above maps any URLs starting
    # with rng/ to be handled by
    # the RNG application.
    url(r'^admin/', admin.site.urls),
]


    # So fellas, just using the rango
    # URL mapping stuff but replacing
    # 'rango' with 'rng'. Be careful,
    # given folder names RNG in caps
    # but it's likely bad practise to
    # use caps in URLS.

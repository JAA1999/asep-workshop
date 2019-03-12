from django.conf.urls import url
from RNG import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

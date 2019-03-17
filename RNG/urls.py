from django.conf.urls import url
from RNG import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
	
    url(r'^category/$', views.category, name='category'),
	
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^game/$', views.signup, name='game'),
]


from django.conf.urls import url
from RNG import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/', views.category, name='category'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^game', views.signup, name='game'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

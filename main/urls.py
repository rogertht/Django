from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^vaatatootaja/', views.vaatatootaja, name='vaatatootaja'),
  url(r'^lisatootaja/', views.lisatootaja, name='lisatootaja'),
  url(r'^kustutatootaja/', views.kustutatootaja, name='kustutatootaja'),
  url(r'^lisaasutus/', views.lisaasutus, name='lisaasutus'),
  url(r'^vaata_asutusi/', views.vaata_asutusi, name='vaata_asutusi'),
  url(r'^sisesta_tunnid/', views.sisesta_tunnid, name='sisesta_tunnid'),
  url(r'^vaata_tootundide_summasid/', views.vaata_tootundide_summasid, name='vaata_tootundide_summasid')
]

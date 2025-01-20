from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diziler", views.diziler, name="diziler"),
    path("diziler/<int:id>", views.dizi_detay, name="dizi_detay"),
    path("kategoriler", views.kategoriler, name="kategoriler")
]

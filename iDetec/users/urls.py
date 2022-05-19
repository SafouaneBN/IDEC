from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dash'),
    path('home/', views.home),
    path('add/', views.create),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('upload/', views.upload, name='upload'),
    #anomalies
    path('anomalies/<int:id>/add', views.addAnom, name='add-ano'),
    path('anomalies/', views.listAnom, name='list-ano'),
    path('listanomali/', views.listanno),
    path('showAno/<int:id>', views.showAno),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

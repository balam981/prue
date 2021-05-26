from django.urls import path

from APP1 import views

urlpatterns = [
  
    path('home/', views.home, name ="home"),
    path('servicios/', views.servicios, name ="servicios"),
    path('tienda/', views.tienda, name ="tienda"),
    path('blog/', views.blog, name ="blog"),
    path('contacto/', views.contacto, name ="contacto"),
     
]
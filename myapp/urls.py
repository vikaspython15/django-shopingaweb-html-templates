from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('electronic',views.electronic, name='electronic'),
    path('fashion',views.fashion, name='fashion'),
    path('jewellery',views.jewellery, name='jewellery'),
]
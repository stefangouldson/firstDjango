from django.conf.urls import url
from first_app import views
from django.urls import path

app_name = 'first_app'

urlpatterns = [
    path('', views.first_app,name='first_app'),
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]
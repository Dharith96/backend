from django.urls import path
from . import views

urlpatterns = [

    # /Search/
    path('', views.index, name= 'index'),

    # /Search/4/
    path('<int:location_id>/', views.detail, name='detail'),
]
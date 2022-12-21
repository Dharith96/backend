from django.urls import path
from . import views

urlpatterns = [
    path('signin/', view=views.sinin, name='sinin'),
    path('', view=views.home, name='home'),
    path('contactus/', view=views.contactus, name='contactus'),
    path('lasvegas/', view=views.lasvegas, name='lasvegas'),
    path('signup/', view=views.signup, name='signup'),  
        # /home/4/
    path('<int:location_id>/', views.detail, name='detail'),
]
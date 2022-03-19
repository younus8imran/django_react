from django.urls import path, include 

from rest_framework.routers import DefaultRouter 
from rest_framework.authtoken import views

from rest_framework.authtoken.views import obtain_auth_token

from .views import LeadViewSet  

router = DefaultRouter()
router.register('lead', LeadViewSet, basename='lead')

urlpatterns = [
	path('api/', include(router.urls)),	
	#path('login/', views.obtain_auth_token),
]
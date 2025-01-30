"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from women.views import WomenViewSet
from rest_framework import routers
=======
from django.urls import path
from women.views import *
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
>>>>>>> b02ee8ac92253d09a7e772900e29e023483d0d7a

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)
urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path("api/v1/", include(router.urls)),

    # path("api/v1/womenlist/", WomenAPIView.as_view()),
    # path("api/v1/womenlist/<int:pk>/", WomenAPIView.as_view()),
=======
    path("api/v1/womenlist/", WomenViewSet.as_view({'get': 'list'})),
    path("api/v1/womenlist/<int:pk>/",  WomenViewSet.as_view({'put': 'update'})),
    # path("api/v1/womendetail/<int:pk>/", WomenAPIDetailView.as_view()),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
>>>>>>> b02ee8ac92253d09a7e772900e29e023483d0d7a
]

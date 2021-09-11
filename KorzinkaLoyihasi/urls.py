"""KorzinkaLoyihasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_api/', include('rest_framework.urls', namespace='rest_framework')),
    path('korzinka_api/', include('korzinka_api.urls')),
    #path('djoser/', include('djoser.urls')),
    #path('djoser/', include('djoser.urls.authtoken')),
    #path('djoser/', include('djoser.urls.jwt')),
    #path('rest-auth/', include('rest_auth.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('silk', include('silk.urls', namespace='silk')),
]


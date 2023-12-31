"""
URL configuration for CrunchySpoof project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from episodes.urls import router_episodes
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="CrunchySpoof documentation",
      default_version='v1',
      description="Blog Documentation",
      terms_of_service="",
      contact=openapi.Contact(email="carlosochoa@tae.capital"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('anime_list.urls')),
    path('api/', include('rating.urls')),
    path('api/', include('episodes.urls')),
    path('api/', include('episode_comment.urls')),
         ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

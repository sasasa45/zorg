"""zorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from item.views import ZorgList, ZorgDetail, email, contact, info_code, language
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ZorgList.as_view(), name='main'),
    path('contacts/', contact, name='contacts'),
    path('info/', info_code, name='info'),
    path('<slug:slug>/', ZorgDetail.as_view(), name='detail'),
    path('email', email, name='email'),
    path('language/<slug:slug>/', language, name='language'),
    path('tinymce/', include('tinymce.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

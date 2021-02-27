"""MinorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from testapp import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.home_blood),
    url(r'^home/', views.home_blood),
    url(r'^search_blood_group/', views.search_blood_group_view, name="search_blood_group"),
    url(r'^ask_help/$', views.helper_view, name="ask_help"),
    url(r'^confirmed/$', views.donner_confirm, name="confirmed"),
    url(r'^register/', views.register_for_donner, name="register"),
    url(r'^feedback/', views.feedback_view, name="feedback"),
    url(r'^contact/', views.contact_us, name="contact"),
    url(r'^suggest/', views.suggestions, name="suggest"),
    url(r'^problem/', views.problem, name="problem"),
    url(r'^gallery/', views.gallery, name="gallery"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.BASE_DIR, document_root=settings.STATIC_URL)



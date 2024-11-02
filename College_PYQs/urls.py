"""
URL configuration for College_PYQs project.

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
from django.urls import path
from pyqs.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('home', home, name = "home"),
    path('stud_login', stud_login, name = "stud_login"),
    path('admin_login', admin_login, name = "admin_login"),
    path('stud_signup', stud_signup, name = "stud_signup"),
    path('logout', Logout, name = "logout"),
    path('admin_logout', admin_Logout, name = "admin_logout"),
    path('upload', upload, name = "upload"),
    path('uploadedpyqs', uploadedpyqs, name = "uploadedpyqs"),
    path('feedback', feedback, name = "feedback"),
    path('firstyear', firstyear, name = "firstyear"),
    path('core', core, name = "core"),
    path('eso', eso, name = "eso"),
    path('oe', oe, name = "oe"),
    path('admin_home', admin_home, name = "admin_home"),
    path('delete_paper/<int:id>', delete_paper, name = "delete_paper"),
    path('add_paper/<int:id>', add_paper, name = "add_paper"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
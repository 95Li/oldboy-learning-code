"""days70_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
from app01 import session_views
from app01 import CBV_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book_list/',views.book_list),
    url(r'^login/',views.login),
    
    url(r'^se_book_list/',session_views.book_list),
    url(r'^se_login/',session_views.login),
    
    url(r'^cbv_book_list/',CBV_views.Book_view.as_view()),
    url(r'^cbv_login/',CBV_views.Login_view.as_view()),
    
]

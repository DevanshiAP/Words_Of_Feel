"""words_of_feel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from words_of_feelapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name='Homepage'),
    path('registration/',views.registration,name='registartion'),
    path('userinfo/',views.user_info,name='userinfo'),
    path('quotes/',views.quotes,name='quotes'),
    path('mainpage/',views.mainpage,name='mainpage'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('settings/',views.settings,name='settings'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('quotesinfo/',views.quotes_info,name='quotesinfo'),
    path('quotesupadte/<int:id>',views.quotesupadte,name='quotesupadte'),
    path('quotesdelete/<int:id>',views.quotesdelete,name='quotesdelete'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('onetimepassword/',views.onetimepassword,name='onetimepassword'),
    path('password/',views.password,name='password')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

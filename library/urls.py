"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from library import views
from rest_framework.urlpatterns import format_suffix_patterns


#Aqui nos endpoints o admin/ vai para o site 
#library/ exibe uma visao geral dos books cadastrados
#library/<id> exibe uma visão do book de id = <id>
#booklist/ vai para um html que criei que mostra visualmente as informações dos books 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', views.book_list),
    path('library/<int:id>', views.book_detail),
    path('booklist/', views.booklist),
    path('', views.home)
]

urlpatterns = format_suffix_patterns(urlpatterns)

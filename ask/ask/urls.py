"""ask URL Configuration

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
from django.urls import path, re_path

from qa import views as qav

urlpatterns = [
    re_path('admin/', admin.site.urls),
    path('', qav.get_new, name='news'),
    re_path('login/', qav.test),
    re_path('signup/', qav.test),
    re_path(r'question/(?P<pk>\d+)/', qav.get_question, name='question_detail'),
    re_path('ask/', qav.ask, name='add_ask'),
    re_path('popular/', qav.populars, name='populars'),
    re_path('new/', qav.test),
]

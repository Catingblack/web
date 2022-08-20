"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
     """path('/', include('qa.urls')),
    path('/login/', include('qa.urls')),
    path('/signup/', include('qa.urls')),
    path('/ask/', include('qa.urls')),
    path('/popular/', include('qa.urls')),
    path('/new/', include('qa.urls')),
    path('/question/<int:id>/', include('qa.urls')),
    path('admin/', admin.site.urls), """ 
    
    
    url(r'^$', include('qa.urls')),
    url(r'^login/', include('qa.urls')),
    url(r'^signup/', include('qa.urls')),
    url(r'^ask/', include('qa.urls')),
    url(r'^popular/', include('qa.urls'))
    url(r'^new/', include('qa.urls')),
    url(r'^question/(\d+)/', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
]



from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
    path('question/<int:id>/', views.question_details, name='question'),
    
    #path('login/', include('qa.urls')),
    #path('signup/', include('qa.urls')),
    #path('ask/', include('qa.urls')),
    #path('admin/', admin.site.urls), 
   
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.new, name='new'),
    path('popular/', views.popular, name='popular'),
    path('question/<int:id>/', views.question_details, name='question'),
    path('ask/', views.ask_question, name='ask_question'),
    
    #path('login/', include('qa.urls')),
    #path('signup/', include('qa.urls')),
    #path('admin/', admin.site.urls), 
   
]
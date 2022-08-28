from django.urls import path

from . import views

urlpatterns = [
    path('', views.new, name='new'),
    path('popular/', views.popular, name='popular'),
    path('question/<int:id>/', views.question_details, name='question'),
    path('ask/', views.ask_question, name='ask_question'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    #path('admin/', admin.site.urls), 
   
]
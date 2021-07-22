from django.urls import path,include
from django.contrib.auth import views as auth_views
from portfolio_backapp import views 

app_name = 'portfolio_backapp'

urlpatterns = [
    # path('register/', views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name= 'portfolio_backapp/login.html'), name='login',
    # kwargs={'redirect_authenticated_user':True}),
    # path('logout/', auth_views.LogoutView.as_view(template_name= 'portfolio_backapp/logout.html'), name='logout'),

]

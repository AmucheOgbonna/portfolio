from django.urls import path
from portfolio_app import views

app_name = 'portfolio_app'

urlpatterns = [
    path('', views.blog_single, name='blog_single'),
    # path('<slug:slug>', views.blog_single, name='blog_single'),
    
]
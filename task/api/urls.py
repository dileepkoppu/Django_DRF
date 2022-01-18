from django.urls import path

from .views import SignupView,updateView,homeListView,welcome



app_name = 'api'




urlpatterns = [
    path('',welcome,name="welcome"),
    path('signup/',SignupView.as_view(),name='signup'),
    path('home/',homeListView.as_view(),name='home'),
    path('update/<int:pk>/',updateView.as_view(),name='update')
]
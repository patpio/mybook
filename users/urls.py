from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpPageView.as_view(), name='signup'),
    path('<int:pk>/', views.UserProfile.as_view(), name='profile')
]

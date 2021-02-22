from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpPageView.as_view(), name='signup'),
    path('profile/', views.user_profile, name='profile')
]

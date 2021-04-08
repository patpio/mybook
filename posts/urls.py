from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.CreatePost.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('list/', views.PostList.as_view(), name='list'),
    path('edit/<int:pk>/', views.UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]

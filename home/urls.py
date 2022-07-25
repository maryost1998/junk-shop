from django.urls import path, re_path
from home.views import HomeView, AboutView, PostCreateView, MyPostsView, PostDetailView, PostDeleteView, PostEditView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>', MyPostsView.as_view(), name='my_post'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post_edit'),

]

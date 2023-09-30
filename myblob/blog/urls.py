from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, \
    CategoryView, CategoryListView, LikeView, PasswordsChangeView, AddCommentsView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/remove/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('<int:pk>/password/', PasswordsChangeView.as_view(template_name="change_password.html")),
    path('article/<int:pk>/add_comment/', AddCommentsView.as_view(), name="add_comment"),

]

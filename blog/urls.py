from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, CommentViewSet, home, LogoutView

# 📦 Негізгі роутер — /posts/
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

# 🔁 Пост ішіндегі комментарийлер үшін nested роутер — /posts/<post_id>/comments/
posts_router = NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', home, name='home'),  # Басты бет
    path('auth/', obtain_auth_token, name='login'),  # Логин /auth/
    path('logout/', LogoutView.as_view(), name='logout'),  # Логаут /logout/

    path('', include(router.urls)),  # /posts/
    path('', include(posts_router.urls)),  # /posts/<post_id>/comments/


]

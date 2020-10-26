from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

post_router = DefaultRouter()
post_router.register('posts', PostViewSet, basename='posts')

comment_router = DefaultRouter()
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [

    path('v1/', include(post_router.urls)),
    path('v1/posts/<int:post_id>/', include(comment_router.urls)),

]

urlpatterns += [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
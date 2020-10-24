from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cat', views.CategoryViewSet)
router.register(r'pro', views.ProductViewSet)





urlpatterns = [
    path('', include(router.urls)),
    path('setcat/', views.SetCategory.as_view())
]

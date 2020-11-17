from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'categorySet', views.CategoryViewSet)
router.register(r'productSet', views.ProductViewSet)





urlpatterns = [
    path('', include(router.urls)),
    path('category/<str:slug_title>', views.CategoryView.as_view()),
    path('product/<str:slug_title>', views.ProductView.as_view()),
]

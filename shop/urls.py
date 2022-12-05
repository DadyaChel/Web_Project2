from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/shop/
    path('', views.list_item, name='list_item'),
    # http://127.0.0.1:8000/shop/<int:id>/
    path('<int:id>/', views.detail_item, name='detail_item'),
]
from django.urls import path, include
from . import views


urlpatterns = [
    path('block/list/', views.BlockListView.as_view(), name='block_list'),
    path('block/create/', views.BlockListView.as_view(), name='block_create'),
    path('block/<int:pk>/', views.BlockListView.as_view(), name='block_detail'),
    path('flat/<int:pk>/', views.FlatListView.as_view(), name='flat_detail'),
    # path('flat/<int:pk>/', views.FlatListView.as_view(), name='flat_detail'),

]
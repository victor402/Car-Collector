from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_gassing/', views.add_gassing, name='add_gassing'),
    path('cars/<int:car_id>/assoc_detail_shop/<int:detail_shop_id>/', views.assoc_detail_shop, name='assoc_detail_shop'),
    path('detail_shops/', views.DetailShopList.as_view(), name='detail_shops_index'),
    path('detail_shops/<int:pk>/', views.DetailShopDetail.as_view(), name='detail_shops_detail'),
    path('detail_shops/create/', views.DetailShopCreate.as_view(), name='detail_shops_create'),
    path('detail_shops/<int:pk>/update/', views.DetailShopUpdate.as_view(), name='detail_shops_update'),
    path('detail_shops/<int:pk>/delete/', views.DetailShopDelete.as_view(), name='detail_shops_delete'),
   ]
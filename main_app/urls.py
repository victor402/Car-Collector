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
    path('cars/<int:car_id>/assoc_detailshop/<int:detailshop_id>/', views.assoc_detail_shop, name='assoc_detailshop'),
    path('detailshops/', views.DetailerList.as_view(), name='detailshops_index'),
    path('detailshops/<int:pk>/', views.DetailerDetail.as_view(), name='detailshops_detail'),
    path('detailshops/create/', views.DetailerCreate.as_view(), name='detailshops_create'),
    path('detailshops/<int:pk>/update/', views.DetailerUpdate.as_view(), name='detailshops_update'),
    path('detailshops/<int:pk>/delete/', views.DetailerDelete.as_view(), name='detailshops_delete'),
   ]
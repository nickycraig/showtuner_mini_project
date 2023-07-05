from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('composers/', views.ComposerList.as_view(), name="composer_list"),
    path('composers/new/', views.ComposerCreate.as_view(), name="composer_create"),
    path('composers/<int:pk>/', views.ComposerDetail.as_view(), name="composer_detail"),
    path('composers/<int:pk>/update', views.ComposerUpdate.as_view(), name="composer_update"),
    path('composers/<int:pk>/delete', views.ComposerDelete.as_view(), name="composer_delete"),
    path('composers/<int:pk>/shows/new', views.ShowCreate.as_view(), name="show_create"),
    path('favorites/<int:pk>/shows/<int:show_pk>/', views.FavoriteShowAssoc.as_view(), name="favorite_show_assoc"),
]
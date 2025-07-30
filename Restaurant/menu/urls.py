from django.urls import path
from .views import MenuListView, MenuDetailView, MenuItemCreateView, MenuItemUpdatePriceView

urlpatterns = [
    path("menus/", MenuListView.as_view(), name="menu_list"),
    path("menu/<int:pk>/", MenuDetailView.as_view(), name="menu_detail"),
    path("menuitem/add/", MenuItemCreateView.as_view(), name="menuitem_add"),
    path("menuitem/<int:pk>/update-price/", MenuItemUpdatePriceView.as_view(), name="menuitem_update_price"),
]

from django.urls import path
from catalog.views import ProductDeleteView, ProductUpdateView, ProductCreateView, MaterialCreateView, \
    MaterialUpdateView, MaterialDeleteView, MaterialListView, MaterialDetailView, ProductListView, ContactsView, \
    ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('material/create/', MaterialCreateView.as_view(), name='create_material'),
    path('material/list/', MaterialListView.as_view(), name='list_material'),
    path('material/view/<int:pk>/', MaterialDetailView.as_view(), name='view_material'),
    path('material/edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit_material'),
    path('material/delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete_material'),
]

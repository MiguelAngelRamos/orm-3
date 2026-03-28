from django.contrib import admin
from django.urls import path
from crud_app.views import ProductoCreateView, ProductoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductoListView.as_view(), name='listar'),
    path('nuevo/', ProductoCreateView.as_view(), name='crear'),
]


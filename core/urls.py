from django.contrib import admin
from django.urls import path
from crud_app.views import ProductoListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductoListView.as_view(), name='producto_list'),
]

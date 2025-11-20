"""
URL configuration for inventoryapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from loginM.login_master import CustomAuthToken
from loginM.views import loginCheck
from inventorycrud.views import get_inventoryList,get_StockoutList
from inventorycrud.add_inventory import add_inventory
from inventorycrud.add_stockout import add_stockout


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/register/', CustomAhToken.as_view()),
    path('api/login/', CustomAuthToken.as_view()),
    # path('api/login/', loginCheck),
    path('api/GetInventoryList/', get_inventoryList),
    path('api/GetStockoutList/', get_StockoutList),
    path('api/AddInventory/', add_inventory),
    path('api/AddStockout/', add_stockout),
]

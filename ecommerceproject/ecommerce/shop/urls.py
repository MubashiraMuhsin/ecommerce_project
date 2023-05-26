
from django.urls import path

from shop import views
app_name = 'shopapp'
urlpatterns = [

    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='Prod_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.ProdDetail,name='Prod_detail'),

]

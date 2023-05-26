from django.urls import path, include

from cartapp import views
app_name = 'cartapp'
urlpatterns = [

    path('Add/<int:product_id>',views.AddtoCart,name='add_cart'),
    path('remove/<int:product_id>',views.cart_remove,name='remove_cart'),
    path('',views.cart_detail,name='to_cart'),
    path('delete/<int:product_id>',views.full_remove,name='full_remove'),

]
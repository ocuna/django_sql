from django.urls import path
from mysql_cart.views import Cookie, SKUshop, SKUdetail, SKUupdate, SKUcreate, SKUdelete, Cart, EmptyCart, Aesspode

urlpatterns = [
    path('shop', SKUshop.as_view()),
    path('shop/add/<int:pk>', SKUshop.as_view(), name="SKUdetail"),
    path('shop/create/', SKUcreate.as_view(), name="SKUcreate"),
    path('shop/detail/<int:pk>', SKUdetail.as_view(), name="SKUdetail"),
    path('shop/update/<int:pk>', SKUupdate.as_view(), name="SKUupdate"),
    path('shop/delete/<int:pk>', SKUdelete.as_view(), name="SKUdelete"),
    path('shop/cart/', Cart ),
    path('shop/cart/empty', EmptyCart ),
    path('cookie/', Cookie, ),
    path('aesspoded-evrahdang/', Aesspode),
    path('cookie/<slug:arg>', Cookie),
]


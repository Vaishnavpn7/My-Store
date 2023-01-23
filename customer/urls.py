from django.urls import path
from customer import views

urlpatterns = [
    path("register", views.SignUpView.as_view(), name="register-cus"),
    path('', views.SigninView.as_view(), name='signin'),
    path('customer/home', views.HomeView.as_view(), name='user-home'),
    path('products/<int:id>', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/carts/<int:id>/add', views.addto_cart, name='add-cart'),
    path('carts/all', views.CartListView.as_view(), name='cart-list'),
    path('order/add/<int:cid>/<int:pid>', views.OrderView.as_view(), name='place-order'),
    path('order/all', views.OrderListView.as_view(), name='my-orders'),
    path('order/<int:id>/cancel', views.calcelorder_view, name='cancel-order'),
    path('customer/account/logout', views.logout_view, name='signout'),

]

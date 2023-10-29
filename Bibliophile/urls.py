from django.contrib import admin
from django.urls import path
from store import views
from cart import views as cv
from superuser import views as suv
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='store/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', suv.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='store/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', suv.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', suv.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', suv.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', suv.update_customer_view,name='update-customer'),

    path('admin-products', suv.admin_products_view,name='admin-products'),
    path('admin-add-product', suv.admin_add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', suv.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', suv.update_product_view,name='update-product'),

    path('admin-view-booking', suv.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', suv.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', suv.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='store/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', cv.add_to_cart_view,name='add-to-cart'),
    path('cart', cv.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', cv.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', cv.customer_address_view,name='customer-address'),
    path('payment-success', cv.payment_success_view,name='payment-success'),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
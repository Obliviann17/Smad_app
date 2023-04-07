from django.template.defaulttags import url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('autorisation', views.login_request, name='autoris'),
    path('registration', views.register_request, name='regist'),
    path('logout', views.logout_request, name='logout'),
    path('404', views.not_found, name='404-error'),
    path('about', views.about, name='about_us'),
    path('delivery', views.delivery, name='delivery'),
    path('create', views.order_create, name='order_create'),
    path('created', views.order_completed, name='order_created'),
    path('contacks', views.contakt, name='contakt'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_page')

]


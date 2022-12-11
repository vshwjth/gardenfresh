from django.urls import path
from . import views

urlpatterns =[
    path('catalog/', views.catalog, name='catalog'),
    path('', views.home, name='home'),
    path('cart/', views.viewcart, name='cart'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('update_item/', views.updateItem, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutpage, name='logout'),
    path('account/', views.account, name='account'),
    path('success/', views.success, name='success'),
]
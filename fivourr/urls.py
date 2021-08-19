"""fivourr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # API PATH

    path('api/', include('API.urls')),

    path('', views.get_landing_page, name="get_landing_page"),
    path('buyer_view/', views.buying_view, name="buying_view"),
    path('gig_details/<int:id>/', views.gig_details, name="gig_details"),

    #user Registration URL
    path('registration/', views.user_registration, name="user_registration"),
    # User Login URL

    path('login/', views.user_login, name="user_login"),

    # Logout URL

    path('logoutview/', views.logoutview, name="logoutview"),

    ## Seller Profile View URL

    path('seller_profile/', views.seller_profile, name="seller_profile"),

    ## Service wise gigs url
    path('gigs/<int:id>/', views.service_wise_gigs, name="service_wise_gigs"),
    # Category wise page
    path("category-wise/", views.categoryWisePage, name="category-wise"),
    # Manage order page url
    path("manage-order/", views.manageOrder, name="manage-order"),
    # Gigs page url
    path("manage-gigs/", views.manageGigs, name="manage-gigs"),
    # Chat inbox url
    path("inbox", views.chatInbox, name="inbox"),
    # Seller Dashboard
    path('seller_dashboard/', views.seller_dashboard, name="seller_dashboard"),

    # cart page or checkout Page

    path('cart/', views.cartView, name="cartView"),

    # Add To Cart

    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),

    # Checkout Page Url

    path('checkout/', views.checkout, name="checkout"),

    # category wise Subcategory

    path('category_wise_subcategory/p=2021/<int:category_id>/', views.category_wise_gigs, name="categoryWiseView"),

    # Settings URL

    path('settings/', views.settings_page, name="settings"),

    # Account url
    path('account/', views.account_page, name="account"),

    # security url

    path('security/', views.security_page, name="security_page"),

    # notifications_page url

    path('notifications/', views.notifications_page, name="notifications_page"),


    # support page url

    path('support/', views.support_page, name="support"),

    # Contacts Page Url

    path('contacts/', views.azim_contact_page, name="contact"),

    # All Category Page Url
    path('categories/', views.view_all_category, name="Categories"),

    # POST A REQUEST PAGE URL
    path('post_request/', views.post_a_request, name="post_a_request"),

    #  Become A Seller Page

    path('become_a_seller/', views.get_become_a_seller_page, name="BecomeSeller"),

    # Buyer Orders Page Url
    
    path('buyer_orders/', views.get_buyer_orders_url, name="BuyerOrders"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
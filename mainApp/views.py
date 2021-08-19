from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min
from .models import Gig
import time
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User


def get_landing_page(request):
    landing_slider = LandingSlider.objects.all().order_by('-id')
    services = Services.objects.all()
    cats = Category.objects.all()

    args = {
        'landing_slider': landing_slider,
        'services': services,
        'cats': cats
    }
    return render(request, 'landingview/landingPage.html', args)


@login_required(login_url='user_login')
def service_wise_gigs(request, id):
    service = Services.objects.all()
    gigs = Gig.objects.filter(service_id=id)
    cats = Category.objects.all()[:6]
    args = {
        'service': service,
        'gigs': gigs,
        'cats': cats
    }

    return render(request, 'landingview/service_wise_gigs.html', args)


@login_required(login_url='user_login')
def view_all_category(request):
    cats = Category.objects.all()

    args = {
        'cats': cats
    }

    return render(request, 'landingview/categories.html')


@login_required(login_url='user_login')
def buying_view(request):
    gigs = Gig.objects.all()
    cats = Category.objects.all()

    pop_gigs = Gig.objects.filter(is_popular=True)
    pop_web_gigs = Gig.objects.filter(pop_web=True)
    pro_gigs = Gig.objects.filter(is_pro=True)

    args = {
        'gigs': gigs,
        'pop_gigs': pop_gigs,
        'cats': cats,
        'pop_web_gigs': pop_web_gigs,
        "pro_gigs": pro_gigs
    }
    return render(request, 'buyingview/buying_view.html', args)

# @login_required(login_url='user_login')


def gig_details(request, id):
    gigs = Gig.objects.filter(id=id).first()

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = DummyUser(user=ip)

    result = DummyUser.objects.filter(Q(user__icontains=ip))

    if len(result) == 1:
        print("It wont Work Dude!")
    elif len(result) > 1:
        print("It wont work either!!")
    else:
        u.save()
        # gigs.gig_click_count = gigs.gig_click_count + 1
        # gigs.save()
    # if request.user:
    #     gigs.gig_click_count = gigs.gig_click_count + 1
    #     gigs.save()
    c = DummyUser.objects.all().count()
    related_gigs = Gig.objects.all()
    args = {
        'gigs': gigs,
        'c': c,
        'related_gigs': related_gigs,
    }
    return render(request, 'buyingview/gigs_details.html', args)


def user_registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('user_login')
    args = {
        'form': form
    }
    return render(request, 'accountview/registration.html', args)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('buying_view')
    return render(request, 'accountview/login.html')


def logoutview(request):
    logout(request)
    return redirect('get_landing_page')


@login_required(login_url='user_login')
def seller_profile(request):
    return render(request, 'accountview/seller.html')

# Category Wise Page


@login_required(login_url='user_login')
def categoryWisePage(requrest):
    return render(requrest, "buyingview/category_wise.html")


# Order page
@login_required(login_url='user_login')
def manageOrder(request):
    return render(request, "wasekPart/manage_order.html")


# Gigs page
@login_required(login_url='user_login')
def manageGigs(request):
    return render(request, "wasekPart/manage_gigs.html")

# Chat inbox


@login_required(login_url='user_login')
def chatInbox(requrest):
    return render(requrest, "wasekPart/chat_inbox.html")

# Seller Dashboard


@login_required(login_url='user_login')
def seller_dashboard(request):
    users = User.objects.all()

    args = {
        'users': users
    }

    return render(request, 'sellingview/seller_dashboard.html', args)


# Settings Page
@login_required(login_url='user_login')
def settings_page(request):
    return render(request, 'sellingview/settings.html')

# Account Page


@login_required(login_url='user_login')
def account_page(request):
    return render(request, 'sellingview/account.html')

# Security Page


@login_required(login_url='user_login')
def security_page(request):
    return render(request, 'sellingview/security.html')

# Notification Page


@login_required(login_url='user_login')
def notifications_page(request):
    return render(request, 'sellingview/notifications.html')

# Support Page


@login_required(login_url='user_login')
def support_page(request):
    return render(request, 'sellingview/support.html')

# Azim Contact Page


@login_required(login_url='user_login')
def azim_contact_page(request):
    return render(request, 'sellingview/contacts.html')


# seller Dashboard End
@login_required(login_url='user_login')
def add_to_cart(request):
    cart = request.session.get('cart')
    package_id = request.POST.get('package_id')
    remove = request.POST.get('remove')

    if request.method == "POST":
        if cart:
            quantity = cart.get(package_id)
            if quantity:
                cart[package_id] = quantity + 1
            else:
                cart[package_id] = 1
        else:
            cart = {}
            cart[package_id] = 1
        request.session['cart'] = cart

        return redirect('cartView')


def map_function(request, package_id):
    cart = request.session.get('cart', None)
    package_id = str(package_id.id)

    if package_id in cart:
        return package_id.price * cart[package_id]


def get_cart_products(request):
    ids = list(request.session.get('cart').keys())
    cart_products = GigManager.get_gig(ids)
    package_prices = list(map(map_function, cart_products))
    print(package_prices)
    total = sum(package_prices)

    args = {'cart_products': cart_products, 'total': total}
    return render(request, 'buyingview/cart.html', args)


@login_required(login_url='user_login')
def cartView(request):
    cart = request.session.get('cart')

    if not cart:
        request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    cart_products = GigManager.get_gig(ids)
    print(cart)
    context = {
        'cart_products': cart_products
    }

    return render(request, 'buyingview/cart.html', context)


@login_required(login_url='user_login')
def checkout(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    cart_products = GigManager.get_gig(ids)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = request.user
        packages = GigManager.get_gig(list(cart.keys()))

        for package in packages:
            checkout = Checkout(
                first_name=first_name,
                last_name=last_name,
                user=user,
                package=package,
                price=package.price,
                quantity=cart.get(str(package.id))
            )

            checkout.save()

            return redirect('BuyerOrders')

        request.session['cart'] = {}
    args = {
        'cart_products': cart_products
    }
    return render(request, 'buyingview/checkout.html', args)


@login_required(login_url='user_login')
def get_buyer_orders_url(request):
    orders = Checkout.objects.filter(user=request.user)
    
    
     
    args = {
        'orders': orders
    }
    return render(request, 'buyingview/buying_orders.html', args)


@login_required(login_url='user_login')
def category_wise_gigs(request, category_id):
    cats = Category.objects.all()
    sub_cats = Subcategory.objects.filter(parent_market_id=category_id)
    # sub_cats = Subcategory.objects.all()

    args = {'sub_cats': sub_cats, 'cats': cats}

    return render(request, 'landingview/category_wise.html', args)


@login_required(login_url='user_login')
def post_a_request(request):
    categories = Category.objects.all()
    delivery_time = DeliveryTime.objects.all()

    post_form = PostRequestForm(request.POST, request.FILES)
    if request.method == 'POST':
        post_form = PostRequestForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()

            print(post_form)

            return redirect('buying_view')
    args = {
        'categories': categories,
        'delivery_time': delivery_time,
        'post_form': post_form
    }
    return render(request, 'buyingview/post_request.html', args)


def get_become_a_seller_page(request):
    return render(request, 'landingview/become_a_seller.html')

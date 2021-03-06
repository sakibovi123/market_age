from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Avg, Max, Min
from django.contrib import messages
from .models import Offer
import time
import os
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import date
from datetime import datetime
import string    
import random


def get_landing_page(request):
    user_session = request.session.get("user", None)
    print(f"{user_session=}")

    if (user_session is None):
        landing_slider = LandingSlider.objects.all().order_by('-id')
        services = Services.objects.all()
        cats = Category.objects.all()

        args = {
            'landing_slider': landing_slider,
            'services': services,
            'cats': cats
        }
        return render(request, 'landingview/landingPage.html', args)
    else:
        return redirect("buying_view")


def service_wise_offers(request, id):
    service = Services.objects.all()
    offers = Offer.objects.filter(service_id=id)
    cats = Category.objects.all()[:6]
    args = {
        'service': service,
        'offers': offers,
        'cats': cats
    }

    return render(request, 'landingview/service_wise_offers.html', args)


@login_required(login_url='user_login')
def view_all_category(request):
    cats = Category.objects.all()

    args = {
        'cats': cats
    }

    return render(request, 'landingview/categories.html', args)


@login_required(login_url='user_login')
def buying_view(request):
    offers = Offer.objects.all().order_by('-click')
    cats = Category.objects.all()

    pop_offers = Offer.objects.filter(is_popular=True)
    pop_web_offers = Offer.objects.filter(pop_web=True)
    pro_offers = Offer.objects.filter(is_pro=True)

    args = {
        'offers': offers,
        'pop_offers': pop_offers,
        'cats': cats,
        'pop_web_offers': pop_web_offers,
        "pro_offers": pro_offers
    }
    return render(request, 'buyingview/buying_view.html', args)

# @login_required(login_url='user_login')


def offer_details(request, id):
    cats = Category.objects.all()
    offers = Offer.objects.filter(id=id).first()
    cart_session = request.session.get("cart", None)

    for image in offers.extra_images.all():
        print(image)

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)

    print(ip)

    u = DummyUser(user=ip)

    result = DummyUser.objects.filter(Q(user__icontains=ip))

    if result is None:
        u.save()
    c = DummyUser.objects.all().count()
    related_offers = Offer.objects.all()

    # ISSUE ##

    # print(packages)

    args = {
        'offers': offers,
        'c': c,
        'related_offers': related_offers,
        'cats': cats,
        "cart_session": cart_session,
    }
    return render(request, 'buyingview/offers_details.html', args)


def user_registration(request):
    user_session = request.session.get("user", None)

    if (user_session is None):
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                request.session["new_user"] = True
                form.save()

                return redirect('user_login')
        args = {
            'form': form
        }
        return render(request, 'accountview/registration.html', args)
    else:
        return redirect("buying_view")


def user_login(request):
    user_session = request.session.get("user", None)
    new_user = request.session.get("new_user", None)

    if (user_session is None):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Creating user session
                user_session = username
                request.session["user"] = user_session
                login(request, user)
                # print("USER SESSION:")
                # print(request.session.get("user"))
                if new_user is not None:
                    return redirect("extended-user")
                return redirect('buying_view')
            else:
                messages.error(request, "Incorrect username or password!")

        return render(request, 'accountview/login.html')
    else:
        return redirect("buying_view")


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
    orders = Checkout.objects.filter(seller=request.user).filter(paid=True).order_by("-id")
    active_orders, late_orders, delivered_orders, completed_orders, cancelled_orders, review_orders = [], [], [], [], [], []

    for order in orders:
        if order.is_complete:
            completed_orders.append(order)
        if order.on_review and order.order_status == "ON REVIEW":
            review_orders.append(order)
        if order.order_status == "ACTIVE":
            active_orders.append(order)
        elif order.order_status == "LATE":
            late_orders.append(order)
        elif order.order_status == "DELIVERED":
            delivered_orders.append(order)
        elif order.order_status == "CANCELLED":
            cancelled_orders.append(order)

    print(review_orders)
    # print(cancelled_orders)

    args = {
        "active_orders": active_orders,
        "late_orders": late_orders,
        "delivered_orders": delivered_orders,
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders,
        "review_orders": review_orders
    }

    return render(request, "wasekPart/manage_order.html", args)


# offers page
@login_required(login_url='user_login')
def manageOffers(request):
    offers = Offer.objects.all().order_by("-id")
    active_offers, pending_approvals, required_modifications, denieds, pauseds = [], [], [], [], []

    for offer in offers:
        if offer.offer_status == "ACTIVE":
            active_offers.append(offer)
        elif offer.offer_status == "PENDING APPROVAL":
            pending_approvals.append(offer)
        elif offer.offer_status == "REQUIRED MODIFICATION":
            required_modifications.append(offer)
        elif offer.offer_status == "DENIED":
            denieds.append(offer)
        elif offer.offer_status == "PAUSED":
            pauseds.append(offer)

    if request.method == "POST":
        offer_id = request.POST.get("offer_id", None)
        print(f"{offer_id=}")

        if offer_id is not None:
            try:
                offer_id = int(offer_id)
            except:
                return redirect("manage-offers")
            else:
                try:
                    offer = Offer.objects.get(id=offer_id)
                    offer.offer_status = "PAUSED"
                    offer.save()
                    return redirect("manage-offers")
                except:
                    return redirect("manage-offers")
        else:
            return redirect("manage-offers")

    args = {
        "active_offers": active_offers,
        "pending_approvals": pending_approvals,
        "required_modifications": required_modifications,
        "denieds": denieds,
        "pauseds": pauseds,
    }
    return render(request, "wasekPart/manage_offers.html", args)

# Chat inbox


@login_required(login_url='user_login')
def chatInbox(requrest):
    return render(requrest, "wasekPart/chat_inbox.html")

# Seller Dashboard


@login_required(login_url='user_login')
def seller_dashboard(request):
    users = User.objects.all()
    active_orders, completed_orders, cancelled_orders = [], [], []
    count_active = Checkout.objects.filter(order_status="ACTIVE").filter(user=request.user).count()
    orders = Checkout.objects.filter(seller=request.user).filter(paid=True).order_by("-id")

    for order in orders:
        if order.is_complete:
            completed_orders.append(order)
        elif order.order_status == "ACTIVE":
            active_orders.append(order)
        elif order.order_status == "CANCELLED" and order.is_cancel:
            cancelled_orders.append(order)

    args = {
        'users': users,
        "active_orders": active_orders,
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders,
        "count_active": count_active
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
    remove = request.POST.get('remove')
    package_id = request.POST.get('package_id')

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
    cart_products = OfferManager.get_offer(ids)
    package_prices = list(map(map_function, cart_products))
    print(package_prices)
    total = sum(package_prices)

    args = {'cart_products': cart_products, 'total': total}
    return render(request, 'buyingview/cart.html', args)


@login_required(login_url='user_login')
def cartView(request):
    cart = request.session.get('cart', None)

    if request.method == "POST":
        cart = {}
        del request.session["cart"]
        return redirect("buying_view")

    print(request.session.get("cart"))
    if not cart:
        request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    cart_products = OfferManager.get_offer(ids)
    # print(len(cart))
    # print(cart)
    # print(cart.keys())
    if cart is not None:
        if len(cart) > 1:
            cart_first_item = str(list(cart.keys())[0])
            cart_first_item_val = list(cart.values())[0]
            request.session['cart'] = {}
            request.session["cart"] = {cart_first_item: cart_first_item_val}
            ids = list(request.session.get('cart').keys())
            cart_products = OfferManager.get_offer(ids)
    # print(request.session.get("cart"))
    context = {
        'cart_products': cart_products,
    }

    return render(request, 'buyingview/cart.html', context)


@login_required(login_url='user_login')
def checkout(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    ids = list(request.session.get('cart').keys())
    cart_products = OfferManager.get_offer(ids)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        due_date = request.POST.get('due_date')
        user = request.user
        # seller work

        packages = OfferManager.get_offer(list(cart.keys()))

        for package in packages:
            checkout = Checkout(
                first_name=first_name,
                last_name=last_name,
                due_date=due_date,
                user=user,
                package=package,
                price=package.price,
                quantity=cart.get(str(package.id)),
                seller = package.offer.user
            )
            
            # checkout.order_status = ""
            
            checkout.save()
            request.session['cart'] = {}
            return redirect('BuyerOrders')

    args = {
        'cart_products': cart_products
    }
    return render(request, 'buyingview/checkout.html', args)


# buyer order page views
@login_required(login_url='user_login')
def get_buyer_orders_url(request):
    orders = Checkout.objects.filter(user=request.user).order_by('-id')
    args = {
        'orders': orders
    }
    return render(request, 'buyingview/buying_orders.html', args)


# category wise Page
@login_required(login_url='user_login')
def category_wise_offers(request, slug):
    cats = Category.objects.all()
    category = Category.objects.all()
    catwise_offers = Offer.objects.filter(category__slug=slug)
    all_offers = Offer.objects.all()
    # sub_cats = Subcategory.objects.all()

    args = {'catwise_offers': catwise_offers, 'category': category,
            "all_offers": all_offers, 'cats': cats}

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

            return redirect('buying_view')
    args = {
        'categories': categories,
        'delivery_time': delivery_time,
        'post_form': post_form
    }
    return render(request, 'buyingview/post_request.html', args)


def get_become_a_seller_page(request):
    return render(request, 'landingview/become_a_seller.html')


# Order Details Page & SSLCOMMERZ
@login_required(login_url='user_login')
def get_order_details_url(request, id, *args, **kwargs):
    order = Checkout.objects.get(pk=id)
    # print(order_details)
    print(order.user)

    if request.method == 'POST':
        settings = {
            'store_id': 'testbox', 'store_pass': 'qwerty', 'issandbox': True
        }

        user = request.user
        # order = Checkout.objects.get(pk=kwargs['id'])
        order = Checkout.objects.get(pk=id)
        print(order)
        first_name = order.first_name
        last_name = order.last_name
        quantity = order.quantity
        total = order.grand_total
        transaction_id = order.id

        # Checkout.objects.filter(pk=kwargs['id'])
        Checkout.objects.filter(pk=id)

        sslcommerz = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = total
        post_body['currency'] = "BDT"
        post_body['tran_id'] = transaction_id
        # post_body['tran_id'] = transaction_id
        post_body['success_url'] = "http://127.0.0.1:8000/success/"
        post_body['fail_url'] = "http://127.0.0.1:8000/failed/"
        post_body['cancel_url'] = "http://127.0.0.1:8000/cancel/"
        post_body['emi_option'] = 0
        post_body['cus_name'] = first_name
        post_body['cus_email'] = "test@test.com"
        post_body['cus_add1'] = "customer address"
        post_body['cus_phone'] = "01700000000"
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = quantity
        post_body['product_name'] = order.package
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"
        print(post_body)
        response = sslcommerz.createSession(post_body)
        print(response)
        return redirect(response['GatewayPageURL'])
    args = {
        'order': order
    }

    return render(request, 'buyingview/order_details.html', args)


@csrf_exempt
def successView(request):
    if request.POST.get('status') == "VALID":
        tran_id = request.POST['tran_id']
        order = Checkout.objects.filter(id=tran_id)
        if order.exists():
            order.update(paid = True)
        
    return render(request, "responseview/success.html")


@csrf_exempt
def failedView(request):
    return render(request, "responseview/failed.html")


@csrf_exempt
def cancelledView(request):
    return render(request, "responseview/cancel.html")


def extendedUserView(request):
    form = ExtendedUserForm()
    user_session = request.session.get("user", None)

    if user_session is not None:
        if request.method == "POST":
            email = request.POST.get("email")
            contact_no = request.POST.get("contact_no")
            profile_picture = request.FILES.get("profile_picture")
            country_id = request.POST.get("country")
            city_id = request.POST.get("city")
            # print(request.user, email, contact_no, profile_picture, country_id, city_id)
            try:
                country = Country.objects.get(id=country_id)
                city = City.objects.get(id=city_id)
            except:
                return redirect("extended-user")
            else:
                SellerAccount.objects.create(user=request.user, email=email,
                                             contact_no=contact_no, profile_picture=profile_picture,
                                             country=country, city=city)
                return redirect('buying_view')
    else:
        return redirect("user_registration")

    args = {
        'form': form,
    }
    return render(request, "wasekPart/extendedForm.html", args)


@login_required(login_url='user_login')
def sellerSubmitView(request, pk):
    print(pk)
    if request.method == "POST":
        file_field = request.FILES.get("file_field")
        try:
            checkout = Checkout.objects.get(id=pk)
            print(f"{checkout=}")
            print(file_field)
        except:
            return redirect("manage-order")
        else:
            SellerSubmit.objects.create(
                checkout=checkout, file_field=file_field)

            checkout.order_status = "DELIVERED"
            checkout.save()
            return redirect("manage-order")

    args = {
        "checkout_id": pk,
    }
    return render(request, "wasekPart/sellerSubmit.html", args)


# Level up sellers (FOR TESTING)

def level_up_seller(request):

    offs = Offer.objects.all()

    args = {
        'offs': offs
    }

    return render(request, 'testpart/test.html', args)


def level_up_function(request, id):
    count_clicks = Offer.objects.filter(id=id).first()
    info = count_clicks.user.extendeduser.level

    lvl = Checkout.objects.filter(seller=request.user).first()

    # if count_clicks > 10:
    #     level  = "Hello"
    #     lvl.save()

    # else:
    #     level = "New Freelancer"

    print(count_clicks)

    args = {
        # 'level': level,
        'info': info,
        # 'lvl': lvl
    }

    return render(request, 'testpart/test_details.html', args)


# Rating Sellers


# Top Offers


## Footer Part ---------- >>>>>

def aboutusView(request):
    return render(request, "azimpart/aboutus.html")

def privacypolicyView(request):
    return render(request, "azimpart/privacy-policy.html")


def helpSupportView(request):
    return render(request, "azimpart/help-support.html")


def trustSafetyView(request):
    return render(request, "azimpart/trust-safety.html")

def termOfservicesView(request):
    return render(request, "azimpart/term-services.html")


## Footer Aprt ENd ------->>>


def create_offer_random_slug(str_len):
    rand_slug = ''.join(random.choices(string.ascii_uppercase + string.digits, k = str_len))
    offer = Offer.objects.filter(slug=rand_slug)
    if offer.exists():
        create_offer_random_slug(str_len)
    return rand_slug


@login_required(login_url='user_login')
def createOfferView(request):
    categories = Category.objects.all()
    services = Services.objects.all()
    deliveries = DeliveryTime.objects.all()
    revisions = Revision.objects.all()
    num_of_pages = NumberOfPage.objects.all()

    if request.method == "POST":
        print(request.POST.get("offer_title"))
        print(request.POST.get("seo_title"))
        print(request.POST.get("category"))
        print(request.POST.get("service"))
        # print(request.POST.getlist("tag"))
        # print(request.POST.get("basic_title"))
        # print(request.POST.get("standard_title"))
        # print(request.POST.get("premium_title"))
        print(request.POST.get("basic_shortDesc"))
        print(request.POST.get("standard_shortDesc"))
        print(request.POST.get("premium_shortDesc"))
        print(request.POST.get("delivery_time_basic"))
        print(request.POST.get("delivery_time_standard"))
        print(request.POST.get("delivery_time_premium"))
        print(request.POST.get("num_pages_basic"))
        print(request.POST.get("num_pages_standard"))
        print(request.POST.get("num_pages_premium"))
        print(request.POST.get("is_responsive_basic"))
        print(request.POST.get("is_responsive_standard"))
        print(request.POST.get("is_responsive_premimum"))
        print(request.POST.get("revision_basic"))
        print(request.POST.get("revision_standard"))
        print(request.POST.get("revision_premimum"))
        print(request.POST.get("price_basic"))
        print(request.POST.get("price_standard"))
        print(request.POST.get("price_premium"))
        print(request.POST.get("content"))
        print(request.FILES.get("offer_main_image"))
        print(request.FILES.getlist("uploaded_photo"))
        print(request.FILES.get("uploaded_video"))
        print(request.FILES.get("document"))

        # Data section
        slug = create_offer_random_slug(20)
        offer_title = request.POST.get("offer_title")
        seo_title = request.POST.get("seo_title")
        category = request.POST.get("category")
        service = request.POST.get("service")
        # basic_title = request.POST.get("basic_title")
        # standard_title = request.POST.get("standard_title")
        # premium_title = request.POST.get("premium_title")
        basic_shortDesc = request.POST.get("basic_shortDesc")
        standard_shortDesc = request.POST.get("standard_shortDesc")
        premium_shortDesc = request.POST.get("premium_shortDesc")
        delivery_time_basic = request.POST.get("delivery_time_basic")
        delivery_time_standard = request.POST.get("delivery_time_standard")
        delivery_time_premium = request.POST.get("delivery_time_premium")
        num_pages_basic = request.POST.get("num_pages_basic")
        num_pages_standard = request.POST.get("num_pages_standard")
        num_pages_premium = request.POST.get("num_pages_premium")
        is_responsive_basic = request.POST.get("is_responsive_basic")
        is_responsive_standard = request.POST.get("is_responsive_standard")
        is_responsive_premimum = request.POST.get("is_responsive_premimum")
        revision_basic = request.POST.get("revision_basic")
        revision_standard = request.POST.get("revision_standard")
        revision_premimum = request.POST.get("revision_premimum")
        price_basic = request.POST.get("price_basic")
        price_standard = request.POST.get("price_standard")
        price_premium = request.POST.get("price_premium")
        content = request.POST.get("content")
        main_image = request.FILES.get("offer_main_image")
        uploaded_photo = request.FILES.getlist("uploaded_photo")
        uploaded_video = request.FILES.get("uploaded_video")
        document = request.FILES.get("document")

        service = Services.objects.get(title=service)
        category = Category.objects.get(title=category)
        offer = Offer(slug=slug, user=request.user, offer_title=offer_title, seo_title=seo_title, 
                    image=main_image, offer_video=uploaded_video, document=document, 
                    service=service, category=category, description=content)
        if basic_shortDesc is not None:
            dt_basic = DeliveryTime.objects.get(title=delivery_time_basic)
            re_basic = Revision.objects.get(title=revision_basic)
            num_page_basic = NumberOfPage.objects.get(title=num_pages_basic)

            if is_responsive_basic == "on":
                is_responsive_basic = True
            else:
                is_responsive_basic = False
            package = Package(title="Basic", delivery_time=dt_basic, package_desc=basic_shortDesc, 
                            revision_basic=re_basic, num_of_pages_for_basic=num_page_basic, is_responsive_basic=is_responsive_basic,
                            )
            offer.save()
            for item in uploaded_photo:
                image_obj = ExtraImage(image=item)
                image_obj.save()
                offer.extra_images.add(image_obj.id)
            package.save()
            OfferManager.objects.create(offer=offer, package=package, price=price_basic)

    args = {
        "categories": categories,
        "services": services,
        "deliveries": deliveries,
        "revisions": revisions,
        "num_of_pages": num_of_pages,
    }
    return render(request, "sellingview/create_offer.html", args)


def edit_offer(request):
    return render(request, 'azimpart/edit_offer.html')



def seller_order_details(request, id):
    order = Checkout.objects.get(pk=id)
    today_date = date.today()
    duration = str(order.due_date - today_date).split(",")[0]

    print(duration)
    print(type(duration))
    
    args = {
        'order': order,
        "duration": duration,
    }
    return render(request, 'sellingview/seller_order_details.html', args)


def buyerGigFormView(request, pk):
    try:
        order = Checkout.objects.get(id=pk)
        # print(f"{order=}")
        seller = order.seller
        # print(seller)
        seller_submit = SellerSubmit.objects.get(checkout=order)
        print(seller_submit.id)
    except:
        messages.error(request, "Error while submitting!")
    else:
        if request.method == "POST":
            order_status = request.POST.get("order_status")
            l = Checkout.objects.filter(is_complete=True).filter(
                 seller=request.user).count()
            print(l)
            cancel_amount = Checkout.objects.filter(is_cancel=True).filter(
                seller=request.user
            ).count()
            
            if order_status == "complete" or l > 15:
                order.order_status = "COMPLETED"
                order.is_complete = True
                order.seller.selleraccount.level = 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashboard")
            
            elif order_status == "complete" or l > 25:
                order.order_status = "COMPLETED"
                order.is_complete = True
                order.seller.selleraccount.level += 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashboard")
            
            elif order_status == "complete" or l > 35:
                order.order_status = "COMPLETED"
                order.order_status = True
                order.seller.selleraccount.level += 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashboard")
            
            elif order_status == "complete" or l > 50:
                order.order_status = "COMPLETED"
                order.order_status = True
                order.seller.selleraccount.level += 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashboard")
                
            # Leveling Down ALgorithm
            
            elif order_status == "cancel" or cancel_amount > 5:
                order.order_status = "CANCELLED"
                order.is_cancel = True
                order.seller.selleraccount.level -= 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashboard")
            
            elif order_status == "cancel" or cancel_amount > 8:
                order.order_status == "CANCELLED"
                order.is_cancel = True
                order.seller.selleraccount.level -= 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashbaord")
            
            elif order_status == "cancel" or cancel_amount > 15:
                order.order_status == "CANCELLED"
                order.is_cancel = True
                order.seller.selleraccount.level -= 1
                order.seller.selleraccount.save()
                order.save()
                return redirect("buyer-dashboard")
            
            elif order_status == "review":
                order.order_status = "ON REVIEW"
                order.on_review = True
                order.save()
                return redirect("buyer-dashboard")
            else:
                messages.error(request, "Error while submitting!")

    args = {
        "seller_submit": seller_submit,
        "order": order
    }
    return render(request, "wasekPart/buyer_gigForm.html", args)


def buyerDashboardFormView(request):
    orders = Checkout.objects.filter(
        user=request.user, order_status="DELIVERED", is_complete=False).order_by("-id")

    args = {
        "orders": orders,
    }

    return render(request, "wasekPart/buyer_dashboard.html", args)

# Download Function
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(
                fh.read(), content_type="application/file_field")
            response["Content-Disposition"] = "inline;filename=" + \
                os.path.basename(file_path)
            return response
    raise Http404

def searchPageView(request):
    query = request.GET.get("search")

    args = {

    }
    return render(request, "buyingview/search-box-Result.html", args)

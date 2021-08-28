from django.shortcuts import render

# Create your views here.


def get_adminpanel_url(request):
    return render(request, 'admin_panel.html')


def uploadedOfferView(request):
    return render(request, "uploaded_offer.html")

def allUsersView(request):
    return render(request, "all_users.html")

def allOrdersView(request):
    return render(request, "all_order.html")

def adminLoginView(request):
    return render(request, "admin_login.html")
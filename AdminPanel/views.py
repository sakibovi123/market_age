from django.shortcuts import render

# Create your views here.


def get_adminpanel_url(request):
    return render(request, 'admin_panel.html')
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class GigManagerInline(admin.TabularInline):
    model = GigManager

class GigAdmin(admin.ModelAdmin):
    inlines = [
        GigManagerInline
    ]


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Package)
admin.site.register(ExtendedUser)
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Tag)
admin.site.register(DeliveryTime)
admin.site.register(Gig, GigAdmin)
admin.site.register(Currency)
admin.site.register(DummyUser)
admin.site.register(LandingSlider)
admin.site.register(Checkout)
admin.site.register(PromoCode)
admin.site.register(BuyerPostRequest)
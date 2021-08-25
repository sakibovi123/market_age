from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class RoleModel(models.Model):
    role_title = models.CharField(max_length=120)

    def __str__(self):
        return self.role_title


class LandingSlider(models.Model):
    slider_img = models.ImageField(upload_to="images/")

    def __str__(self):

        return str(self.id)

class SecondarySlider(models.Model):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.id)


class Country(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title


class City(models.Model):
    city_name = models.CharField(max_length=120)

    def __str__(self):
        return self.city_name


class ExtendedUser(models.Model):
    levels_fields = (
        ("NEW SELLER", "NEW SELLER"),
        ("LEVEL1", "LEVEL1"),
        ("LEVEL 2", "LEVEL 2"),
        ("LEVEL 3", "LEVEL 3"),
        ("MARKETAGE PRO", "MARKETAGE PRO")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, unique=True)
    contact_no = models.CharField(max_length=15, null=True)
    profile_picture = models.ImageField(upload_to="images/", null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length = 120, null=True, blank=True, choices=levels_fields, default="NEW SELLER")

    def __str__(self):
        return str(self.user)


class DummyUser(models.Model):
    user = models.CharField(max_length=120, default=None)

    def __str__(self):
        return self.user


class Services(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.sub_title


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    icon = models.FileField(upload_to="images/", validators=[
                            FileExtensionValidator(['svg', 'png', 'jpg'])], null=True)

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    slug = models.SlugField(unique=True)
    sub_title = models.CharField(max_length=120)
    sub_img = models.ImageField(upload_to="images/", null=True, blank=True)
    parent_market = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    # is_iterested = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title

class CategoryInterestedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_interested = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.user)




class Tag(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class DeliveryTime(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Package(models.Model):
    title = models.CharField(max_length=120)
    delivery_time = models.ForeignKey(
        DeliveryTime, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class ExtraImage(models.Model):
    image = models.ImageField(upload_to="images/", null=True, unique=True)

    def __str__(self):
        return str(self.image)


class Offer(models.Model):
    Offer_STATUS = (
        ("ACTIVE", "ACTIVE"),
        ("PENDING APPROVAL", "PENDING APPROVAL"),
        ("REQUIRED MODIFICATION", "REQUIRED MODIFICATION"),
        ("DENIED", "DENIED"),
        ("PAUSED", "PAUSED"),
    )

    slug = models.SlugField(unique=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    offer_title = models.CharField(max_length=240)
    image = models.ImageField(upload_to='images/')
    extra_images = models.ManyToManyField(ExtraImage)
    offer_video = models.FileField(upload_to="images/")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    packages = models.ManyToManyField(Package, through='OfferManager')
    description = models.TextField()
    # offer_rating = models.FloatField(default=0)
    is_popular = models.BooleanField(default=False, null=True)
    pop_web = models.BooleanField(default=False, null=True, blank=True)
    is_pro = models.BooleanField(default=False, null=True)
    short_desc = models.TextField(null=True)
    click = models.PositiveIntegerField(null=True, blank=True, default=0)
    impressions = models.PositiveIntegerField(default=0, null=True, blank=True)
    order_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    cancellation = models.PositiveIntegerField(default=0, null=True, blank=True)
    offer_status = models.CharField(max_length=200, null=True, choices=Offer_STATUS, default="ACTIVE")
    # is_complete = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.offer_title



class OfferFavoriteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    is_Favorite = models.BooleanField(default=False)




class OfferManager(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.offer)

    @staticmethod
    def get_price(self):
        return self.price

    @staticmethod
    def get_offer(ids):
        return OfferManager.objects.filter(id__in=ids)


class Currency(models.Model):
    currency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.currency_name


class Rating(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class ReviewSeller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    rate_seller = models.ForeignKey(
        Rating, on_delete=models.CASCADE, null=True)


class Checkout(models.Model):
    ORDER_CHOICES = (
        ("ACTIVE", "ACTIVE"),
        ("LATE", "LATE"),
        ("DELIVERED", "DELIVERED"),
        ("CANCELLED", "CANCELLED"),
        ("ON REVIEW", "ON REVIEW")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='seller')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    package = models.ForeignKey(OfferManager, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    grand_total = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00, null=True)
    paid = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    order_status = models.CharField(max_length=200, choices=ORDER_CHOICES, default="ACTIVE")
    is_complete = models.BooleanField(default=False, null=True)
    is_cancel = models.BooleanField(default=False, null=True)
    on_review = models.BooleanField(default=False, null=True)    
    
    def save(self, *args, **kwargs):
        self.total = self.price*self.quantity
        service_fee = self.total * 25 / 100
        self.grand_total = self.total + service_fee
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_total(total):
        return Checkout.objects.filter(total=total)

    @staticmethod
    def get_all_orders(self):
        return Checkout.objects.all()

    @staticmethod
    def placeOrder(self):
        return self.save()

    @staticmethod
    def get_orders_by_users(user):
        return Checkout.objects.filter(user=user['id'])


class SellerSubmit(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, related_name="checkout")
    file_field = models.FileField(upload_to="files/", null=True)
    submit_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    


class PromoCode(models.Model):
    promo_title = models.CharField(max_length=120)
    code = models.CharField(max_length=90)
    discount_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.promo_title


class BuyerPostRequest(models.Model):
    postrequest_title = models.CharField(max_length=220)
    description = models.TextField(null=True)
    attachment = models.FileField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deliver_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE)
    budget = models.IntegerField()

    def __str__(self):
        return self.postrequest_title

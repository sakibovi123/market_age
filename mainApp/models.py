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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="images/", null=True)
    rating_text = models.CharField(max_length=1000, null=True)
    level = models.IntegerField(default=None, null=True)
    rating = models.FloatField(default=0.0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

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
    icon = models.FileField(upload_to="images/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg', 'png'])], null=True)


    def __str__(self):
        return self.title


class Subcategory(models.Model):
    slug = models.SlugField(unique=True)
    sub_title = models.CharField(max_length=120)
    sub_img = models.ImageField(upload_to="images/", null=True, blank=True)
    parent_market = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

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
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title


class Gig(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    gig_title = models.CharField(max_length=240)
    image = models.ImageField(upload_to='images/')
    extra_images = models.ImageField(upload_to="images/")
    gig_video = models.FileField(upload_to="images/")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    packages = models.ManyToManyField(Package, through='GigManager')
    description = models.TextField()
    gig_rating = models.FloatField(default=0)
    is_popular = models.BooleanField(default=False, null=True)
    pop_web = models.BooleanField(default=False, null=True, blank=True)
    is_pro = models.BooleanField(default=False, null=True)
    short_desc = models.TextField(null=True)
    click = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.gig_title


class GigManager(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return str(self.package)
    
    
    
    @staticmethod
    def get_price(self):
        return self.price



    @staticmethod
    def get_gig(ids):
        return GigManager.objects.filter(id__in=ids)




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
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True)
    rate_seller = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    package = models.ForeignKey(GigManager, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)



    def save(self, *args, **kwargs):
        self.total = self.price*self.quantity
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
    def get_orders_by_users(self, user):
        return Checkout.objects.filter(user=user['id'])




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
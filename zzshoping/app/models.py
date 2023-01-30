from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Telangana','Telangana'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Chandigarh','Chandigarh'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Ladakh','Ladakh'),
    ('Lakshadweep','Lakshadweep'),
    ('Puducherry','Puducherry')
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return str(self.id)
CATEGORY_CHOICES=(
    ('TW','top wears'),
    ('BW','bottom wears'),
    ('L','laptops'),
    ('M','mobiles'),
)
class Product(models.Model):
    title=models.CharField(max_length=200)
    brand=models.CharField(max_length=20)
    description=models.TextField()
    discounted_price=models.FloatField()
    selling_price=models.FloatField()
    product_image=models.ImageField(upload_to='productimg')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
STATUS_CHOICES=(
    ('Cancel','Cancel'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    )
class Order_placed(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    product=models.ForeignKey(Product,models.CASCADE)
    customer=models.ForeignKey(Customer,models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=60)
    
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse

class Courier(models.Model):
	STATUS = (
        ('NEW','NEW'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
	user   = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='user', null=True)
	name = models.CharField(max_length=255)
	service = models.CharField(max_length=255)
	tracking_id = models.CharField(max_length=255, null=True)
	phone = models.CharField(max_length=255,null=True)
	reciever_name = models.CharField(max_length=250, blank=True, null=True)
	reciever_phone = models.CharField(max_length=200,blank=True, null=True)
	reciever_address = models.CharField(max_length=500, blank=True, null=True)
	reciever_email = models.EmailField(blank=True,null=True)
	agent = models.CharField(max_length=200,blank=True, null=True)
	product_name = models.CharField(max_length=300, blank=True,null=True)
	courier = models.CharField(max_length=300, blank=True,null=True)
	mode = models.CharField(max_length=200, blank=True, null=True)
	quantity = models.IntegerField(blank=True,null=True)
	carrier = models.CharField(max_length=250, blank=True, null=True)
	carrier_reference_no = models.IntegerField(blank=True, null=True)
	payment_mode = models.CharField(max_length=200, blank=True, null=True)
	weight = models.CharField(max_length=200, blank=True, null=True)
	departure_time = models.DateTimeField(blank=True,  null=True)
	origin = models.CharField(max_length=200, blank=True, null=True)
	destination = models.CharField(max_length=300, blank=True, null=True)
	status = models.CharField(max_length=20, choices=STATUS, default='New',null=True)
	expected_delivery_date = models.DateTimeField(blank=True, null=True)
	comments = models.CharField(max_length=200,blank=True, null=True)
	list_date = models.DateTimeField(default=timezone.datetime.now, blank = True, null=True)

	def get_absolute_url(self):
		return reverse("couriermanage:listing",args=[self.name])


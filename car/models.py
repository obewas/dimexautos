from django.db import models

# Create your models here.
class Car(models.Model):
	carMake = models.CharField(max_length=250)
	carModel = models.CharField(max_length=250)
	carReg = models.CharField(max_length=250)
	carYear = models.CharField(max_length=250)
	engNumber = models.CharField(max_length=250)
	chassNumber = models.CharField(max_length=250)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	image1 = models.ImageField(upload_to='static/images', null=True, blank=True)
	image2 = models.ImageField(upload_to='static/images', null=True, blank=True)
	image3 = models.ImageField(upload_to='static/images', null=True, blank=True)
	image4 = models.ImageField(upload_to='static/images', null=True, blank=True)
	image5 = models.ImageField(upload_to='static/images', null=True, blank=True)

	def __str__(self):
		name = self.carMake + ' ' + self.carModel + ' ' + self.carReg
		return name

class Cost(models.Model):
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	cif_cost = models.IntegerField()
	customs_duty = models.IntegerField()
	delivery_order = models.IntegerField()
	cfs_charges = models.IntegerField()
	kebs = models.IntegerField()
	ntsa = models.IntegerField()
	insurance = models.IntegerField()
	agency = models.IntegerField()
	transport = models.IntegerField()

	def total_cost(self):
		cost = self.cif_cost + self.customs_duty + self.delivery_order + self.cfs_charges + self.kebs + self.ntsa + self.insurance + self.agency + self.transport
		
		print(cost)
		return cost

class Profit(models.Model):
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	selling_price = models.IntegerField()
	car_cost = models.ForeignKey(Cost, on_delete=models.CASCADE)

	def total_profit(self):
		profit = self.selling_price - self.car_cost.total_cost

		return profit




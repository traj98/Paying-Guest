from django.db import models

Property_type = (
	( ("R") ,"Residential "),
	(("E") ,"Educational "),
	(("B") ,"Business "),
	(("I") ,"Industrial "),
	)

Furnished_type = (
	(("F") ,"Fully Furnished"),
	(("P") ,"Partly Furnished"),
	(("N") ,"Not Furnished"),
	(("A") ,"Any"),


	)

class Property(models.Model):
	name= models.CharField(max_length=50)
	price=models.PositiveIntegerField()
	size=models.DecimalField(max_digits=5, decimal_places=2)
	rooms=models.PositiveIntegerField()
	category=models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
	bath_rooms=models.PositiveIntegerField()
	building_type=models.CharField(choices=Property_type,max_length=20)
	parking=models.CharField(max_length=50)
	Furnished=models.CharField(choices=Furnished_type, max_length=20)
	detail=models.CharField(max_length=100)
	address=models.CharField(max_length=50)
	image=models.ImageField(upload_to='media/upload/',null=True)

	def __str__(self):
		return self.name


	class Meta:

		verbose_name='Property'
		verbose_name_plural='Properties'




class Category(models.Model):
	category_name=models.CharField(max_length=30)


	def __str__(self):
		return self.category_name



	class Meta:

		verbose_name='Category'
		verbose_name_plural='Categories'
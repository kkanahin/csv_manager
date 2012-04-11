from django.db import models

class Category(models.Model):
    name_category=models.CharField(max_length=15)
    
    
class CSVData(models.Model):
    name_file=models.CharField(max_length=30)
    upload_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category)

class Func_var(models.Model):
    data=models.ForeignKey(CSVData)
    variable=models.FloatField()

class Function(models.Model):
    variable=models.ForeignKey(Func_var)
    function=models.FloatField()


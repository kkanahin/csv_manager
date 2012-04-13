from django.db import models

class Category(models.Model):
    name_category=models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name_category
    
    
class CSVData(models.Model):
    name_file=models.CharField(max_length=30)
    upload_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.name_file


class Func_var(models.Model):
    data=models.ForeignKey(CSVData)
    variable=models.FloatField()
    
    def __unicode__(self):
        return str(self.variable)


class Function(models.Model):
    variable=models.ForeignKey(Func_var)
    function=models.FloatField()
    
    def variable_id(self):
        return self.variable.id
    
    def variable_data(self):
        return self.variable.data

    def __unicode__(self):
        return str(self.function)


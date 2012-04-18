from django.db import models

class Category(models.Model):
    name_category=models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name_category
    
def make_upload_file(instance,filename):
    return u"%s" % (filename)

class CSVData(models.Model):
    name_file=models.FileField(upload_to=make_upload_file)
    upload_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category)
    
    def __unicode__(self):
        return str(self.name_file)


class Func_var(models.Model):
    data=models.ForeignKey(CSVData)
    variable=models.FloatField()
    
    def __unicode__(self):
        return str(self.variable)


class Function(models.Model):
    variable=models.ForeignKey(Func_var)
    function=models.FloatField()
    
#    def variable_id(self):
#        return self.variable.id
    
#    def variable_data(self):
#        return self.variable.data

    def __unicode__(self):
        return str(self.function)


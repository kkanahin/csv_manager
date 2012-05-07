from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name_category=models.CharField(max_length=15,unique=True)
    category_slug=models.SlugField(editable=False)
    
    def save(self,**kwargs):
        self.category_slug=slugify(self.name_category)
        super(Category,self).save()
    
    def __unicode__(self):
        return self.name_category
    
def make_upload_file(instance,filename):
    return u"%s" % (filename)

UPLOAD_STATUS_CHOICES=((u'is_uploading',u'is uploading'),
                       (u'uploaded',u'uploaded')
                      )

class CSVData(models.Model):
    category=models.ForeignKey(Category,help_text='Select category')
    name_file=models.FileField(upload_to=make_upload_file,verbose_name='upload file')
    upload_date=models.DateTimeField(auto_now_add=True)
    last_change=models.DateTimeField(auto_now=True)
    upload_status=models.CharField(max_length=13,editable=False,\
                                   choices=UPLOAD_STATUS_CHOICES)
    
    def __unicode__(self):
        return str(self.name_file)
        
class File_head(models.Model):
    data=models.ForeignKey(CSVData)
    column_number=models.IntegerField()
    column_head_str=models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.column_head_str
class Func_var(models.Model):
    data=models.ForeignKey(CSVData)
    variable=models.FloatField()
    
    def __unicode__(self):
        return str(self.variable)


class Function(models.Model):
    variable=models.ForeignKey(Func_var)
    function=models.FloatField()

    def __unicode__(self):
        return str(self.function)

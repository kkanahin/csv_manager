from django.db import models

class Categories(models.Model):
    name_category=models.CharField(max_length=15)
    
    
class Files(models.Model):
    name_file=models.CharField(max_length=30)
    upload_date=models.DateField()
    category=models.ForeignKey(Categories)

class Files_content(models.Model):
    file=models.ForeignKey(Files)
    file_content=models.TextField()


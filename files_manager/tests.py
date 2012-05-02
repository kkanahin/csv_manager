"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from files_manager.models import CSVData,Function,Func_var
from django.test import TestCase,Client
from django.contrib.auth.models import User
from files_manager import forms
from django.core.files import File
from django.core.urlresolvers import reverse
import os
from django.conf import settings

class Files_managerTest(TestCase):
    fixtures=['test_data.json']
    path=os.path.realpath(os.path.dirname('__file__'))
    test_files_path=os.path.join(path,'files_manager','test_files')
    
    def setUp(self):
        User.objects.create_user('test_user','test_user@example.com','pass')

    def test_default_page(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code,200)

    def test_upload_page(self):
        c=Client()
        response=c.get('/upload/')
        self.assertRedirects(response,'accounts/login/?next=/upload/')
        c.login(username='test_user',password='pass')
        response=c.get('/upload/')
        self.assertEqual(response.status_code,200)
    
    def test_upload_file(self):
        c=Client()
        c.login(username='test_user',password='pass')
        upload_file_path=(os.path.join(self.test_files_path,'1.csv_test'))
        upload_file=open(upload_file_path,'rb')
        response=c.post('/upload/',{'category':'1','upload_file':upload_file})
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response,'form',field='upload_file',\
                             errors=u'The Head of this file is not right!')
        upload_file.close()
        upload_file_path=(os.path.join(self.test_files_path,'2.csv_test'))
        upload_file=open(upload_file_path,'rb')
        response=c.post('/upload/',{'category':'1','upload_file':upload_file})
        self.assertRedirects(response,reverse('file_view',args=[2]))
        upload_file.close()
        num_variables=Func_var.objects.filter(data=2).count()
        self.assertEqual(num_variables,2)
        num_functions=Function.objects.filter(variable__data=2).count()
        self.assertEqual(num_functions,3)
        remove_file=CSVData.objects.get(id=2).name_file.url
        os.remove(os.path.join(settings.MEDIA_ROOT,remove_file))
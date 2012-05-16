#-*-coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from files_manager.models import CSVData,Function,Func_var,File_head,Category
from django.test import TestCase,Client
from django.contrib.auth.models import User
from files_manager import forms
from django.core.files import File
from django.core.urlresolvers import reverse
import os
from django.conf import settings


class Files_managerTest(TestCase):
    path=os.path.realpath(os.path.dirname('__file__'))
    test_files_path=os.path.join(path,'files_manager','test_files')
    
    def setUp(self):
        User.objects.create_user('test_user','test_user@example.com','pass')
        Category.objects.create(name_category='category 1')
        Category.objects.create(name_category='category 2')
        c=Client()
        c.login(username='test_user',password='pass')
        upload_file_path=(os.path.join(self.test_files_path,'2.csv_test'))
        upload_file=open(upload_file_path,'rb')
        response=c.post('/upload/',{'category':'1','name_file':upload_file})
        c.logout()
        remove_file=CSVData.objects.get(id=1).name_file.url
        os.remove(os.path.join(settings.MEDIA_ROOT,remove_file))

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
        response=c.post('/upload/',{'category':'1','name_file':upload_file})
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response,'form',field='name_file',\
                             errors=u'The Head of this file is not right!')

        upload_file_path=(os.path.join(self.test_files_path,'3.csv_test'))
        upload_file=open(upload_file_path,'rb')
        response=c.post('/upload/',{'category':'1','name_file':upload_file})
        self.assertFormError(response,'form',field='name_file',\
                             errors=u'This file is not csv!')
        upload_file.close()

        upload_file_path=(os.path.join(self.test_files_path,'2.csv_test'))
        upload_file=open(upload_file_path,'rb')
        response=c.post('/upload/',{'category':'1','name_file':upload_file})
        self.assertRedirects(response,reverse('file_view',args=[2]))
        upload_file.close()
        num_variables=Func_var.objects.filter(data=2).count()
        self.assertEqual(num_variables,2)
        num_functions=Function.objects.filter(variable__data=2).count()
        self.assertEqual(num_functions,3)
        remove_file=CSVData.objects.get(id=2).name_file.url
        os.remove(os.path.join(settings.MEDIA_ROOT,remove_file))

    def test_main_page(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'<a href="/category/category-1">category 1</a><br>',\
                            status_code=200)
        self.assertContains(response,'<a href="/accounts/login/">Вход</a>',\
                            status_code=200)
        self.assertNotContains(response,'<a href="/file_view/1" > Открыть</a>')
        c.login(username='test_user',password='pass')
        response=c.get('/')
        self.assertContains(response,'<a href="/file_view/1" > Открыть</a>',\
                            status_code=200)
    
    def test_file_view(self):
        c=Client()
        response=c.get('/file_view/1/')
        self.assertRedirects(response,'accounts/login/?next=/file_view/1/')
        c.login(username='test_user',password='pass')
        response=c.get('/file_view/1/')
        self.assertContains(response,'<th>col1</th>',status_code=200)
        self.assertContains(response,'categories: [2.3, 4.8]',status_code=200)
        self.assertContains(response,'data:[4.0, 6.0]',status_code=200)
    
    def test_range_files_by_category(self):
        upload_file_path=(os.path.join(self.test_files_path,'2.csv_test'))
        upload_file=open(upload_file_path,'rb')
        c=Client()
        c.login(username='test_user',password='pass')
        response=c.post('/upload/',{'category':'2','upload_file':upload_file})
        response=c.get('/')
        self.assertContains(response,'<td>1</td>',status_code=200,html=True)
        self.assertContains(response,'<td>2</td>',status_code=200,html=True)
        response=c.get('/category/category-1')
        self.assertContains(response,'<td>1</td>',status_code=200,html=True)
        self.assertNotContains(response,'<td>2</td>',status_code=200,html=True)
        
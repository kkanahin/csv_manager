"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase,Client

class Files_managerTest(TestCase):
    fixtures=['test_data.json']
    
    def test_default_page(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code,200)
        
    def test_upload_page(self):
        c=Client()
        response=c.get('/upload/')
        self.assertRedirects(response,'accounts/login/?next=/upload/')
        c.login(username='test_admin',password='admin')
        response=c.get('/upload/')
        self.assertEqual(response.status_code,200)
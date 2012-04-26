"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase,Client

class TestMainPage(TestCase):
    def TestDefaultPage(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code,300)
        print "hello"

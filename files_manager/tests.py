"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase,Client

<<<<<<< HEAD
class TestMainPage(TestCase):
    def TestDefaultPage(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code,300)
        print "hello"
=======

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class MyTest(TestCase):
    def test_default_page(self):
        c=Client()
        response=c.get('/')
        self.assertEqual(response.status_code,200)
        c.login(username='admin',password='02111985')
        response=c.get('/upload/')
        self.assertEqual(response.status_code,302)
>>>>>>> 19309855401042df7ae072e6e2bc7c8711f3050b

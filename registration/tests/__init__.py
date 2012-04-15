from django.test import TestCase

import registration

from registration.tests.backends import *
from registration.tests.forms import *
from registration.tests.models import *
from registration.tests.views import *


class RegistrationVersionInfoTests(TestCase):
    """
    Test django-registration's internal version-reporting
    infrastructure.
    
    """
    def setUp(self):
        self.version = registration.VERSION

    def tearDown(self):
        registration.VERSION = self.version
    
    def test_get_version(self):
        """
        Test the version-info reporting.
        
        """
        versions = [
            {'version': (0, 8, 0, 'final', 0),
             'expected': "0.8"},
            ]
        
        for version_dict in versions:
            registration.VERSION = version_dict['version']
            self.assertEqual(registration.get_version(), version_dict['expected'])

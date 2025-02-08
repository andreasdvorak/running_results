"""module for test cases"""

from django.test import TestCase
from .models import AgeGroup

class AgeGroupTestCase(TestCase):
    """Test case for age groups

    Args:
        TestCase (_type_): _description_
    """
    def setUp(self):
        AgeGroup.objects.create(age="150", age_group_m="M150", age_group_w="W150")

    def test_show_age_group(self):
        age_150 = AgeGroup.objects.get(age="150")
        self.assertEqual()

"""module for test cases"""

from django.test import TestCase
from .models import AgeGroup

class AgeGroupTestCase(TestCase):
    """Test case for age groups

    Args:
        TestCase (_type_): _description_
    """
    def setUp(self):
        AgeGroup.objects.create(age=50, age_group_m="M50", age_group_w="W50")

    def test_show_age_group(self):
        """Verify that the age group can be retrieved."""
        age_50 = AgeGroup.objects.get(age=50)
        self.assertEqual(age_50.age, 50)
        self.assertEqual(age_50.age_group_m, "M50")
        self.assertEqual(age_50.age_group_w, "W50")

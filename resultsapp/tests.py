from django.test import TestCase
from models import AgeGroup

class AgeGroupTestCase(TestCase):
    def setUp(self):
        AgeGroup.objects.create(age="150", age_group_m="M150", age_group_w="W150")

    def test_show_age_group(self):
        age_150 = AgeGroup.objects.get(age="150")
        self.assertEqual()
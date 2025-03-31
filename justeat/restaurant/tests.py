from django.test import TestCase
from django.urls import reverse
import re
# Create your tests here.

class PostcodeValidation(TestCase):
    postcodes = [
        'CT1 2EH', 'BS1 4DJ', 'L40TH', 'NE9 7TY',
        'SW1A 1AA', 'CF11 8AZ', 'M16 0RA', 'EH1 1RE',
        'BN1 1AE', 'CB74DL', 'LS2 7HY', 'G3 8AG',
        'PL4 0DW', 'B26 3QJ', 'DH4 5QZ', 'BT7 1NN'
    ]
    
    def test_api_response_valid_postcodes(self):
        for postcode in self.postcodes:
            url = reverse('restaurant_list', args=[postcode.replace(' ', '')])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'restaurant-list')

    def test_valid_postcode_format(self):
        pattern = r"^[A-Za-z0-9]+(?:[ ]?[A-Za-z0-9 ]+)*$"
        for postcode in self.postcodes:
            self.assertIsNotNone(
                re.fullmatch(pattern, postcode),
                f"Failed validation: {postcode}"
            )
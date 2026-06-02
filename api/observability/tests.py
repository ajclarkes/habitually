from django.test import TestCase

class HealthTestCase(TestCase):
    def test_health_is_ok(self):
        response = self.client.get('/obs/health/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})

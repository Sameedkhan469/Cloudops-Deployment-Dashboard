import unittest
from app import app


class TestCloudOpsDashboard(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CloudOps Deployment Dashboard", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_info_endpoint(self):
        response = self.client.get("/api/info")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["application"],
            "CloudOps Deployment Dashboard"
        )


if __name__ == "__main__":
    unittest.main()

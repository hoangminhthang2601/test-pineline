"""
Test API health check.
"""

from ailiver.main import app
from unittest import TestCase
from fastapi.testclient import TestClient
from fastapi import status


class TestHealthCheckAPI(TestCase):
    """Test health check api."""

    def setUp(self):
        self.client = TestClient(app)

    def test_health_check_successful(self):
        """Test health check api successful."""
        res = self.client.get("/health-check")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.content, b"OK")

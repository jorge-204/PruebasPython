import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_substract(self):
        url = f"{BASE_URL}/calc/substract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_square_root(self):
        url = f"{BASE_URL}/calc/square_root/25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_log(self):
        url = f"{BASE_URL}/calc/log/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_nonexistent_route(self):
        url = f"{BASE_URL}/nonexistent_route"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.NOT_FOUND, f"Expected 404 for {url}"
            )
        else:
            self.fail(f"Expected 404 for {url}, but received response with status {response.status}")

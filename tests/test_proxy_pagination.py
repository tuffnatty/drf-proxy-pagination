import json

from django.test import TestCase

from rest_framework import status

from tests.models import TestModel


class ProxyPaginationTests(TestCase):
    """
    Tests for drf-proxy-pagination
    """
    def setUp(self):
        for n in range(200):
            TestModel.objects.create(n=n)

    def test_without_pager_param(self):
        resp = self.client.get('/data/', HTTP_ACCEPT='application/json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp['Content-Type'], 'application/json')
        content = json.loads(resp.content)
        self.assertIn('next', content)
        self.assertIn('count', content)
        self.assertIn('page=', content['next'])
        self.assertNotIn('cursor=', content['next'])

    def test_with_pager_param(self):
        resp = self.client.get('/data/?pager=cursor', HTTP_ACCEPT='application/json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp['Content-Type'], 'application/json')
        self.assertNotIn('count', resp.content)
        content = json.loads(resp.content)
        self.assertIn('next', content)
        self.assertNotIn('page=', content['next'])
        self.assertIn('cursor=', content['next'])

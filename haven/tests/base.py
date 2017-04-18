import json
import unittest

from haven import create_app
from haven.lib.database import db


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['DEBUG'] = True
        self.app.config['TESTING'] = True
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()


class ViewTestCaseResponse(object):
    """Wraps a response object to easily extract and manipulate fields."""

    def __init__(self, response):
        self.data = json.loads(response.get_data() or '{}')
        self.status_code = response.status_code


class ViewTestCase(BaseTestCase):

    def setUp(self):
        super(ViewTestCase, self).setUp()
        self.client = self.app.test_client()

    def _get_headers(self, headers):
        """Get headers to send with the request."""
        default_headers = {}
        default_headers.update(headers)
        return default_headers

    def post(self, url, data=None, **kwargs):
        """Perform a post request."""
        res = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
            headers=self._get_headers(kwargs.pop('headers', {})),
            **kwargs
        )
        return ViewTestCaseResponse(res)

    def raw_get(self, url, **kwargs):
        """Perform a get request with no additional formatting."""
        res = self.client.get(
            url,
            headers=self._get_headers(kwargs.pop('headers', {})),
            **kwargs
        )
        return res

    def get(self, url, **kwargs):
        """Perform a get request."""
        res = self.client.get(
            url,
            headers=self._get_headers(kwargs.pop('headers', {})),
            **kwargs
        )
        return ViewTestCaseResponse(res)

    def delete(self, url, **kwargs):
        """Perform a delete request."""
        res = self.client.delete(
            url,
            headers=self._get_headers(kwargs.pop('headers', {})),
            **kwargs
        )
        return ViewTestCaseResponse(res)

    def patch(self, url, data=None, **kwargs):
        """Perform a patch request."""
        res = self.client.patch(
            url,
            data=json.dumps(data),
            content_type='application/json',
            headers=self._get_headers(kwargs.pop('headers', {})),
            **kwargs
        )
        return ViewTestCaseResponse(res)

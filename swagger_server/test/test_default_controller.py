# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.image import Image  # noqa: E501
from swagger_server.models.scores import Scores  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_score_image(self):
        """Test case for score_image

        Score an image
        """
        image = Image()
        response = self.client.open(
            '/v2/yolo',
            method='POST',
            data=json.dumps(image),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

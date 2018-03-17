import connexion
import six

from swagger_server.models.image import Image  # noqa: E501
from swagger_server.models.scores import Scores  # noqa: E501
from swagger_server.models.scored_class import ScoredClass
from swagger_server import util

import cv2
import base64
import numpy

def tfnet():
    from __main__ import options
    return options["tfnet"]

def score_image(image=None):  # noqa: E501
    """Score an image

     # noqa: E501

    :param image: 
    :type image: dict | bytes

    :rtype: Scores
    """
    if connexion.request.is_json:
        imageobj = Image.from_dict(connexion.request.get_json())
        image = base64.b64decode(imageobj.image)  # noqa: E501
        
    imgcv = cv2.imdecode(numpy.asarray(bytearray(image), dtype=numpy.uint8), cv2.IMREAD_COLOR)
    result = tfnet().return_predict(imgcv)
    print(repr(result))
    scores = [ScoredClass(voc=r['label'], score=float(r['confidence'])) for r in result]
    
    return scores

import connexion
import six

from swagger_server.models.image import Image  # noqa: E501
from swagger_server.models.scores import Scores  # noqa: E501
from swagger_server import util

import cv2

def score_image(image=None):  # noqa: E501
    """Score an image

     # noqa: E501

    :param image: 
    :type image: dict | bytes

    :rtype: Scores
    """
    if connexion.request.is_json:
        image = Image.from_dict(connexion.request.get_json())  # noqa: E501
    
    imgcv = cv2.imread("./sample_img/sample_dog.jpg")
    result = tfnet.return_predict(imgcv)
    
    return 'do some magic!'

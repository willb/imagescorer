# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.voc import VOC  # noqa: F401,E501
from swagger_server import util


class ScoredClass(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, voc: str=None, score: float=None):  # noqa: E501
        """ScoredClass - a model defined in Swagger

        :param voc: The voc of this ScoredClass.  # noqa: E501
        :type voc: str
        :param score: The score of this ScoredClass.  # noqa: E501
        :type score: float
        """
        self.swagger_types = {
            'voc': str,
            'score': float
        }

        self.attribute_map = {
            'voc': 'voc',
            'score': 'score'
        }

        self._voc = voc
        self._score = score

    @classmethod
    def from_dict(cls, dikt) -> 'ScoredClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScoredClass of this ScoredClass.  # noqa: E501
        :rtype: ScoredClass
        """
        return util.deserialize_model(dikt, cls)

    @property
    def voc(self) -> str:
        """Gets the voc of this ScoredClass.


        :return: The voc of this ScoredClass.
        :rtype: str
        """
        return self._voc

    @voc.setter
    def voc(self, voc: str):
        """Sets the voc of this ScoredClass.


        :param voc: The voc of this ScoredClass.
        :type voc: str
        """
        allowed_values = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]  # noqa: E501
        if voc not in allowed_values:
            raise ValueError(
                "Invalid value for `voc` ({0}), must be one of {1}"
                .format(voc, allowed_values)
            )

        self._voc = voc

    @property
    def score(self) -> float:
        """Gets the score of this ScoredClass.


        :return: The score of this ScoredClass.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this ScoredClass.


        :param score: The score of this ScoredClass.
        :type score: float
        """

        self._score = score
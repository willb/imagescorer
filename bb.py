#!/usr/bin/env python3

import sys
import cv2

import json
result = {}

img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
meta = json.loads(sys.stdin.read())

for d in meta:
    tl = (int(d["tl_x"]), int(d["tl_y"]))
    br = (int(d["br_x"]), int(d["br_y"]))
    cv2.rectangle(img, tl, br, color=(255,255,255), thickness=3)

cv2.imwrite("output.jpg", img)
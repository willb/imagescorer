#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from darkflow.net.build import TFNet

def main():
    options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}    
    
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'YOLO Image Scorer'})
    app.tfnet = TFNet(options)

    app.run(port=8080)


if __name__ == '__main__':
    main()

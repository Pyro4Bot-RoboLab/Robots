#!/usr/bin/env python
# -*- coding: utf-8 -*-
#____________developed by paco andres____________________

import threading
from nodeproxy import ClientNODERB
import time
import Pyro4
import cv2
import urllib
import numpy as np
from PIL import Image
import io
import socket
import struct
import time


class clientCamera(object):
    def __init__(self, camera):
        print "client"
        self.cam = camera
        self.cam_t = threading.Thread(target=self.execute_camera, args=())
        self.cam_t.setDaemon(True)
        self.cam_t.start()

    def execute_camera(self):
        print "Connecting to Server. Waiting for IP and PORT"
        ip, port = self.cam.image()
        print "Client: " + ip + ":" + str(port)
        client_socket = socket.socket()
        try:
            client_socket.connect((ip, port))
            try:
                connection = client_socket.makefile("make" + str(port))
                # Construct a stream to hold the image data and read the image
                # data from the connection
                image_stream = io.BytesIO()
                while True:
                    # Read the length of the image as a 32-bit unsigned int. If the
                    # length is zero, quit the loop
                    image_len = struct.unpack(
                        '<L', connection.read(struct.calcsize('<L')))[0]

                    if not image_len:
                        print "No image len"
                        break
                    image_stream.write(connection.read(image_len))
                    # Rewind the stream, open it as an image with PIL and do some
                    # processing on it
                    image_stream.seek(0)

                    # BytesIO
                    data = np.fromstring(
                        image_stream.getvalue(), dtype=np.uint8)
                    c = cv2.imdecode(data, 1)
                    # centro=[]
                    # centro,img=track(c)
                    cv2.imshow('learnbot1-' + str(port), c)
                    if cv2.waitKey(1) == 27:
                        exit(0)
            except Exception:
                print "Error al recibir"
            finally:
                connection.close()
        except Exception:
            print "Error al conectar a " + ip + ":" + str(port)
        finally:
            print("Exit")
            client_socket.close()


print("Ejecutando cliente de camara...")
bot = ClientNODERB("picambot")  # nombre del bot en la name no el fichero json
camera = clientCamera(bot.camera)

while True:
    time.sleep(0.05)

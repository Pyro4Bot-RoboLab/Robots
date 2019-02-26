#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________
from libs.class_client_robot import ClientRobot
from libs.class_client_camera import ClientCamera
import sys
import time


if __name__ == "__main__":
    try:
        print("Ejecutando cliente de camara...")

        ROBOT_NAME = "paco"

        if len(sys.argv) is 2:
            ROBOT_NAME = sys.argv[1]

        bot = ClientRobot(ROBOT_NAME)
        camera = ClientCamera(bot.picam)
        
        while True:
            time.sleep(0.05)

    except (KeyboardInterrupt, SystemExit):
        print("\nSaliendo.  print(cam.image()..")
        exit()

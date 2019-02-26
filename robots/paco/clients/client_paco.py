#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ____________developed by paco andres____________________
# _________collaboration with cristian vazquez____________

from libs.class_client_robot import ClientRobot
import time

def main():
    bot = ClientRobot("paco")
    for x in range(20):
        print(bot.base.get_base())
        time.sleep(0.01)


if __name__ == '__main__':
    main()

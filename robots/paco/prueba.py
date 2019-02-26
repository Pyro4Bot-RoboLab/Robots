import os
import sys
def get_PYRO4BOT_HOME():
    """ It turns back the environment path of the program Pyro4Bot """
    if "PYRO4BOT_HOME" not in os.environ:
        print("ERROR: PYRO4BOT_HOME not setted")
        print("please type export PYRO4BOT_HOME=<DIR> to set it up")
        sys.exit()
    else:
        return os.environ["PYRO4BOT_HOME"]


PYRO4BOT_HOME = get_PYRO4BOT_HOME()
print(PYRO4BOT_HOME)
sys.path.append(PYRO4BOT_HOME)
from node.libs.bluetooth import bt_RFCOMM as bt
import time
from node.libs import control
from node.libs import utils
from picamera import PiCamera
from io import BytesIO
import Pyro4
import socket
import struct
import threading

print(bt.GetFirstMAC())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lock().acquire()
# ____________developed by paco andres____________________
import time
from node.libs import control
import Pyro4
import sys


class basemotion(control.Control):
    """Movement of wheels through Arduino."""

    __REQUIRED = ["usbserial", "BASE"]

    def __init__(self):
        self.start_subscription("usbserial", "BASE")
        self.start_worker(self.worker)
        self.set__vel(mi=0, md=0)
        #print(self.__dict__)

    def worker(self):
        self.BASE=[0,0]
        while self.worker_run:
            self.BASE[0]=self.BASE[0]+1
            #print(self.BASE)
            time.sleep(self.frec)

    @Pyro4.expose
    @Pyro4.oneway
    @control.flask("actuator")
    def set__vel(self, mi=1, md=1):
        #self.BASE[11]=0
        # print "base " + str(mi) + "," + str(md)
        self.usbserial.command(comman="base " + str(mi) + "," + str(md))


    @Pyro4.expose
    @control.flask("sensor", 2)
    def get_base(self):
        return self.BASE

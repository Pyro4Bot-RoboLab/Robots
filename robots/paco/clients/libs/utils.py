"""Utils to PYRO4BOT."""

import Pyro4
import netifaces as ni
import sys
from termcolor import colored
import os
import socket


def get_all_ip_address(broadcast=False):
    """Return the list of IPs of all network interfaces.

    If broadcast = True, returns the list of broadcast IPs of all network
    interfaces.
    """
    address = []
    try:
        for x in ni.interfaces():
            add = ni.ifaddresses(x)
            try:
                for ips in add[ni.AF_INET]:
                    if broadcast:
                        address.append(ips["broadcast"])
                    else:
                        address.append(ips["addr"])
            except Exception:
                pass
    except Exception:
        print("ERROR: utils.get_all_ip_address()")
        exit()
        raise
    return address


def get_uri(name, ip, port):
    """Return the Pyro4 URI formed from name, ip and port."""
    return "PYRO:" + name + "@" + ip + ":" + str(port)




def get_pyro4proxy(uri, password):
    """Given a Pyro4 URI and a password, return the connection proxy."""
    proxy = Pyro4.Proxy(uri)
    proxy._pyroHmacKey = password.encode()
    return proxy

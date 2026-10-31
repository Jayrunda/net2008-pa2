#!/usr/bin/env python3

"""JAYDEN NDAYITEGEYE PA_2"""

import json
import sys
from pathlib import Path
import yaml
import xml.etree.ElementTree as ET

class InputError(Exception):
"""Raises when you put in an unreadable file for the script or if the input is missing"""

def version_tuple(version):
""" Functino to turn verison numbers with dots into a tuple of ints"""
	return tuple(int(part) for part in version.split("."))

class Device:
	"""The device class my script will parse from XML"""
	def __init__(self,id, role, os, owner, interfaces):
	

"""Device attributes and interface statuses."""
        self.device_id = device_id
        self.role = role
        self.os_version = os_version
        self.owner = owner
        self.interfaces = interfaces

	def down_interface_count(self):
"""Return the number of interfaces whose status is down."""
        	return sum(1 for status in self.interfaces if status == "down")

    	def has_owner(self):
"""Return True when the device has an owner."""
        	return self.owner != ""

    	def is_outdated(self, required_version):
"""Return True when this device's OS is older than required_version."""
        	return version_tuple(self.os_version) < version_tuple(required_version)	

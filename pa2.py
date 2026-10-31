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


def load_yaml_policy(path):
    """Open and validate the YAML compliance policy."""
    try:
        with path.open("r", encoding="utf-8") as file:
            policy = yaml.safe_load(file)
    except FileNotFoundError:
        raise InputFileError(f"File not found: {path}")
    except yaml.YAMLError as error:
        raise InputFileError(f"Invalid YAML file: {path}: {error}")

    if policy is None:
        return {}

    if not isinstance(policy, dict):
        raise InputFileError(f"Policy is not a mapping: {path}")

    return policy

def load_inventory(path):
    """Load and validate the XML inventory, returning its root element."""
    try:
        tree = ET.parse(path)
    except FileNotFoundError:
        raise InputFileError(f"File not found: {path}")
    except ET.ParseError as error:
        raise InputFileError(f"Invalid XML file: {path}: {error}")

    return tree.getroot()

def parse_device(element):
    """Convert one XML device element into a Device object, or None if skipped."""
    device_id = element.get("id")

    if device_id is None:
        return None

    owner_element = element.find("owner")
    owner = "" if owner_element is None else (owner_element.text or "").strip()

    interfaces = [
        interface.get("status", "")
        for interface in element.findall("interface")
    ]

    return Device(
        device_id=device_id,
        role=element.get("role", ""),
        os_version=element.get("os", ""),
        owner=owner,
        interfaces=interfaces,
    )


def parse_devices(root):
    """Parse all device elements, separating kept devices from skipped devices."""
    devices = []
    skipped = 0

    for element in root.findall("device"):
        device = parse_device(element)

        if device is None:
            skipped += 1
        else:
            devices.append(device)

    return devices, skipped

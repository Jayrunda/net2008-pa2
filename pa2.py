#!/usr/bin/env python3

"""JAYDEN NDAYITEGEYE PA_2"""

import json
import sys
from pathlib import Path
import yaml
import xml.etree.ElementTree as ET

class InputError(Exception):
"""Raises when you put in an unreadable file for the script or if the input is missing"""

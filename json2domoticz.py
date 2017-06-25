#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
    Send JSON-data to update Domoticz
    ---------------------------------

    This script takes JSON-data on STDIN and sends it to a Domoticz
    installation as sensor-data updates.

    Copyright (c) 2017 Anders Green <louie@louie.se>


    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.

"""

import sys
import json

from config import CONFIG as config

import requests # import requests and hide all warnings about SSL
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import SNIMissingWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)



for line in sys.stdin:
    try:
        for sensor in json.loads(line):
            result = requests.get(
                config["domoticz_host"] + config["domoticz_url"].format(**sensor),
                auth=("tellstick", "tellstick"),
                verify=False)
            rjson = result.json()
            if rjson["status"] != "OK":
                print "FAILED TO UPDATE {}".format(sensor["name"])
                print "\t{}".format(json.dumps(rjson))
            else:
                print "SUCCESSFULLY UPDATED {}".format(sensor["name"])
    except Exception as message:
        print message

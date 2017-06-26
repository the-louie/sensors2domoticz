#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
    Returns Sector Alarm armed state as JSON
    ----------------------------------------

    This script is part of a toolchain to collect and publish sensor data
    to a Domoticz installation.

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
import json
import sectoralarm.sectoralarm as sectoralarm
import sectoralarm.config as saconfig

SECTORSTATUS = sectoralarm.SectorStatus(saconfig)
ACTION = "On" if SECTORSTATUS.status()["ArmedStatus"] != "disarmed" else "Off"
print json.dumps([{
    "type": "Light/Switch",
    "idx": 234,
    "action": ACTION,
}])

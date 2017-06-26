#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
    Returns Telldus sensor-data as JSON
    -----------------------------------

    This script imitates the behavior of the tdtool --list but limited to
    sensor data. You can limit the sensors you can return by adding them
    to config.py

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


import sys
import json
import datetime

from config import CONFIG as config

import tellcore.telldus as td
import tellcore.constants as tdconst

if sys.version_info < (3, 0):
    import tellcore.library as lib
    lib.Library.DECODE_STRINGS = False

def parse_sensors(configuration):
    """
        Bake the sensors array to a dict where the telldus id is
        the key for easier parsing later on.
    """
    result = {}
    for sensor in configuration["my_sensors"]:
        result[sensor["id"]] = sensor

    return result

def is_valid_sensor(sensor, my_sensors):
    """ Filter so we only see wanted sensors"""
    valid = False
    for my_sensor_id in my_sensors.keys():
        if my_sensors[my_sensor_id]["id"] == sensor.id \
                and my_sensors[my_sensor_id]["protocol"] == sensor.protocol:
            valid = True
            break

    return valid

def get_sensor_values(sensors, my_sensors, specific_sensor=None):
    """ Get sensor values and report to Domoticz """

    result = []
    for sensor in sensors:
        if not is_valid_sensor(sensor, my_sensors) or \
            (specific_sensor and sensor.id != int(specific_sensor)):
            continue

        now = datetime.datetime.now()
        metric_timestamp = sensor.value(tdconst.TELLSTICK_TEMPERATURE).datetime
        if (now - metric_timestamp).total_seconds() > 3600:
            #print "VALUE TOO OLD {}".format(my_sensors[sensor.id]["name"])
            continue

        result.append({
            "id": sensor.id,
            "idx": my_sensors[sensor.id]["idx"],
            "type": "Temp + Humidity",
            "temperature": sensor.value(tdconst.TELLSTICK_TEMPERATURE).value,
            "humidity": sensor.value(tdconst.TELLSTICK_HUMIDITY).value,
            "name": my_sensors[sensor.id]["name"],
        })

    return result

MY_SENSORS = parse_sensors(config)

print json.dumps(get_sensor_values(
    td.TelldusCore().sensors(),
    MY_SENSORS,
    sys.argv[1] if len(sys.argv) > 1 else None
))

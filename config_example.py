""" Configuration for telldus2json and json2domoticz """
CONFIG = {
    "my_sensors": [
        {"name": "kitchen", "protocol": "mandolyn", "id": 11, "idx": 12},
        {"name": "porch", "protocol": "mandolyn", "id": 151, "idx": 14, },
        {"name": "attic north", "protocol": "mandolyn", "id": 72, "idx": 15, },
        {"name": "attic south", "protocol": "mandolyn", "id": 14, "idx": 19, },
        {"name": "bedroom", "protocol": "mandolyn", "id": 22, "idx": 24, },
        {"name": "livingroom", "protocol": "mandolyn", "id": 32, "idx": 27, },
        {"name": "outside", "protocol": "mandolyn", "id": 142, "idx": 31, },
    ],
    "domoticz_host": "https://193.168.1.10", # no trailing slash!
    # ------ DO NOT CHANGE BELOW THIS LINE IF YOU DON'T KNOW WHAT YOU'RE DOING! ------
    "domoticz_url": ("/json.htm?type=command&param=udevice&idx={idx}"
                     "&nvalue=0&svalue={temperature};{humidity};0"),
}

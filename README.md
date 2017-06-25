# sensors2domoticz
Set of scripts to update Domoticz sensor values.

WORK IN PROGRESS!

## json2domoticz
Takes a json-blob on STDIN that need the following format
```json
[
    {
        "id": 91,
        "idx": 14,
        "name": "livingroom",
        "humidity": "54",
        "temperature": "24.1"
    }, {
        "id": 92,
        "idx": 23,
        "name": "attic",
        "humidity": "59",
        "temperature": "19.7"
    }
]
```

## telldus2json
Prints a JSON-blob on STDOUT with the above format
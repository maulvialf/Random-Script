from collections import OrderedDict
import json

def beautify(raw_json):
    jsonobject = json.loads(raw_json, object_pairs_hook=OrderedDict)
    jsonstring = json.dumps(jsonobject, indent=4)
    return jsonstring


def unbeautify(beauty_json):
    jsonobject = json.loads(beauty_json, object_pairs_hook=OrderedDict)
    jsonstring = json.dumps(jsonobject, separators=(',', ':'))
    return jsonstring

def test():
    beautyjson = beautify('''{"test":{"test":"test"}}''')
    print("============")
    print(" Beautifier")
    print("============")
    print(beautyjson)
    print("============")
    print(" Unbeautify")
    print("============")
    print(unbeautify(beautyjson))


"""
============
Beautifier
============
{
    "test": {
        "test": "test"
    }
}
============
Unbeautify
============
{"test":{"test":"test"}}
"""

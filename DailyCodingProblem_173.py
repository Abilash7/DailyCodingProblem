#Write a function to flatten a nested dictionary. Namespace the keys with a period.

#For example, given the following dictionary:

#{
#    "key": 3,
#    "foo": {
#        "a": 5,
#        "bar": {
#            "baz": 8
#        }
#    }
#}

import collections
def flatten_dict(myDict, res={}, base_key=None):
    if not isinstance(myDict, dict):
        return
    else:
        actual_key =f"{base_key}." if base_key is not None else ""

        for key,value in myDict.items():
            if isinstance(value, dict):
                res=flatten_dict(value, res,actual_key+key)
            else:
                res[f"{actual_key}{key}"]=value
    return res

myDict = { "key": 3, "foo":{"a":5, "bar":{"baz":8}} }

result=flatten_dict(myDict)
print(result)
#print (flatten(myDict))

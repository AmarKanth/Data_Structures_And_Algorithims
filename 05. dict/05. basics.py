"""
1. items returns list of tuples with key, value
2. keys returns list of keys
3. values returns list of values
4. len returns the len of the dict
"""

"""
{"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}} return values of given dict in flatten list.

output should like this ['1', 1, 2, 3, 5, 1, 1, 2, 3, 4]
"""
res = []

def flatten_list(obj):
    if type(obj) == dict:
        flatten_list(list(obj.values()))
    elif type(obj) == list:
        for e in obj:
            flatten_list(e)
    else:
        res.append(obj)

flatten_list({"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}})
print(res)
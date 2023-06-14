#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listKeys = list(a_dictionary.keys())

    for dicValue in listKeys:
        if value == a_dictionary.get(dicValue):
            del a_dictionary[dicValue]

    return (a_dictionary)

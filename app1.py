"""
The purpose of this application is to provide the user an
interactive English dictionary

This application is for the beginner's who wants to search meaning of some English words
The data format used for developing this dictionary is in JSON[which looks like a python dictionary]
While building this application it has been kept in mind that the user might enter some wrong
jffcvvjvords, and this application also suggests the user what they are actually looking for!!!

Enjoy the Application
"""
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

store_data = json.load(open("data.json"))  # store data in a variable which is of the data-type dict


def similarity_ratio(parameter: str):
    global store_data
    close_match = get_close_matches(parameter, store_data.keys(), cutoff=0.8)
    print(close_match)
    resulted_close_match = close_match[0]
    print(resulted_close_match)
    if len(get_close_matches(parameter, store_data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(parameter, store_data.keys())[0])
        return "Did you mean %s instead?" % get_close_matches(parameter, store_data.keys())[0]


def dictate(parameter: list):
    global store_data
    global x
    parameter = parameter.lower()
    if parameter in store_data:
        parsed_data = store_data[parameter]
        print(parsed_data)
    elif similarity_ratio(parameter) in store_data:
        word_1 = input("Enter a word: ")
        dictate(word_1)
    return True


if __name__ == "__main__":
    word_0 = input("Enter a word: ")
    dictate(word_0)

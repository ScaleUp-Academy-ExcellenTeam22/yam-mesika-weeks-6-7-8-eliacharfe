from collections import Callable, Iterable
from typing import Dict


def group_by(func: Callable, iterable: Iterable) -> Dict:
    """
    Get a function and an iterable and return a dictionary which the keys are what the function
    returns on the item of the iterable and the value is a list of the items that the result
    on those items it is this key.
    Possible input:   len, ["hi", "bye", "yo", "try"]
    Output:           {2: ["hi", "yo"], 3: ["bye", "try"]}
    :param func: A function.
    :param iterable: An iterable.
    :return: Dictionary of key and value as explained.
    """
    dictionary_group_by_func = {}
    for item in iterable:
        dictionary_group_by_func.setdefault(func(item), []).append(item)
    return dictionary_group_by_func


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))


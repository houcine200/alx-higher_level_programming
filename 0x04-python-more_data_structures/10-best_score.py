#!/usr/bin/python3
def best_score(a_dictionary):
    # return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
    if not a_dictionary:
        return None
    top = (max(a_dictionary.values()))
    for k, v in a_dictionary.items():
        if v == top:
            return k

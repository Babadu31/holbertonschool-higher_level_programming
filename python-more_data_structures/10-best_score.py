#!/usr/bin/python3
def best_score(a_dictionary):
    mx = 0
    resultat = ""
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > mx:
                result = key
                mx = value
        return result
    else:
        return None

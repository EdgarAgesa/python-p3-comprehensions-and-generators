#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
print(return_evens([0,2,3,4,5,6,7,8]))


def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
print(make_exclamation(['hello', 'world'])) 
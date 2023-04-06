#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [i for i in num_list if i %2 == 0]
    return new_list
    # for i in range(0,8,2):
    #     return [0, 2, 4, 6, 8]
    # else:
    #     return [] 

def make_exclamation(sentence_list):
    new_list =[sentence + "!" for sentence in sentence_list if sentence != ""]
    return new_list



 
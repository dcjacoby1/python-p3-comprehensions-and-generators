#!/usr/bin/env python3

#function returns list all the even numbers in num_list
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

#adds exclamation to each string in list 
def make_exclamation(sentence_list):
    return [word + "!" for word in sentence_list]
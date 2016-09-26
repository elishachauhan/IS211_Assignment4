#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for Assignment 4 Sort"""


import random
import time

def insertion_sort(a_list):
    """Insetion Sort:

    Args:
        a_list (list): list of random numbers.

    Returns:
        elapsed (float): Function exec time.
    """

    begin = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    return time.time() - begin

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def shell_sort(a_list):
    """Shell Sort:

    Args:
        a_list (list): list of random numbers.

    Returns:
        elapsed (float): Function exec time.
   """
    begin = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    return time.time() - begin

def python_sort(a_list):
    """Python Sort:

    Args:
        a_list (list): list of random numbers.

    Returns:
        elapsed (float): Function exec time.
   """
    begin = time.time()
    a_list.sort()
    return time.time() - begin

def generate_random_list(size):
    the_list = []
    for i in range(size):
        the_list.append(random.randint(0,10000))
    return the_list

if __name__ == '__main__':

    num_list = 100
    sort_functions = [(insertion_sort,"Insertion Sort"), (shell_sort,"Shell Sort"),
                         (python_sort,"Python Sort")]
    list_sizes = [500,1000,10000]

    for list_size in list_sizes:

        sum_of_search_time_list = []

        for i in range(len(sort_functions)):
            sum_of_search_time_list.append(0.0)

        print("List of size %d:"%(list_size))

        for i in range(num_list):

            a_list = generate_random_list(list_size)

            for j, function_tuple in enumerate(sort_functions):
                function, name = function_tuple
                list_copy = a_list[:]
                duration = function(list_copy)
                sum_of_search_time_list[j] += duration

        for j, function_tuple in enumerate(sort_functions):
            function, name = function_tuple
            print("\t%s took %10.7f seconds to run, on average"%(name, (sum_of_search_time_list[j]/num_list)))

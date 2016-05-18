# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:25:05 2015

@author: matt

This script removes the null byte character
that causes other scripts to crash.

"""
import sys

def remove_nulls(in_file, out_file): 
    
    f1 = open(in_file, 'rb') 
    data = f1.read()
    f1.close()
    f2 = open(out_file, 'wb')
    f2.write(data.replace('\x00', ''))
    f2.close()


if __name__ == "__main__":
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]    
    remove_nulls(first_arg,second_arg)

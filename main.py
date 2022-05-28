#!/usr/bin/env python3

""" This is a rewrite of the Borlang Programming Language.
    My plan is to make Borlang a compiled language, but maybe 
    I will transpile this into another compiled programming language. 
"""
stack = []

filename = open("hello.bl", "r")
program = filename.read().split()

for p, op in enumerate(program):
    print(program[::])
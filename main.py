#!/usr/bin/env python3

""" This is a rewrite of the Borlang Programming Language.
    My plan is to make Borlang a compiled language, but maybe 
    I will transpile this into another compiled programming language. 
"""
import os

stack = []

fn = "hello.bl"

filename = open(fn , "r")
out_path = os.path.splitext(fn)

of = out_path[0] + ".c"
# print(of)
out = open(of, "w")
program = filename.read().split()

# I need to choose a programming language to transpile to.
out.write("#import <stdio.h>\n")
out.write("int main() {\n")
for p, op in enumerate(program):
    i = 1
    if program[p] == 'write':
        out.write(f' printf({program[p+1]});\n')
        print("I saw a write statement")
out.write("}\n")
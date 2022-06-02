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

of = out_path[0] + ".jakt"
# print(of)
out = open(of, "w")
program = filename.read().split()

# I need to choose a programming language to transpile to.
# For now i chose Jakt(https://github.com/serenityos/jakt).
# out.write("function main(args: [String]) {\n")
for p, op in enumerate(program):
    i = 1
    if program[p] == 'fun':
        out.write(f"function {program[p+1]}()\n")
    if program[p] == 'write':
        out.write('    println("{')
        out.write('}",')
        out.write(f' {program[p+1]})\n')
        # print("I saw a write statement")
    if program[p] == 'var':
        out.write(f'    let {program[p+1]} = {program[p+3]}\n')
    if program[p] == 'do':
        out.write("{")
    if program[p] == 'end':
        out.write("}\n")
# out.write("}\n")
# os.system(f"jakt {of}")

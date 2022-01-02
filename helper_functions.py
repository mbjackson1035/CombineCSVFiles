import os

def chomp(x):
    "This removes EOL (end of line) character. Equivalent to Perl's chomp"
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x

def number_of_lines_in_file(x):
    num_lines = sum(1 for line in open(x,"rb"))
    return num_lines;


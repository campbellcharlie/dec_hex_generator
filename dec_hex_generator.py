#!/usr/bin/python

#Simple script to generate hex vaules from decimal input values and output them into a list
#Example usage: python dec_hex_generator.py 400 500 > output.txt

import sys

def int_tuple_from_cmdline():
      """return exactly two integers form sys.argv
         or die with an error message
      """
      import sys
      args = sys.argv[1:] # drop first entry (progpath)
      if len(args) != 2:
          raise SystemExit("\n#################################################\n# Please enter both a start and stop parameter. #\n#################################################")
      for i in range(len(args)):
          try:
             args[i] = int(args[i])
          except ValueError:
             raise SystemExit("\n#################################################\n# Parameter %d is not an integer. You entered: %s #\n#################################################\n" %(i+1,
args[i]))
      return tuple(args)

start, stop = int_tuple_from_cmdline()

r = start - 1
while r < stop:
	r = r + 1 
	hx = hex(r)[2:]
	print(hx)

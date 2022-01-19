#!/bin/bash

import math
import sys
from getopt import getopt

class COLORS:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


class EXIT_CODES:
	OK = 0
	ERROR = 1


def main():
	args = getopt(sys.argv[1:], "a:b:c:")[0]
	params = ['-a', '-b', '-c']
	if not args:
		for param in params:
			arg = input("Please, enter '" + param[1:] + "' parameter: ")
			valid_number = validate_param(arg)
			if not valid_number:
				sys.exit(EXIT_CODES.ERROR)
			args.append(valid_number)
	else:
		args_dict = dict(sorted(args, key=lambda item: item[0]))
		if not len(args_dict) == 3:
			print(COLORS.FAIL + "There are missing arguments: " + COLORS.ENDC + ", ".join(item for item in (set(params) - set(args_dict))))
			sys.exit(EXIT_CODES.ERROR)
		args = []
		for arg in args_dict:
			sys.stdout.write("Param '" + arg[1:] + "': ")
			valid_number = validate_param(args_dict[arg])
			if valid_number:
				args.append(valid_number)
				sys.stdout.write("Ok\n")
				continue
			else:
				sys.exit(EXIT_CODES.ERROR)
	roots = solv_square(a=args[0], b=args[1], c=args[2])
	square_print(a=args[0], b=args[1], c=args[2], roots=roots)
	sys.exit(EXIT_CODES.OK)


def validate_param(arg):
	for i in range(4):
		try:
			arg = float(arg.replace(',', '.'))
		except:
			message = COLORS.FAIL + "You've entered incorrect value! " + COLORS.ENDC
			if i < 3:
				message += "Please, repeat your input: "
				arg = input(message)
				continue
			else:
				message += "Please, have some rest and try again later!"
				print(message)
				return False
		return arg
		
	
def discriminant(a, b, c):
	return b * b - 4 * a * c
	

def roots(d, a, b, c):
	if d < 0:
		return []
	elif d == 0:
		return [
			-b / (2 * a)
		]
		
	discriminant_root = math.sqrt(d)
	return [
		(-b - discriminant_root) / (2 * a),
		(-b + discriminant_root) / (2 * a)
	]
	

def solv_square(a, b, c):
	d = discriminant(a, b, c)
	square_roots = roots(d, a, b, c)
	return square_roots
	

def square_print(a, b, c, roots):
	output = ""
	if not a == 0:
		if abs(a) == 1:
			if a < 0:
				output += "-"
			output += "x²"
		else:
			if int(a) == float(a):
				output += str(int(a))
			else:
				output += str(float(a))
			output += "x²"
			
	
	if not b == 0:
		if b >= 0:
			output += "+"

		if abs(b) == 1:
			if b < 0:
				output += "-"
			output += "x"
		else:
			if int(b) == float(b):
				output += str(int(b))
			else:
				output += str(float(b))
			output += "x"
		
	if not c == 0:
		if c > 0:
			output += "+"
		if int(c) == float(c):
			output += str(int(c))
		else:
			output += str(float(c))

	output += " = 0\n"
	subnum = ['₁', '₂']
	for i, root in enumerate(roots):
		output += COLORS.OKGREEN + "x" + subnum[i] + " = " + str(root) + "\n" + COLORS.ENDC
	
	if not roots:
		output += COLORS.WARNING + "There are no roots in this equasion!" + COLORS.ENDC
	print(output)

if __name__ == "__main__":
	main()
	

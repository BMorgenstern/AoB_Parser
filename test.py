import sys,re,struct
from readin import *
from funcs import*
from specialcall import SpecialCall

def main(args):
	if len(args) != 3:
		print('Usage error')
		return
	with open(args[-2], 'br') as game:
		with open("output.cpp" ,'w') as out:
			src = game.read()
			with open(args[-1] ,'r') as ifile:
				lines = ifile.readlines()
				for line in lines:
					for key in FUNCS.keys():
						for match in matchKeys(key, line):
							callobj = getCall(match)
							result = FUNCS[callobj.getFunc()](src, callobj.getArgs()[0])
							line = line.replace(match, hex(result))
					out.write(line)

if __name__ == '__main__':
	main(sys.argv)

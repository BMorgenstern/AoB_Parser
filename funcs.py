import struct

def fromBin(dump, size, offset):
	return int(hex(struct.unpack('<I', dump[offset:offset+size])[0]),16)

def noquotes(var):
	return var.replace('\'', '').replace('\"', '')

def addrofLiteral(pos):
	return pos | 0x8000000

def posof(src, dumpfile):
	dumpfile = noquotes(dumpfile)
	with open(dumpfile, 'br') as dumpf:
		dump = dumpf.read()
	return src.find(dump)

def addrof(srcfile, dump):
	return addrofLiteral(posof(srcfile, dump))

def thumbfunc(src, dump):
	return addrof(src,dump) | 1

def valAfter(src, dumpfile):
	dumpfile = noquotes(dumpfile)
	off = posof(src, dumpfile)
	with open(dumpfile, 'br') as dumpf:
		dump = dumpf.read()
	off += len(dump)
	return fromBin(src, 4, off)

def square(dummyarg, realarg):
	a = int(realarg)
	return a*a

FUNCS = { 
	'posof' : posof, 
	'valAfter' : valAfter, 
	'addrof': addrof, 
	'square': square,
	'thumbfunc' : thumbfunc
}
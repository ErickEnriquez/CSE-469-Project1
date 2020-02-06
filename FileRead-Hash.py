#!/usr/bin/env python
import sys
import hashlib
	


filename = sys.argv[1]
print(filename)

BLOCK_SIZE = 512

file_hash_obj = hashlib.sha256()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash_obj.update(fb)
        fb = f.read(BLOCK_SIZE)
    
print(file_hash_obj.hexdigest())


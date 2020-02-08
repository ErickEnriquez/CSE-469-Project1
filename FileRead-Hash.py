#!/usr/bin/env python
import sys
import os
import hashlib
	
filename = sys.argv[1] #get the name of the file

BLOCK_SIZE = 512 # size of the block we will be reading while hashing

Md5file = "MD5" + filename
ShaFile  = "SHA256" +filename

Md5file = os.path.splitext(Md5file)[0]# remove the .raw extension
ShaFile = os.path.splitext(ShaFile)[0]# remove .raw extension

Md5file = Md5file + '.txt'
ShaFile = ShaFile + '.txt'


#hash the file with SHA 256
file_hash_obj = hashlib.sha256()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash_obj.update(fb)
        fb = f.read(BLOCK_SIZE)

#write the result into the file
with open(ShaFile,'w') as FileHandler:
    FileHandler.write(file_hash_obj.hexdigest())

#hash the file with MD5    
file_hash_obj = hashlib.md5()
with open(filename, 'rb') as fh:
    fb = fh.read(BLOCK_SIZE)
    while len(fb) > 0 :
        file_hash_obj.update(fb)
        fb  = fh.read(BLOCK_SIZE)

with open(Md5file,'w') as FileHandler:
    FileHandler.write(file_hash_obj.hexdigest())

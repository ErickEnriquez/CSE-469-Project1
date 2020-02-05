import sys
import hashlib
	
from zipfile import ZipFile

with ZipFile('sample.raw.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

filename = 'sample_final.raw'

BLOCK_SIZE = 512

file_hash_obj = hashlib.sha256()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash_obj.update(fb)
        fb = f.read(BLOCK_SIZE)
    
print(file_hash_obj.hexdigest())
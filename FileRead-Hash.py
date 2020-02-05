import sys
import hashlib


filename = 'sample_final.raw'

BLOCK_SIZE = 512

file_hash_obj = hashlib.md5()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash_obj.update(fb)
        fb = f.read(BLOCK_SIZE)
    
print(file_hash_obj.hexdigest())
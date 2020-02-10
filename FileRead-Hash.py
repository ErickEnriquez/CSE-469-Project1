#!/usr/bin/env python
import sys      # reading command line args
import os       # splits strings 
import hashlib  # hashing library
import binascii # reading file in hex
	
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
file_hash_MD5 = hashlib.md5()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    data = fb #read first 512 bytes of data of master boot record
    while len(fb) > 0:
        file_hash_obj.update(fb)
        file_hash_MD5.update(fb)
        fb = f.read(BLOCK_SIZE)

#write the result into the file
with open(ShaFile,'w') as FileHandler:
    FileHandler.write(file_hash_obj.hexdigest())

#write the MD5 result into the file
with open(Md5file,'w') as FileHandler:
    FileHandler.write(file_hash_MD5.hexdigest())

dataString = binascii.hexlify(data)
print("\n\n\n")
partition1 = dataString[446*2:(462)*2]  # 1st partition 
print(partition1 , "length is" , len(partition1)/2 )
partition2 = dataString[462*2:478*2]      # 2nd partition
print(partition2 , "length is" , len(partition2)/2 )
partition3 = dataString[477*2:493*2]      # 3nd partition
print(partition3 , "length is" , len(partition3)/2 )
partition4 = dataString[494*2:510*2]      # 4th partition
print(partition4 , "length is" , len(partition4)/2 )
print("\n\n\n")
print(dataString) # print out the hex data
print("length of the data string is " , len(dataString)/2)
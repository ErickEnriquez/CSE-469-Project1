#!/usr/bin/env python
import sys      # reading command line args
import os       # splits strings 
import hashlib  # hashing library
import binascii # reading file in hex
	
filename = sys.argv[1] #get the name of the file

BLOCK_SIZE = 512 # size of the block we will be reading while hashing

Md5file = "MD5" + filename
ShaFile  = "SHA1" +filename

Md5file = os.path.splitext(Md5file)[0]# remove the .raw extension
ShaFile = os.path.splitext(ShaFile)[0]# remove .raw extension

Md5file = Md5file + '.txt'
ShaFile = ShaFile + '.txt'


#hash the file with SHA 1
file_hash_obj = hashlib.sha1()
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

offset  = 446 * 2
byte = 2 
word = 4 * 2
doubleword = 8 * 2
partitionlength = 16 * 2
# make a matrix by appending 4 lists to a matrix
matrix = []
for i in range(0,4):
    matrix.append([])

dataString = binascii.hexlify(data) # make the data we have into a hex string


i = 0
while(offset < 1020 ) :# while we we haven't finished the parition
    partition = dataString[offset: offset + partitionlength] #grab the 16 bytes of the partition
    paritiontype = partition[word:word+byte] # grab the partition type
    startingsectorle = partition[doubleword:doubleword + word]
    sizeLittle = partition[doubleword + word : partitionlength]

    sizeBig = bytearray.fromhex(sizeLittle)#convert the big endian to do math on the number
    sizeBig.reverse()#reverse the array
    sizeString = ''.join(format(x, '02x') for x in sizeBig)#format the string back and remove the byte array part
    sizeNumber = int(sizeString,16)
    sizeString = str(sizeNumber)


    startingsectorbe = bytearray.fromhex(startingsectorle)#convert the big endian to do math on the number
    startingsectorbe.reverse()#reverse the array
    s = ''.join(format(x, '02x') for x in startingsectorbe)#format the string back and remove the byte array part
    number = int(s,16)
    startingAddress =str(number)
    
    output_data = paritiontype + " " + startingAddress.zfill(10) + " " + sizeString.zfill(10)
    print(output_data)

    #print(paritiontype)
    last8bytes = partition[doubleword:doubleword + doubleword]
    counter = 0
    while(counter < 16):#format the last 8 bytes
        dataAsInt = int(last8bytes[counter:counter+2],16)
        dataAsInt = dataAsInt*512
        matrix[i].append(last8bytes[counter:counter+2])
        counter+=2
    offset = offset + partitionlength
    i+=1
#print(matrix)

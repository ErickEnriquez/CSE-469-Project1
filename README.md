# CSE_469_Homework1


Erick Enriquez

ASU ID: 1208001804

This is an exercise in being able to read in hex values from a master boot record, hashing and checking hashes, and determining types of partitions on a drive given raw data file  

first we open the file, and hash the file with md5 and sha256, then we create the text files and write the hashes to them , next we take the 512 bytes and convert them to hex by using the binascii library and the .hexify function, which takes the 512 bytes and creates 1024 length string containing the master boot record and split it up into the boot loader , the partition data , and the signature, 

we then open up the csv 


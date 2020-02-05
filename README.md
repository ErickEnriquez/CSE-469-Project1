# CSE_469_Homework1


Erick Enriquez

ASU ID: 1208001804

This is an exercise in being able to read in hex values from a master boot record, hashing and checking hashes, and determining types of partitions on a drive given raw data file  

We need to figure out how we are going to actually open this file and read the values that it holds

traceback (most recent call last):
  File "/home/erick/Documents/cse_469_homework1/FileRead-Hash.py", line 10, in <module>
    with open(filename, 'rb') as f:
IOError: [Errno 13] Permission denied: 'sample_final.raw'


We also need to figure out how to read command line arguments and make a makefile that can create a python executable


run: FileRead-Hash.py
	cp FileRead-Hash.py mbr_info
	chmod +x mbr_info
	./mbr_info

clean:
	rm mbr_info

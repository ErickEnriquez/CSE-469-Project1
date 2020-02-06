

run: FileRead-Hash.py
	cp FileRead-Hash.py mbr_info
	chmod +x mbr_info
	./mbr_info sample_final.raw

clean:
	rm mbr_info

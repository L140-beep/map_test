CC=g++
CFLAGS=-c -Wall -std=c++2a

ifeq ($(OS), Winsows_NT)
	RM = del
	OUTNAME = get_data.exe
else
	RM = rm -rf
	OUTNAME = get_data.out
endif

all:
	$(CC) get_data.cpp -o $(OUTNAME)

clean:
	$(RM) *.out *.o *.h.gch *.txt

run: all
	./$(OUTNAME)
	python get_data.py
	python main.py

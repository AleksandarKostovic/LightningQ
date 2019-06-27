SRC=src/qubit.py
CMD=python3

all: build

build:

	$(CMD) $(SRC)

clean:

	rm *.gds

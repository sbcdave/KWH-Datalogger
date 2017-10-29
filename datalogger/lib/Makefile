VERSION	= 0.9.1

PREFIX	= /usr

CC	= gcc
CFLAGS	= -W -Wall -Wextra -Werror \
	-DVERSION=\"$(VERSION)\" \
	-g
LDFLAGS =

all: atinout

atinout: atinout.c
	$(CC) -o $@ $(CFLAGS) $(LDFLAGS) $^

clean:
	rm -f atinout

install: all

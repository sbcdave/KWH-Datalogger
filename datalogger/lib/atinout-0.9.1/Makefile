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
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp atinout $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)$(PREFIX)/share/man/man1
	cp atinout.1 $(DESTDIR)$(PREFIX)/share/man/man1/atinout.1

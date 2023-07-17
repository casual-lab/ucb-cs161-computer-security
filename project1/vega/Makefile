TARGET  := flipper

CFLAGS  := -g -ansi -O0 -fno-stack-protector -Wall -Werror -fno-pic -static -mpreferred-stack-boundary=2

LDFLAGS := -z execstack

all:	$(TARGET)

$(TARGET):	$(TARGET).c
	gcc $(CFLAGS) $(LDFLAGS) -o $@ $< 

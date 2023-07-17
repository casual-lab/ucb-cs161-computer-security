TARGET  := dehexify

CFLAGS  := -g -ansi -O0 -Wall -Werror -mpreferred-stack-boundary=2

LDFLAGS := -z execstack

all:	$(TARGET)

$(TARGET):	$(TARGET).c
	gcc $(CFLAGS) $(LDFLAGS) -o $@ $< 

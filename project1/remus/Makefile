TARGET  := orbit

CFLAGS  := -g -ansi -O0 -fno-stack-protector -Wall -Werror -fno-pic -static -fno-pie

LDFLAGS := -z execstack

all:	$(TARGET)

$(TARGET):	$(TARGET).c
	gcc $(CFLAGS) $(LDFLAGS) -o $@ $< 

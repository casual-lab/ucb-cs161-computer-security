TARGET  := orbit

CFLAGS  := -g -ansi -O0 -fno-stack-protector -Wall -Werror

LDFLAGS := -z execstack

all:	$(TARGET)

$(TARGET):	$(TARGET).c
	gcc $(CFLAGS) $(LDFLAGS) -o $@ $< 

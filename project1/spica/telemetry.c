#include <stdint.h>
#include <stdio.h>
#include <string.h>

void display(const char *path)
{
  char msg[128];
  int8_t size;
  memset(msg, 0, 128);

  FILE *file = fopen(path, "r");
  if (!file) {
    perror("fopen");
    return;
  }
  size_t n = fread(&size, 1, 1, file);
  if (n == 0 || size > 128)
    return;
  n = fread(msg, 1, size, file);

  puts(msg);
}


int main(int argc, char *argv[])
{
  if (argc != 2)
    return 1;

  display(argv[1]);
  return 0;
}

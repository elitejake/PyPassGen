# -*- coding: utf-8 -*-
"""
@author: elitejake
"""

defaults = 'Configuration for PyPassGen\n\nLength of password:\n16\n\nNumber of passwords to generate:\n10\n\nOutput filename: (optional)\npasswords.txt\n\nPrint generated password(s) in the terminal?: [Y, N]\nN\n\nUse secrets module?: [Y, N]\nY\n\n\nCan the password contain...\n\n... upper-case alphabets: [Y, N]\nY\n\n... numbers: [Y, N]\nY\n\n... symbols: [Y, N]\nY\n\nIf you somehow mess this file up, use defaults.py to reset this all the parameters.'

try:
    with open('config.txt', 'w') as config:
        config.write(defaults)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

    

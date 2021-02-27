#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import main

arg = sys.argv

password_array = []

help_arguments = '''
PyPassGen HELP

PyPassGen is short for Python Password Generation, just in case you\'re wondering.

Usage:
    PyPassGen-cli.py [arguments]

PASSWORD CONFIGURATION:
-l           Disables upper-case alphabet in generated passwords.
-n           Disables numerals (0, 1, 2, ...) in generated passwords.
-s           Disables symbols (!, @, $, ...).
-L <length>  Length of the password to generate.
-C           Uses config.txt to get parameters. It will override cli arguments.

OUTPUT:
-N <num>     Number of passwords to generate.
-o <file>    Outputs generated passwords to a file.
-c           Copies the generated password to the clipboard (requires tkinter, broken).
-p           Disables printing the password to the terminal.
-S / -strong Uses secrets module to produce cryptographically random password.

EXAMPLES:
PyPassGen-cli.py -p
PyPassGen-cli.py -N 200 -l -n -o passwords.txt
PyPassGen-cli.py -l -c -strong -s
'''

if len(arg) <= 1:
    print(help_arguments)
    help_print = True
else:
    help_print = False

if '-l' in arg:
    uppercase = False
else:
    uppercase = True

if '-n' in arg:
    numbers    = False
else:
    numbers    = True

if '-s' in arg:
    symbols    = False
else:
    symbols    = True

if '-c' in arg:
    try:
        from tkinter import tk        
        clip   = True
        r      = tk()
    except ImportError:
        print('Passwords will not be copied to the clipboard. This is because you doesn\'t appear to have tkinter or your Python may not be configured for tkinter.')
        clip   = False
else:
    clip       = False

if '-p' in arg:
    printOut   = False
else:
    printOut   = True
    
if '-S' in arg:
    strong_ran = True
elif '-strong' in arg:
    strong_ran = True
else:
    strong_ran = False
    
if '-N' in arg:
    n = arg.index('-N') + 1
    try:
        number_of_passwords = int(arg[n])
        if clip:
            print('Only the last password will be copied to the clipboard.\n')
    except ValueError:
        print('-N option:', arg[n], 'is invalid. It couldn\'t be converted into int.')
else:
    number_of_passwords = 1

if '-o' in arg:
    file_out = True
    n = arg.index('-o') + 1
    try:
        output_filename = arg[n]
    except IndexError:
        print('You didn\'t provide a filename.')
        file_out = False
else:
    file_out = False

if '-L' in arg:
    n = arg.index('-L') + 1
    try:
        length = int(arg[n])
    except ValueError:
        print('-L option:', arg[n], 'is invalid. It couldn\'t be converted into int.')
        length = 8
    except IndexError:
        print('-L requires an argument!')
        length = 8
else:
    length = 8
    
if '-C' in arg:
    try:
        with open('config.txt', 'r') as config:
            line       = config.readlines()
            length     = int(line[3].rstrip())
            number_of_passwords = int(line[6].rstrip())
            printOut   = True if line[12].rstrip() == 'Y' else False
            file_out   = True
            strong_ran = True if line[15].rstrip() == 'Y' else False
            uppercase  = True if line[21].rstrip() == 'Y' else False
            numbers    = True if line[24].rstrip() == 'Y' else False
            symbols    = True if line[27].rstrip() == 'Y' else False
            
            if line[9] == '\n':
                file_out = False
            else:
                file_out = True
                output_filename = line[9].rstrip()
            
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if help_print is False:
    for i in range(number_of_passwords):
        password = main.generate_password(length, uppercase, numbers, symbols, strong_ran)
        if printOut:
            print(password)
        if clip: #This is probably broken for now
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(password)
            r.update()
            r.destroy()
        if file_out:
            password_array.append(password)

if file_out:
    print('\nWriting to', output_filename + '!')
    main.write_to_file(password_array, output_filename)
    print('Done!\n')

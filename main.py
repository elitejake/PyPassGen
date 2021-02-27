#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: elitejake
"""

import random
import sys
import secrets

ver = '1.0.0' #version

UpperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers   = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols   = ['~', '`', '!', ' ', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '\"', '\'', '<', '>', ',', '.', '?', '/']

def generate_character(upper, numbers, symbols, strong_random):
    """
    Returns a character (str) which complies with the parameters.

    Parameters
    ----------
    upper : bool
        If True, then the returned character (str) is allowed to be a upper-case alphabet.
    numbers : bool
        If True, then the returned character (str) is allowed to be a digit.
    symbols : bool
        If True, then the returned character (str) is allowed to be a symbol.
    strong_random : bool
        If True, then the function uses the secrets module rather than the random module.

    Returns
    -------
    character : str
        The returned str will be a random character.

    """
    character_set = []
    
    if strong_random:
        if upper:
            character_set.append(secrets.choice(UpperCase))
            character_set.append(secrets.choice(LowerCase))
        else:
            character_set.append(secrets.choice(LowerCase))
            
        if numbers:
            character_set.append(secrets.choice(Numbers))
            
        if symbols:
            character_set.append(secrets.choice(Symbols))
            
        character =  secrets.choice(character_set)
        
        return character
    
    if upper:
        character_set.append(random.choice(UpperCase))
        character_set.append(random.choice(LowerCase))
    else:
        character_set.append(random.choice(LowerCase))
        
    if numbers:
        character_set.append(random.choice(Numbers))
        
    if symbols:
        character_set.append(random.choice(Symbols))
        
    character =  random.choice(character_set)
    
    return character

def generate_password(length, upper, numbers, symbols, strong_random):
    """
    Returns a str with random characters which complies with the parameters.

    Parameters
    ----------
    length : int
        The length of the password.
    upper : bool
        If True, then the returned password (str) is allowed to contain upper-case characters.
    numbers : bool
        If True, then the returned password (str) is allowed to contain digits.
    symbols : bool
        If True, then the returned password (str) is allowed to contain symbols.
    strong_random : bool
        If True, then generate_character() will use the secrets module rather than the random module.

    Returns
    -------
    password : str
        The generated password.

    """
    password = ''
    
    for i in range(length):
        character = generate_character(upper, numbers, symbols, strong_random)
        
        password = password + character
    
    return password

def write_to_file(passwords, filename):
    """
    Writes all the elements of the passwords (array) to filename (str).

    Parameters
    ----------
    passwords : array
        Contains the passwords.
    filename : str
        The name of the file.

    Returns
    -------
    None.
    
    Raises
    ------
    OSError :
        If couldn\'t write to file.
    
    """
    length = len(passwords)
    
    try:
        with open(filename, 'w') as file:
            for i in range(length):
                temp = passwords[i]
                file.write(temp + '\n')

    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def version():
    """
    Returns the version of PyPassGen.

    Returns
    -------
    ver : str
        Version of PyPassGen.

    """
    return ver

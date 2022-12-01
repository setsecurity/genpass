# GenPass

GenPass - Word based password generator

By Jokin Totem Security

Script in python3 to generate a password wordlist based on a given word.


**Usage:** python3 genpass.py word  

**Options:**  
* Help: python3 genpass.py -h    
* Capitalize the word: python3 genpass.py -t word  
* Combination options: python3 genpass.py -c 1,2,3 word  

    
**Posible combinations:**  
    1: name + year -> totem1999  
    2: name + specialchar -> totem#  
    3: name + scpecialchar + year -> totem@1992  
    4: name + year + scpecialchar -> totem2001$  
    5: name + num -> totem0  
    6: name + num + scpecialchar -> totem3!  
    7: name + scpecialchar + num -> totem@0  
    8: name + num2 -> totem05  
    9: name + num2 + scpecialchar -> totem31!  
    10: name + scpecialchar + num2 -> totem@19  
    11: name + num3 -> totem100  
    12: name + num3 + scpecialchar -> totem011
    13: name + scpecialchar + num3 -> totem@168  
    14: name in hack language -> t0t3m  
    15: name in hack language + year -> t0tem2001  
    16: name in hack language + year + scpecialchar -> tot3m1999  
    17: name in hack language + scpecialchar + year -> tot3m@1999  
    

If you want to suggest a new combination, send an email to totem-security@protonmail.com

Note: the given word becomes lowercase.  
Note: the script generates a wordlist file named genpass.txt


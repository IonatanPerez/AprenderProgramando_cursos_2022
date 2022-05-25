# Este archivo revisa todos los archivos en la carpeta y los renombre para evitar caracteres raros, acentos y espacios

import os
import sys
import unicodedata
import re

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    #value = re.sub(r'[^\w\s-]', '', value.lower())
    #re.sub(r'[-\s]+', '-', value).strip('-_')
    return value

directory = os.path.dirname(os.path.realpath(sys.argv[0])) #get the directory of your script
for subdir, dirs, files in os.walk(directory): 
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']     # use files and dirs 
    for filename in files:
        
        subdirectoryPath = os.path.join(directory, subdir) #get the path to your subdirectory
        filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
        if filePath[0] != ".":
            if filePath != slugify(filePath):
                print (slugify(filePath))
                print (os.path.isfile(filePath))
            os.rename(filePath, slugify(filePath)) #rename your file
        
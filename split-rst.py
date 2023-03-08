# Script splitting the large .rst file into parts.
# Loads input file (first arg), separates it by chapter headings names,
# then writes the result to a named tree of "source" subdir (second arg).
# the headers will be names of SubSubdirectories 
######### example: python split-docs.py TestDataSyntax.rst newSubBranchName
######### NOTE: BE CAREFULLY!!! it remove all old related named subdirectories

import sys
import unicodedata
import re
import os
import shutil
import logging


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
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')
 
def remove_last_line(s):
    """
    Remove last line of string
    """
    return s.rsplit("\n",2)[0]

def split_rst(filename):
    """
    Splits an .rst file into chunks based on the headings in the file.
    """
    with open(filename, 'r') as file:
        text = file.read()
        
    chunks = []
    current_chunk = ''
    current_heading = ''
    old_line = '\n'
    
    for line in text.split('\n'):
        if line.startswith('==') and current_heading == '':
            current_heading = line.strip()
            if current_chunk != '':
                remove_last_line(current_chunk)
                chunks.append(current_chunk)
                current_chunk = old_line            
        elif line.startswith('--') and current_heading == '':
            current_heading = line.strip()
            if current_chunk != '':
                remove_last_line(current_chunk)
                chunks.append(current_chunk)
                current_chunk = old_line                             
        else:
            current_chunk += old_line
            current_heading = ''
        old_line = line + '\n'
    chunks.append(current_chunk)
    return chunks[1:]

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logger = logging.getLogger('split-rst')
    chunks = split_rst( sys.argv[1] )

    for part in chunks:
        path = 'source/'+ sys.argv[2] + '/' + slugify(part.split("\n",1)[0])
        file = path + "/index.rst"
        print(path+"/media :")
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
            os.makedirs(path)
            file = open(file , "w")
            file.write(part)
            file.close()
            file_names = re.findall(r'\b\w+\.png\b', part)
            print(str(file_names))
            sdir = os.getcwd()+'/media'
            os.makedirs(sdir,exist_ok=True)
            ddir = path+'/media'
            os.makedirs(ddir,exist_ok=True)    
            for f in file_names:
                source = os.path.join(sdir,f)
                destin = os.path.join(ddir,f)
                if os.path.isfile(source):
                    shutil.move(source, destin)
        except FileExistsError as e:
            logger.error('Failed write: '+ str(e))
    
    


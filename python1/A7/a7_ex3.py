import os

def file_statistics(path: str, encoding: str = 'CP1252') -> tuple:
    """
    read a text file from the specified path and count the types of characters in the file.
    
    parameters:
    path (str): the path of the text file.
    encoding (str): encoding format used when reading the file, default value is 'CP1252'.
    
    return:
    tuple: including the number of Latin letters, the number of digits, the number of spaces, and a list of other characters.
    """
    # check the encoding from the file name
    filename = os.path.basename(path).lower()
    if 'cp1252' in filename:
        inferred_encoding = 'cp1252'
    elif 'utf8' in filename or 'utf-8' in filename:
        inferred_encoding = 'utf-8'
    else:
        inferred_encoding = 'cp1252'  # 默认编码

    # if encoding is specified, use the specified encoding
    if encoding:
        final_encoding = encoding
    else:
        final_encoding = inferred_encoding

    # initializes the statistical counter
    latin_count = 0
    digit_count = 0
    space_count = 0
    other_chars = []  # collects other characters

    try:
        # open file with specified encoding
        with open(path, 'r', encoding=final_encoding) as file:
            # read file line by line
            for line in file:
                # read each line character by character
                for char in line:
                    if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
                        # if latin
                        latin_count += 1
                    elif char.isdigit():
                        # if digit
                        digit_count += 1
                    elif char.isspace():
                        # if space
                        space_count += 1
                    else:
                        # if other characters
                        other_chars.append(char)
        
        # return the statistical results
        return (latin_count, digit_count, space_count, other_chars)
    
    except Exception as e:
        # if any error, print error message and return an empty tuple
        print(f"An error occurred: {e}")
        return (0, 0, 0, [])
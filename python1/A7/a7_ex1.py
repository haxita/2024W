import os

def analyze_log_file(filename: str, keyword: str) -> int:
    # split file name and extension
    file_stem, ext = os.path.splitext(filename)
    
    # generate new file name
    new_filename = f"{file_stem}_{keyword}{ext}"
    
    count = 0  # initialize count
    
    try:
        # open input file and output file
        with open(filename, 'r', encoding='utf-8') as infile, open(new_filename, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # check keyword
                if keyword.lower() in line.lower():
                    outfile.write(line)
                    count += 1
        return count
    except FileNotFoundError:
        # if file not exist return None
        return None
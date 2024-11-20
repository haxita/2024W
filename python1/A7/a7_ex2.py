import os
import shutil

def organize_directory(src_path: str):
    """
    orgnize directory and files in it by file extension. Record the move process to move.log.

    params:
    src_path (str): path to the source directory to be organized.
    
    return:
    None
    """
    # check src_path exist and is a directory
    if not os.path.isdir(src_path):
        # if src_path does not exist or is not a directory, record error message to move.log
        # move.log created in the same directory at the current working directory
        with open('move.log', 'w', encoding='utf-8') as log_file:
            log_file.write(f"Error: '{src_path}' is not a valid directory.\n")
        return
    
    # get src_path absolute path
    src_path = os.path.abspath(src_path)
    
    # get parent directory and directory name
    parent_dir, dir_name = os.path.split(src_path)
    
    # construct organized directory path
    organized_dir = os.path.join(parent_dir, f"{dir_name}_organized")
    
    # create target organized directory if not exist
    os.makedirs(organized_dir, exist_ok=True)
    
    # construct log file path
    log_path = os.path.join(organized_dir, 'move.log')
    
    # open and record move process to move.log
    with open(log_path, 'w', encoding='utf-8') as log_file:
        # recursively go through the src_path and its subdirectories
        for root, dirs, files in os.walk(src_path):
            for file in files:
                # construct the full path of the original file
                original_path = os.path.join(root, file)
                
                # get the file extension (without the dot) and convert to lowercase
                _, ext = os.path.splitext(file)
                ext = ext[1:].lower() if ext else 'no_extension'
                
                # construct the target subdirectory path
                target_subdir = os.path.join(organized_dir, ext)
                
                # construct the target subdirectory path create target subdirectory if not exist
                os.makedirs(target_subdir, exist_ok=True)
                
                # construct the new file path
                new_path = os.path.join(target_subdir, file)
                
                try:
                    # move file to target subdirectory
                    shutil.move(original_path, new_path)
                    
                    # get relative path to meet test expectation
                    relative_original = os.path.relpath(original_path, start=os.path.dirname(src_path))
                    relative_new = os.path.relpath(new_path, start=os.path.dirname(src_path))
                    
                    # record the move process to log file
                    log_file.write(f"Copied '{relative_original}' to '{relative_new}'\n")
                except Exception as e:
                    # record error message to move.log
                    log_file.write(f"Error moving '{original_path}' to '{new_path}': {str(e)}\n")
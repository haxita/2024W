import os
import pickle

def analyze_and_append_logs(directory: str, output_file: str):
    """
    anaylze log file in the specified directory, count the number of occurrences of the "ERROR" keyword in each log file, and append the results to a pickle file.
    
    parameters:
    directory (str): log file directory path.
    output_file (str): pickle file path to store the statistical results.
    
    return:
    None
    """
    # recursively search for .log files in directory 
    log_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.log'):
                full_path = os.path.join(root, file)
                log_files.append(full_path)
    
    # count the number of occurrences of the "ERROR" keyword in each log file
    error_counts = {}
    for log_file in log_files:
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                content = f.read()
                count = content.count("ERROR")
                
                # get the relative path to the current working directory
                relative_path = os.path.relpath(log_file, start=os.getcwd())
                
                error_counts[relative_path] = count
        except Exception as e:
            print(f"Can not read log file {log_file}: {e}")
    
    # try load existing pickle file data (if exists)
    if os.path.exists(output_file):
        try:
            with open(output_file, 'rb') as pf:
                existing_data = pickle.load(pf)
        except Exception as e:
            print(f"can not load pickle file {output_file}: {e}")
            existing_data = {}
    else:
        existing_data = {}
    
    # update the statistical results to the existing data
    for relative_path, count in error_counts.items():
        existing_data[relative_path] = count
    
    # write the updated data back to the pickle file
    try:
        with open(output_file, 'wb') as pf:
            pickle.dump(existing_data, pf)
    except Exception as e:
        print(f"can not write in pickle file {output_file}: {e}")
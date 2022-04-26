import os
import re
import argparse

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', type=str, help='directory of the files to be rename', required=True)
parser.add_argument('-n', '--base_name', type=str, help='base name of each file', required=True)
parser.add_argument('-e', '--extension', type=str, help='extension of each file', required=True)
args = parser.parse_args()

directory = args.directory
base_name = args.base_name
extension = args.extension

data_folder_path = os.path.join(os.getcwd(), directory)

for file in os.listdir(data_folder_path):
    # extract one or more digits before the extension
    number_found = re.findall('([0-9]+)\S*\.', file)
    
    # assuming that the file with no number is the first file,
    file_index = number_found[0] if len(number_found) != 0 else '1'
    
    # rename the file
    file_path_old = os.path.join(data_folder_path, file)
    file_path_new = os.path.join(data_folder_path, f'{base_name}-{file_index.zfill(4)}.{extension}')

    os.rename(file_path_old, file_path_new)
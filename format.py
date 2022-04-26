import os
import argparse
import random

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_script', type=str, help='script file', required=True)
parser.add_argument('-d', '--dataset_directory', type=str, help='directory where audio files reside', required=True)
parser.add_argument('-o', '--output', type=str, default="metadata.csv", help='output file')
parser.add_argument('-se', '--start_entry', type=int, default=0, help='the audio index where the dataset begins')
parser.add_argument('-ee', '--end_entry', type=int, default=-1, help='the audio index where the dataset ends')
parser.add_argument('-s', '--shuffle', type=bool, default=False, help='whether or not to suffle the data')
args = parser.parse_args()

inputFile = args.input_script
dataset_dir = args.dataset_directory
outputFile = args.output
start_entry = args.start_entry
end_entry = args.end_entry
shuffle = args.shuffle

# have a list of lines of input file
with open(inputFile, 'r', encoding='UTF-8') as fhand:
    entries = fhand.readlines()

# selecting entries
entries = entries[start_entry:]

if end_entry > 0:
    entries = entries[:end_entry]

# insert audio file name at every entry of the list
for i, entry in enumerate(entries):
    entries[i] = f'{os.listdir(dataset_dir)[start_entry]},' + entry

    # if the sentence doesn't end with '။', appends it
    if not entry.rstrip().endswith("။"):
        entries[i] = entries[i].rstrip() + "။\n"

    start_entry += 1

# if shuffle is True, shuffle the entries
if shuffle:
    random.shuffle(entries)

# output a file that contains modified entries
with open(outputFile, 'w', encoding='UTF-8') as fhand:
    entries = ''.join(entries)
    fhand.write(entries)

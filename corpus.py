import argparse
import re

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='input csv file', required=True)
parser.add_argument('-o', '--output', type=str, default="corpus.txt", help='input file')
args = parser.parse_args()

inputFile = args.input
outputFile = args.output

# have a list of lines of input file
with open(inputFile, 'r', encoding='UTF-8') as fhand:
    entries = fhand.readlines()

# remove the file path, which is before the comma 
for i, entry in enumerate(entries):
    entries[i] = re.sub('\S+,', '', entry)

# output a file that contains modified entries
with open(outputFile, 'w', encoding='UTF-8') as fhand:
    entries = ''.join(entries)
    fhand.write(entries)

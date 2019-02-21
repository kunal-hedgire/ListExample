
import csv
import json

csvfile = open('data.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("Name","age","city")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

print('###################################################################################################')
'''

def read_large_file(file_handler, block_size=10000):
    block = []
    for line in file_handler:
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []

    # don't forget to yield the last block
    if block:
        yield block


with open('') as file_handler:
    for block in read_large_file(file_handler):
        print(block)
'''
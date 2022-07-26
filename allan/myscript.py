
import sys

import csv
import json
import regex as re
from camelcase import convert_camel

read_file = str(sys.argv[1])
output_file = str(sys.argv[2])

my_json = {}
with open(read_file, 'r') as fobj:
	reader = csv.DictReader(fobj)
	for row in reader:
		key = row['industry']
		my_json[key] = row

with open(output_file,'w') as fobj:
	fobj.write(json.dumps(my_json, indent=2))


file = open(output_file)
file_string = file.read()
pattern = r"\".+\":"

converter = lambda x: f"\"{convert_camel(x.group()[1:-2])}\":" 

file_string = re.sub(pattern, converter, file_string)

file.close()
with open(output_file, 'w') as fobj:
	fobj.write(file_string)
print(file_string[:500])
	
	
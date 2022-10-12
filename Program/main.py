from IntervalConverter import IntervalConverter
import sys
import json
import argparse

#Argument Parser part
# parser = argparse.ArgumentParser()
# parser.add_argument("input_filepath")
# parser.add_argument("output_filepath")
# parser.add_argument("--interval")
# parser.add_argument("--unit")
# args = parser.parse_args()
# input_filepath = args.input_filepath
# output_filepath = args.output_filepath
# output_interval = args.interval
# output_unit = args.unit

# #Json Reader part
# input_file = input_filepath
# json_file = open(input_file)
# json_data = json.load(json_file)
# name = json_data['name']
# interval_in_minutes = json_data['interval_in_minutes']
# unit = json_data['unit']
# data = json_data['data']

#for now use this
input_file = '/home/andreas/Documents/FH/Sem1/Software Development 1/Projects/Energy Profile Converter/Input_Files/example.json'
json_file = open(input_file)
json_data = json.load(json_file)
name = json_data['name']
interval_in_minutes = json_data['interval_in_minutes']
unit = json_data['unit']
data = json_data['data']

output_interval = 1
output_unit = 'kWh'
output_filepath = 'sample.json'

converter = IntervalConverter()
#Changer part
new_data = converter.minutes_15(data, interval_in_minutes, output_interval)
print(len(new_data))
#Json Writer part
dictionary = {
"name": name,
"interval_in_minutes": output_interval,
"unit": output_unit,
"data": new_data
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("/home/andreas/Documents/FH/Sem1/Software Development 1/Projects/Energy Profile Converter/OutputFiles/sample.json", "w") as outfile:
    outfile.write(json_object)


converter = IntervalConverter()
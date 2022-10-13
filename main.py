from Program.Interval_Converter import Interval_Converter
from Program.Terminal_Reader import Terminal_Reader
from Program.Unit_Converter import Unit_Converter
import sys
import json
import argparse

reader = Terminal_Reader()
interval_converter = Interval_Converter()
unit_converter = Unit_Converter()

#Changer part
data = interval_converter.convert_interval(reader.input_interval, reader.output_interval, reader.input_data)
new_data = unit_converter.convert_unit(reader.input_unit, reader.output_unit, data)

print(len(new_data))

#Json Writer part
dictionary = {
"name": reader.json_name,
"interval_in_minutes": reader.output_interval,
"unit": reader.output_unit,
"data": new_data
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("OutputFiles/{}".format(reader.output_filepath), "w") as outfile:
    outfile.write(json_object)
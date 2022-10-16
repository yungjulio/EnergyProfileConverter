import argparse
import json

class Terminal_Reader:
    def __init__(self):
        #Argument Parser part
        parser = argparse.ArgumentParser()
        parser.add_argument("input_filepath")
        parser.add_argument("output_filepath")
        parser.add_argument("--interval")
        parser.add_argument("--unit")

        args = parser.parse_args()

        input_filepath = args.input_filepath
        self.output_filepath = args.output_filepath
        self.output_interval = args.interval
        self.output_unit = args.unit

        #Json Reader part
        input_file = input_filepath
        json_file = open("Input_Files/{}".format(input_file))
        json_data = json.load(json_file)
        self.json_name = json_data['name']
        self.input_interval = json_data['interval_in_minutes']
        self.input_unit = json_data['unit']
        self.input_data = json_data['data']
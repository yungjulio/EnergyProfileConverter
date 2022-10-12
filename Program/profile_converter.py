import json
import sys
import argparse

class Main:
    def __init__(self):

        #Argument Parser part
        parser = argparse.ArgumentParser()
        parser.add_argument("input_filepath")
        parser.add_argument("output_filepath")
        parser.add_argument("--interval")
        parser.add_argument("--unit")
        args = parser.parse_args()
        input_filepath = args.input_filepath
        output_filepath = args.output_filepath
        output_interval = args.interval
        output_unit = args.unit

        #Json Reader part
        input_file = input_filepath
        json_file = open(input_file)
        json_data = json.load(json_file)
        name = json_data['name']
        interval_in_minutes = json_data['interval_in_minutes']
        unit = json_data['unit']
        data = json_data['data']

        #Changer part
        new_data = self.minutes_1(data, output_interval)

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
        with open("OutputFiles/{}".format(output_filepath), "w") as outfile:
            outfile.write(json_object)





    

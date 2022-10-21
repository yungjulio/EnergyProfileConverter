import argparse
import json

class Converter:
    def __init__(self):
        #Argument Parser part
        parser = argparse.ArgumentParser()
        parser.add_argument("input_filepath")
        parser.add_argument("output_filepath")
        parser.add_argument("--interval")
        parser.add_argument("--unit")

        args = parser.parse_args()

        self.output_filepath = args.output_filepath
        self.output_interval = args.interval
        self.output_unit = args.unit
        self.input_filepath = args.input_filepath

        self.input_name = None
        self.input_interval = None
        self.input_unit = None
        self.input_data = None

#--------------------------------------------------
    def convert(self):
        try : 
            json_file = open("Input_Files/{}".format(self.input_filepath))
        except OSError as e:
            return print("Unable to find File or Directory {}".format(self.input_filepath))

        json_data = json.load(json_file)
        self.input_name = json_data['name']
        self.input_interval = json_data['interval_in_minutes']
        self.input_unit = json_data['unit']
        self.input_data = json_data['data']


        data_in_base_unit = self.convert_data_to_base_unit(self.input_unit, self.input_data)

        try:
            data_in_required_unit = self.convert_data_to_required_unit(self.output_unit, data_in_base_unit)
        except:
            print("usage: profile_converter.py [-h] [--interval INTERVAL] [--unit UNIT] input_filepath output_filepath")
            return print("profile_converter.py: error: invalid value for [--unit]. Values must be: kWh, Wh, KJ, J")

        try:
            fully_converted_data = self.change_data_interval(int(self.input_interval), int(self.output_interval), data_in_required_unit)
        except:
            print("usage: profile_converter.py [-h] [--interval INTERVAL] [--unit UNIT] input_filepath output_filepath")
            return print("profile_converter.py: error: invalid value for [--interval]. Value must be of type int and one of the following values : 1, 15, 30, 60, 1440")

        return fully_converted_data

#--------------------------------------------------
    def convert_data_to_base_unit(self, input_unit, data):
        new_data = []
        print("input_unit = {}".format(input_unit))

        if input_unit == 'kWh':
            number = 1
        elif input_unit == 'Wh':
            number = 1/1000
        elif input_unit == 'J':
            number = 1/3600000
        elif input_unit == 'KJ':
            number = 1/3600
            
        for i in range(len(data)):
            new_data.append(data[i]*number)

        return new_data

#--------------------------------------------------
    def convert_data_to_required_unit(self, output_unit, data):
        if output_unit != 'kWh' and output_unit != 'Wh' and output_unit != 'KJ' and output_unit != 'J': raise;
        print("output_unit = {}".format(output_unit))
        new_data = []

        if output_unit == 'kWh':
            number = 1
        elif output_unit == 'Wh':
            number = 1000
        elif output_unit == 'J':
            number = 3600000
        elif output_unit == 'KJ':
            number = 3600
        
        for i in range(len(data)):
            new_data.append(data[i]*number)
        
        return new_data

#--------------------------------------------------
    def change_data_interval(self, input_interval, output_interval, data):
        if output_interval != 1 and output_interval != 15 and output_interval != 30 and \
            output_interval != 60 and output_interval != 1440:
            raise;

        print("input_interval = {}{}; output_interval = {}{}".format(type(input_interval), input_interval, type(output_interval), output_interval))
        print(input_interval < output_interval)
        #Case 1 = input_interval equals output_interval
        if input_interval == output_interval:
            return data
        
        #Case 2 = input_interval lower than output_interval => calculate average
        elif input_interval < output_interval:
            print("input_interval < output_interval")
            new_data = []
            decreaseFactor = int(output_interval/input_interval)
            new_data_size = len(data) / decreaseFactor
            print("new data size = {}".format(new_data_size))
            print("decreaseFactor = {}".format(decreaseFactor))
            start = 0
            end = decreaseFactor

            for i in range(0, int(new_data_size)):
                new_value = 0;
                for i in range(start, end):
                    new_value = new_value + data[i]
                
                new_data.append(new_value/decreaseFactor)
                start = end
                end = end + decreaseFactor
            
            return new_data

        #Case 3 = input_interval greater than output_interval => duplicate each value
        elif input_interval > output_interval:
            new_data = []
            increaseFactor = int(output_interval/input_interval)
            new_data_size = len(data) * increaseFactor
            for i in range(0, new_data_size):
                new_data.append(data[int(i/increaseFactor)])

            return new_data

#--------------------------------------------------
    def write_json(self):
        new_data = self.convert()

        dictionary = {
            "name": self.input_name,
            "interval_in_minutes": self.output_interval,
            "unit": self.output_unit,
            "data": new_data
            }

        # Serializing json
        json_object = json.dumps(dictionary, indent=4)

        # Writing to sample.json
        with open("OutputFiles/{}".format(self.output_filepath), "w") as outfile:
            outfile.write(json_object)
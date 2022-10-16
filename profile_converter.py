from Program.Converter import Converter

#reader = Terminal_Reader()
# interval_converter = Interval_Converter()
# unit_converter = Unit_Converter()

# #Changer part
# data = interval_converter.convert_interval(reader.input_interval, reader.output_interval, reader.input_data)
# new_data = unit_converter.convert_unit(reader.input_unit, reader.output_unit, data)

conv = Converter()

conv.write_json()

#print(len(new_data))

#Json Writer part
# dictionary = {
# "name": conv.json_name,
# "interval_in_minutes": conv.output_interval,
# "unit": conv.output_unit,
# "data": new_data
# }

# # Serializing json
# json_object = json.dumps(dictionary, indent=4)

# # Writing to sample.json
# with open("OutputFiles/{}".format(conv.output_filepath), "w") as outfile:
#     outfile.write(json_object)
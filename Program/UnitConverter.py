class UnitConverter:
    def convert_unit(self, input_unit, output_unit, data):
        #units = kWh, Wh, KJ, J
        # 1 kWh = 1000 Wh
        # 1 kWh = 3600 KJ
        # 1 Wh = 3.6 KJ
        # 1 Wh = 3600 J

        if (input_unit == output_unit):
            return data;
        else:
            new_data = []
            number = 0;

            if ((input_unit == "kWh" and output_unit == "Wh") or \
                (input_unit == "KJ" and output_unit == "J")):
                number = 1000
            elif ((input_unit == "Wh" and output_unit == "kWh") or \
                (input_unit == "J" and output_unit == "KJ")):
                number = 1/1000

            elif (input_unit == "Wh" and output_unit == "KJ"):
                number = 3.6
            elif ((input_unit == "Wh" and output_unit == "J") or \
                (input_unit == "kWh" and output_unit == "KJ")):
                number = 3600
            elif (input_unit == "kWh" and output_unit == "J"):
                number = 3600000
            elif (input_unit == "J" and output_unit == "kWh"):
                number = 1/3600000
            elif ((input_unit == "J" and output_unit == "Wh") or \
                (input_unit == "KJ" and output_unit == "kWh")):
                number = 1/3600
            elif (input_unit == "KJ" and output_unit == "Wh"):
                number = 1/3.6
            
            for i in range(0, len(data)):
                new_data.append(data[i]*number)

            return new_data
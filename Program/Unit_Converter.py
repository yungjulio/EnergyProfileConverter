from ast import match_case

class Unit_Converter:
    def convert_unit(self, input_unit, output_unit, data):
        #units = kWh, Wh, KJ, J
        # 1 kWh = 1000 Wh
        # 1 kWh = 3600 KJ
        # 1 Wh = 3.6 KJ
        # 1 Wh = 3600 J

        if (input_unit == output_unit):
            return data;
        
        new_data = []
        number = 0;
        #base unit => kWh
        if (input_unit != "kWh"):
            if input_unit == 'Wh':
                number = 1000
            elif input_unit == 'J':
                number = 3600000
            elif input_unit == 'KJ':
                number = 3600
            
            for i in range(len(data)):
                new_data.append(data[i]*number)
        
        if (output_unit != "kWh"):
            if output_unit == "Wh":
                number = 1/1000
            elif output_unit == "J":
                number = 1/3600000
            elif output_unit == "KJ":
                number = 1/3600
            
            for i in range(len(data)):
                new_data.append(data[i]*number)

        return new_data
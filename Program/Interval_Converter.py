class Interval_Converter:
    def convert_interval(self, param_input_interval, param_output_interval, input_data):
        #1440 mins
        input_interval = int(param_input_interval)
        output_interval = int(param_output_interval)
        output_data = []
        
        if input_interval != output_interval:
            if input_interval > output_interval:
                for value in input_data:
                    for i in range(0, input_interval):
                        output_data.append(value)
            else:
                new_value = 0
                steps = 0
                start = 0
                end = output_interval
                while(steps < len(input_data)/int(output_interval)):
                    for i in range(start, end):
                        new_value += input_data[i]

                    output_data.append(new_value/output_interval)
                    start = end
                    end += output_interval
                    steps += 1
                    new_value = 0
            return output_data
        else:
            return input_data
import json
import sys
import argparse
    
class IntervalConverter:
    def convert(self, data, old_interval_param, new_interval_param, old_unit_param, new_unit_param):
        #1440 mins
        old_interval = int(old_interval_param)
        new_interval = int(new_interval_param)
        new_data = []
        
        if old_interval > new_interval:
            for value in data:
                for i in range(0, old_interval):
                    new_data.append(value)
        else:
            new_value = 0.0
            steps = 0
            start = 0
            end = new_interval
            while(steps < len(data)/int(new_interval)):
                for i in range(start, end+1):
                    new_value += data[i]

                new_data.append(new_value)
            start = end+2
            steps += int(new_interval)
        return new_data
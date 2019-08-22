import numpy as np
import pandas as pd

def combine_days(frame_list):
    first = frame_list[0]
    
    if (len(frame_list) == 1):
        print_countries_extracted(first)
        return first
    
    for x in range(1, len(frame_list)):
        next = frame_list[x]
        frame = pd.concat([first, next], axis=1, sort=False)
        first = frame
    
    #provide a list of the countries pulled - so can just copy & paste
    #print_countries_extracted(frame)
    
    return frame.fillna(0)

def print_countries_extracted(prices_frame):
    print("These are the countries for which we were able to pull prices:\n")
    print(list(prices_frame.index))
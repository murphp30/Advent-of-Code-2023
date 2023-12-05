#!/usr/bin/env python

import numpy as np
import pdb

def generate_map(source_to_destination_map):
    # pdb.set_trace()
    source_to_destination_map  = np.array(source_to_destination_map, dtype=np.int64).T
    source_range_start = source_to_destination_map[1]
    destination_range_start = source_to_destination_map[0]
    range_len = source_to_destination_map[2]
    map_ranges = np.zeros((source_to_destination_map.shape[1],2,2))
    for i in range(source_to_destination_map.shape[1]):
        map_ranges[i][0] = [source_range_start[i], 
                            source_range_start[i]+range_len[i]-1]
        map_ranges[i][1] = [destination_range_start[i], 
                            destination_range_start[i]+range_len[i]-1]
    return map_ranges

def source_to_destination(source, source_to_destination_map):
    source_to_destination_map = generate_map(source_to_destination_map)
    destination = np.copy(source)
    for map_row in range(source_to_destination_map.shape[0]):
        # pdb.set_trace()
        source_range = (source >= source_to_destination_map[map_row][0,0]) & (source <= source_to_destination_map[map_row][0,1])
       
        source_loc = source[source_range] - source_to_destination_map[map_row][0,0] #np.argwhere(source_range == source)
        destination_range = source_to_destination_map[map_row][1,0] + source_loc #destination_range[source_loc][0][0]
        destination[source_range] = destination_range
        # print(destination)
    return destination

def seed_to_location(source, map_dict):
    for source_to_destination_map in map_dict.keys():
   
        source = source_to_destination(source, map_dict[source_to_destination_map])
        dest_name = source_to_destination_map.split()[0].split('-')[-1]
        print("{}: {}".format(dest_name,source))
    return source

input_file = "input.txt"
with open(input_file) as f:
    long_map_string = f.read()

seeds = long_map_string.split("\n\n")[0]
seeds = np.array(seeds.split()[1:], dtype=np.int64)
seed_range_lengths = seeds[1::2]
seeds = seeds[::2]

source_to_destination_maps = long_map_string.split("\n\n")[1:]

map_dict = {}
for source_to_destination_map in source_to_destination_maps:
    map_split = source_to_destination_map.split("\n")
    map_dict[map_split[0][:-1]] = [line.split() for line in map_split[1:]]

locations = np.array([])

for s in range(len(seeds)):
    seed_arr = np.arange(seeds[s], seeds[s] + seed_range_lengths[s] + 1)
    print("Input seed: {}".format(seed_arr))
    location = seed_to_location(seed_arr, map_dict)
    print("Seed {}: Location: {}".format(seed_arr, location))
    locations = np.concatenate((locations,location))
# print("Minimum location: {}".format(np.min(locations)))
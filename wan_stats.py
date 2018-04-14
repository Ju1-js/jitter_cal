import os
import re

path = 'C:/Users/James/Desktop/jitter_cal/output/out'
dir_with_file = {}
for file in os.listdir(path):
    x = 'C:/Users/James/Desktop/jitter_cal/output/out/{}'.format(file)
    dir_with_file[x] = file.split('-')[0]

s = {}

with open('C:/Users/James/Desktop/jitter_cal/ip_to_name.txt') as f:
    for l in f:
        (key, val) = l.split('\t')
        s[key] = val.strip()

d = dict([(v, k) for k, v in s.items()])


def stat(file):
    """takes full file path to ping output"""
    with open(file) as f:
        lis = [int(x.strip('=')) for x in f]
    #calculate jitter before file has been sorted, this will produce negative values
    jit = [j - i for i, j in zip(lis[:-1], lis[1:])]
    #remove negative values
    jit_no_neg = [abs(x) for x in jit]
    av_latency = sum(lis) / len(lis)
    average1 = sum(jit_no_neg)
    average2 = average1 / len(jit_no_neg)
    #prints average latency and jitter as first bits of output after title
    print("Averate Latency - {}".format(av_latency))
    print("Jitter - {}".format(average2))
    sort_list = sorted(lis)
    #returns sorted list of ping output
    return sort_list

#for loop to loop over dict with all file paths in dictionary


for dir in dir_with_file.keys():
    try:
        ip = dir_with_file.get(dir)
        bearer = d.get(ip)
        #print title of output
        print("{} - {}".format(bearer, ip))
        #call stat with full file path to ping output
        x = stat(dir)
        #takes the top and bottom 5 of the sorted output returned. For the highest and lowest pings
        min = x[:5]
        max = x[-5:]
        print("5 lowest - {}".format(min))
        print("5 highest - {}".format(max))
        loss = 1000 - len(x)
        print("drops out of 1000 - {}".format(loss))
        print("-------------")
    except ValueError:
        print("Error with file")
        print("-------------")
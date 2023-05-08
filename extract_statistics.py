import argparse 
import json 

parser = argparse.ArgumentParser(description='Extract statistics from a file')
parser.add_argument('--filename', help='the file to read')
parser.add_argument("--output_file", help="the file to write to")

args = parser.parse_args()

filename = args.filename
statistics = {
    "Total Energy": 0,
    "Total Cycles": 0,
    "MACs": 0,
    "Num of Parameters": 0,
    "Peak Activation Size": 0
}

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        for key in statistics.keys():
            if key in line:
                statistics[key] = float(line.split(":")[1].strip().split(" ")[0])


json.dump(statistics, open(args.output_file, 'w'))
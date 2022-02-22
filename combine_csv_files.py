import sys
import os
import time
import argparse
import configparser
from helper_functions import chomp, number_of_lines_in_file

'''
Notes:
   - Can bypass using headers on the commadline by using the --no_header=True argument
   - Assumes that the first non-empty CSV file read has the header
   - It skips CSV files that have less than 2 lines. Issues warning
   - It ignores non-CSV files (No warning)
   - When combining data, the last line in each file has no end of
     line (EOL) character. The scheme used here is to write the 
     header with no EOL, then append a EOL at the start of each new file. 
'''
start_time = time.time()

config = configparser.ConfigParser()
config.read('config.ini')

input_directory_path = config['files']['input_directory_path']
output_filename = config['files']['output_filename']

parser = argparse.ArgumentParser()
parser.add_argument('--no_header', help="The CSV header requirement that the file row of the each file contains the header (default set to True)", type=str, required=False)
args = parser.parse_args()
bypass_header=False

#Check the header. If True, set. All other cases, it is False
bypass_header=False
if args.no_header is not None:
    if args.no_header == 'True':
        bypass_header=True
    else:
        bypass_header=False
else:
    bypass_header=False

warning_count=0
warning_dictionary={}
start_dir=os.getcwd()

print ("\n=================================================")
print("Processing the following files in '", input_directory_path, "' :")

os.chdir(input_directory_path)
filepaths = [f for f in os.listdir(".") if f.endswith('.csv')]
print (filepaths)

if len(filepaths)==0:
    print("\n*** Critical Error: There are no csv files in directory '%s' ***\n" % input_directory_path)
    sys.exit(1)

text_file = open(filepaths[1], "r")
header=""

if bypass_header==False:
    header=chomp(text_file.readline())

    print ("\n-------------------------------------------------")
    print ("Obtaining header from file "+filepaths[1])
    print ("Header='"+header+"'")  # Note: No CRLF on purpose
    print ("-------------------------------------------------")

    if len(header)==0:
        print("\n*** Critical Error: No data in first file processed: {0}' ***\n".format(filepaths[1]))
        print("The first file processed is used to obtain the header.")
        print("You can do one of following things to continue:")
        print("  1. Fix the issue in the file (or move/delete the file to continue)")
        print("  2. Or use the --no_header=True option in the commandline to skip putting a header in the combined file\n")
        sys.exit(1)

os.chdir(start_dir)
first_file_read=False
with open(output_filename, "wb") as outfile:

    if first_file_read==False:
        # Work around so that if the output file is in a relative path, it will be in not be placed relative 
        # to the input directory by the earlier os.chdir(input_directory_path) call
        os.chdir(input_directory_path)
        first_file_read=True

    if bypass_header==True:
        print("Bypassing header in file due to passed --no_header argument")
    else:
        outfile.write(header.encode("UTF-8"))

    for fname in filepaths:  

        #print ("Processing "+fname)
        num_lines = number_of_lines_in_file(fname)

        if num_lines < 2:
            issue="has no rows of data"
            #print ("*** Warning: "+fname+ " has no rows of data (less than 2 rows in file)")
            warning_dictionary[fname]=issue
            continue;

        with open(fname, "rb") as f:
            is_first_line_in_file=True
            for x in f:
                if is_first_line_in_file:   
                    is_first_line_in_file=False
                    outfile.write(os.linesep.encode("UTF-8")) 
                else:
                    outfile.write(x)
try:
    startpos = output_filename.rindex("/")
except:
    try:
        startpos = output_filename.rindex("\\")
    except:
        startpos = -1

displayable_file_name=output_filename[startpos+1:]

if len(warning_dictionary)==0:
    print("\nFinished processing file '{0}' in {1:.3f} seconds with no issues\n".format(displayable_file_name,time.time() - start_time))
else:
    count_str=str(len(warning_dictionary))
    print("\nFinished processing file '{0}' in {1:.3f} seconds with {2} issues".format(displayable_file_name, time.time() - start_time, count_str))
    for key, value in warning_dictionary.items():
        print("    File '%s' %s" % (key, value))
    print("")

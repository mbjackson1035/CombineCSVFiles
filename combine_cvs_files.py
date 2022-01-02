import sys
import os
import time
import configparser
from helper_functions import chomp, number_of_lines_in_file

'''
Notes:
   - Assumes that the first non-empty CSV file read has the header
   - It skips CVS files that have less than 2 lines. Issues warning
   - It ignores non-CVS files (No warning)
   - When combining data, the last line in each file has no end of
     line (EOL) character. The scheme used here is to write the 
     header with no EOL, then append a EOL at the start of each new file. 
'''
start_time = time.time()

config = configparser.ConfigParser()
config.read('config.ini')

input_directory_path = config['files']['input_directory_path']
output_filename = config['files']['output_filename']

# Variable assignments
#input_directory_path = r"C:\Python\Dev\Test"
#output_filename = r"C:\Python\Dev\combined.cvs"

warning_count=0
warning_dictionary={}

print ("\n=================================================")
print("Processing the following files in '", input_directory_path, "' :")

os.chdir(input_directory_path)
filepaths = [f for f in os.listdir(".") if f.endswith('.csv')]
print (filepaths)

if len(filepaths)==0:
    print("\n*** Error: There are no cvs files in '%s' ***\n" % input_directory_path)
    sys.exit(1)

text_file = open(filepaths[1], "r")
header=chomp(text_file.readline())

with open(output_filename, "wb") as outfile:

    outfile.write(header.encode("UTF-8"))
    print ("\n-------------------------------------------------")
    print ("Obtaining header from file "+filepaths[1])
    print ("Header='"+header+"'")  # Note: No CRLF on purpose
    print ("-------------------------------------------------")

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


if len(warning_dictionary)==0:
    print("\nFinished processing in %s seconds with no issues" % "{:.3f}".format(time.time() - start_time))
else:
    count_str=str(len(warning_dictionary))
    print("\nFinished processing in %s seconds with %s issues" % ("{:.3f}".format(time.time() - start_time),count_str))
    for key, value in warning_dictionary.items():
        print("    File '%s' %s" % (key, value))





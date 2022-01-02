Usage: python combine_cvs_files.py

The source directory for the cvs files -and- the combined output filename are configured in the config.ini file.

First use suggestion: Just dive right in and run the following test ccenarios:

1. Initial test run 
    -This will error out because there are no files to process
    -Notice that no cvs is created
3. Test the happy case 
    -Copy all the files from ./Test/only_good_files into the ./Test directory
    -Run 
    -File combined.csv will be created
    -Inspect the combined file to find that it handles special character sets
3. Test good and bad files
    -Copy all files from ./Test/all_files
    -Run
    -Notice the warnings and inspect the created cvs files

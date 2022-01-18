Usage: python combine_cvs_files.py [--no_header=True]

There is a requirement that the first row of each file should contain a header (the default set to True)
Otherwise, run with the --no_header=True option

Note: The source directory for the cvs files -and- the combined output filename are configured in the config.ini file.

--------------------
First use suggestion
--------------------
Just dive right in and run the following test ccenarios without changing anything in the config.ini file:
1. Run an initial test
    -This will error out because there are no files to process in the default Test directory
    -Notice that no cvs file was created
3. Test the happy case 
    -Copy all the files from ./Test/only_good_files into the ./Test directory
    -Run 
    -File combined.csv will be created
    -Inspect the combined file to find that it handles special character sets
3. Test both good and bad files
    -Copy all files from ./Test/all_files
    -Run
    -Notice the warnings and inspect the created cvs file

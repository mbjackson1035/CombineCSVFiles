Usage: python combine_csv_files.py [--no_header=True]

There is a requirement that the first row of each file should contain the header. Otherwise, run with the --no_header=True option.

Note: The source directory for both the csv files -and- the combined output filename are configured in the config.ini file.

--------------------
Limitations  
--------------------
1. By default, this program assumes that all files the have the same headers. If the first csv 
   file processed is empty, the program will stop. This can be overridden.
2. All other csv files will be processed and will display necessary data warnings. Please check 
   these warnings before using the combined csv file.
3. This program will not delete or move any files. It is left for some other post process to 
   move/delete the input files as well as what to do with the resulting combined csv file. 
4. Re-running the program will overwrite the existing combined file. If this is unacceptable,
   either have some other process check for this before this program is run, or modify the code.
5. This programs does not report on non-csv files. They are just ignored. In the test data, several other
   file types are included, including one misspelled cvs instead of csv. 

--------------------
First use suggestion
--------------------
Just dive right in and run the following test ccenarios without changing anything in the config.ini file.
This project includes files for testing in the Test directory. 

Step 1. In the main directory, enter the following command: python combine_csv_files.py
    -This will error out because there are no files to process in the default Test directory  
    -Notice that no csv file was created  
Step 2. Test the happy case:  
    -Copy all the files from ./Test/only_good_files into the ./Test directory  
    -Run (python combine_csv_files.py)
    -File combined.csv will be created  
    -Inspect the combined file to find that it handles special character sets  
Step 3. Test both good and bad files:  
    -Copy all files from ./Test/all_files  
    -Delete combined.csv created from Step 2
    -Run (python combine_csv_files.py)
    -File Defunct_5.csv has no header. If the first file processed has no header, the program will stop
    -Delete or move Defunct_5.csv and rerun.
    -Notice the warnings and inspect the created csv file (combined.csv)
    -Note only csv files are processed. All other file types are ignored - including a file
     misspelled as cvs.
Step 4. Now run using your own files. Inside the config.ini file, change the values of the
    input directory (input_directory_path) and the combined file name (output_filename).
    
Usage: python combine_csv_files.py [--no_header=True]

There is a requirement that the first row of each file should contain the header. Otherwise, run with the --no_header=True option.

Note: The source directory for both the csv files -and- the combined output filename are configured in the config.ini file.

--------------------
First use suggestion
--------------------
Just dive right in and run the following test ccenarios without changing anything in the config.ini file.
This project includes files for testing in the Test directory. 

Note: This program will not delete or move any files. It is left for some other post process to 
      move/delete the input files as well as what to do with the combined csv file. 
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
    -Run (python combine_csv_files.py)
    -Notice the warnings and inspect the created csv file (combined.csv)
    -Note only csv files are processed
Step 4. Now run using your own files. Inside the config.ini file, change the values of the
    input directory (input_directory_path) and the combined file name (output_filename).
    
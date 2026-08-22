#!/bin/bash

# Merge the contents of three files into a temporary file
cat file1.txt file2.txt file3.txt > merged_file.txt

# Sort the contents of the merged file
sort merged_file.txt > sorted_file.txt

# Display the sorted contents page by page
less sorted_file.txt

# Clean up temporary files
rm merged_file.txt sorted_file.txt

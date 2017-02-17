# Algorithms
CSCI3104

The 4a script parses data from a target URL (in the example it used the census data, but any website organized by
last name with spaces to separate data types will work. It then iterates line by line to put into a subarray, where
each line has a 50% chance of being picked. Then it splits each line by spaces, and takes the names and puts them in 
a subarray. Then I declared another array with the lengths of each entry of the surname subarray. 

It assigns number values to each name, and adds them up in ASCII values, as where the homework specified A=1, B=2, etc., 
so the count shift accounts for that. Then the sums of every name are exported to 'out.txt'

From there the histogram.py file will take the out.txt and model the data for you.

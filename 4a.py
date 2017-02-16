# Authors Nic Williams && Rachel Platt && Roy De Jesus
# CSCI 3104 PS4
# Python Script for 4(a)
#
# Help received in data processing from these sources on StackOverflow:
# Dheeraj V.S., SimonJ, Hasan Ramezani, Ronakg, thiruvenkadam, UlfR
#
# Help received in data processing from:
# Nicolas Carson && Eric Wustrow (CU Boulder)
#
# Target URL used:
# http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last
#

import random, sys, urllib, numpy

def main():
    url = sys.argv[1] #type target URL in the command line
    data = urllib.urlopen(url) #parse data from URL
    input_data = [line for line in data if random.random() >= .5] #each line has 50% chance to be chosen
    surnames = [i.split(" ", 1)[0] for i in input_data] #split line arguments, extracting only the surnames
    surname_lengths = [len(i) for i in surnames] #declaring array with the sizes of each surname
    size = len(surnames)
    hash_bucket = []
    for i in range (0, size): #to iterate through the list
        count = 0
        count = surname_lengths[i] * 64 #since the sum will be in ASCII vals we need to shift by 64 for each letter
        sum_string = numpy.frombuffer(surnames[i], "uint8").sum() #sums all letters in ASCII values
        surnames[i] = sum_string - count #update list value to algorithm-specified value
        bucket = surnames[i] % 200 #assigning each string sum to a bucket
        hash_bucket.append(bucket) #creating data stream for bucket histogram
    with open('out.txt','w') as file:
        for item in hash_bucket:
            print>>file, item
main()

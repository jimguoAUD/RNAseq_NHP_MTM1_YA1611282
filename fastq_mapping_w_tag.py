 # execution: python fastq_mapping_w_tag.py subTag_ls, fastq_file, coverage.txt
from sys import argv
import re
from datetime import datetime


subTag_ls =  argv[1]
fastq_file = argv[2]
coverage = argv[3]
startTime = datetime.now()
matched_reads = []
unique_reads = []
my_dict = {}
with open (fastq_file, "r") as f:
    # read fastq file as lines of a list
    lines = f.readlines()
    # convert list to a dictionary with sequence name as key and sequence as the value for each pair. 
    for index, item in enumerate(lines):
        if index %4 ==0:
            my_dict[item] = lines[index+1]
        #print "my_dic[item] %s is lines[index+1] %s \n" %(item, my_dict[item])
   # iterate through the subTag library of predefined length
    with open (subTag_ls, 'r') as f:
        subTag_ls = f.readlines()
        for ls in subTag_ls:
            ls = ls.rstrip()
            if not ls.strip(): 
               ## search through the values of the dictionary for reads containing the tag sequence, add the names of these reads into a list "matched_reads"
               for key in my_dict:
                   if re.search(ls,my_dict[key],re.I):
                       matched_reads.append(key)
## remove duplicated reads from matched_reads by matching their names and place the unique reads in "unique_reads"
lines_seen = set() # holds lines already seen
for line in matched_reads:
   if line not in lines_seen: # not a duplicate
       unique_reads.append(line)
       lines_seen.add(line)
# print "unique_reads are %s\n" %unique_reads
print datetime.now()-startTime
with open (coverage, 'w') as f:
    f.write('%d\n' %len(unique_reads))

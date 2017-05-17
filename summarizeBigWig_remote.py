import pyBigWig as pw
import numpy as np
import sys


if len(sys.argv)<3:
    sys.exit("USAGE: python " + sys.argv[0] + " <BED or GFF file with regions> <output file>")


# Open a connection to 
bw = pw.open("http://hgdownload.cse.ucsc.edu/goldenPath/hg19/phastCons100way/hg19.100way.phastCons.bw")

infile = sys.argv[1]
outfile = sys.argv[2]
oF = open(outfile, "w")

if not infile.endswith("gff") and not infile.endswith("gff3"):
    sys.exit("The region file needs to be a GFF(3) file!")

counter = 0
for line in open(infile):
    if not line.startswith("chr"):
        continue
    counter += 1
    if counter % 20 == 0: sys.stderr.write("Scored " + str(counter) + " peptides\n")
    fields = line.strip().split()
    (chr, start, end, pept) = (fields[0], fields[3], fields[4], fields[8])
    if not pept.startswith("Parent="): continue
    pept = pept[7:] # Remove "Parent="

    try:
        values = bw.values(chr, int(start), int(end))
        max_val = np.max(values)
        mean_val = np.mean(values)
    except:
        print("Encountered error for line: " + line.strip())
        max_val = -1
        min_val = -1

    oF.write('\t'.join([chr, start, end, pept, str(max_val), str(mean_val)]) + '\n')

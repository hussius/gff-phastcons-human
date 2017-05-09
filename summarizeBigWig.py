import subprocess
import sys
import os

if len(sys.argv)<4:
    sys.exit("USAGE: python " + sys.argv[0] + " <BED or GFF file with regions> <path to bw files> <output file>")

#call('ls')

infile = sys.argv[1]
wigdir = sys.argv[2]
outfile = sys.argv[3]
oF = open(outfile, "w")

if infile.lower().endswith("bed"):
    informat = "bed"
elif infile.lower().endswith("gff") or infile.lower().endswith("gff3"):
    informat = "gff"
else:
    sys.exit("The region file needs to be a BED or GFF file!")

for line in open(infile):
    if not line.startswith("chr"):
        continue
    fields = line.strip().split()
    if informat=="bed":
        pass
        # Not implemented
    else:
        assert(informat=="gff")
        (chr, start, end, pept) = (fields[0], fields[3], fields[4], fields[8])
    if not pept.startswith("ID="): continue
    pept = pept[3:] # Remove "ID="
    cmd_str = 'bigWigSummary -type=max ' + wigdir + '/' + chr + '.bw ' + chr + ' ' + start + ' ' + end + ' 1'
    max_c=subprocess.check_output(cmd_str, shell=True).decode().strip()
    cmd_str2 = 'bigWigSummary -type=mean ' + wigdir + '/' + chr + '.bw ' + chr + ' ' + start + ' ' + end + ' 1'
    mean_c=subprocess.check_output(cmd_str2, shell=True).decode().strip()
    oF.write('\t'.join([chr, start, end, pept, max_c, mean_c]) + '\n')

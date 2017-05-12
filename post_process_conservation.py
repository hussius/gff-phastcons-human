import sys

# Collapse the max or mean by peptide ID/sequence (in column 4)

max_cons = {}
mean_cons_sum = {}
n_regions = {}
coord = {}

with open(sys.argv[1]) as infile:
    for line in infile:
        try:
            [chr,start,end,pep,maxcons_,meancons_] = line.strip().split()
            maxcons = float(maxcons_)
            meancons = float(meancons_)
        except:
            # Sometimes there are missing values for the conservation
            [chr,start,end,pep] = line.strip().split()
            maxcons = -1
            meancons = -1
        coord[pep]=chr+'\t'+start+'\t'+end
        if pep in n_regions: n_regions[pep] += 1
        else: n_regions[pep] = 1
        # Max
        if pep in max_cons:
            if maxcons > max_cons[pep]: 
                max_cons[pep] = maxcons
        else:
            max_cons[pep] = maxcons 
        # Mean
        if pep in mean_cons_sum:
            mean_cons_sum[pep] += meancons
        else:
            mean_cons_sum[pep] = meancons 
        
for p in sorted(max_cons):
    mean_mean_cons = mean_cons_sum[p] / n_regions[p]
    print(coord[p] + '\t' + p + '\t' + str(max_cons[p]) + '\t' + str(mean_mean_cons))

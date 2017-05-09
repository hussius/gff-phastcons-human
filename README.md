# gff-phastcons-human
Use the scripts here to calculate maximal and mean PhastCons46way scores for GFF files of human genomic regions.

## Usage

On the command line (e.g. in a terminal), run

`sh setup.sh`

This is only needed the first time. Afterwards, you can just use the `summarizeBigWig.py` Python script. The `setup.sh` script will:

- Attempt to install the UCSC wigToBigWig and bigWigSummary executables via BioConda
- Create a directory called wigFiles to where PhastCons wig files will be downloaded and converted to bigWig
- Download the PhastCons wig files, extract them, and convert them to bigWig.

After this is finished, you can use the `summarizeBigWig.py` Python script to summarize the conservation scores per regions with a command like this (which uses the gff3 file in this GitHiub repo)

`python summarizeBigWig.py A431_novel_peptides.2017.gff3 wigFiles out_A431.txt`

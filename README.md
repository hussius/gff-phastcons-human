# gff-phastcons-human
Use the scripts here to calculate maximal and mean PhastCons46way scores for GFF files of human genomic regions.

# Usage

## Scoring without downloading files (recommended)

If you want to score your regions without downloading anything, which is convenient, you can use the `summarizeBigWig_remote.py` script, which is based on the [nice pyBigWig library](https://github.com/dpryan79/pyBigWig) by Devon Ryan. This script works by opening a remote connection to `http://hgdownload.cse.ucsc.edu/goldenPath/hg19/phastCons100way/hg19.100way.phastCons.bw`. Note that this is the 100-way PhastCons, as opposed to the recipe below which uses 46-way. This is because we have only found a whole-genome bw file for the 100-way version.

In that case, you have to install the pyBigWig library by, for example, BioConda.

`conda install -c bioconda pybigwig`

You may want to do it in a conda virtual environment. If the above does not work, please refer to [pyBigWig's GitHub page](https://github.com/dpryan79/pyBigWig).

Then, you can score entries in a GFF file with a command like this (using the example file provided in this repository):

`python summarizeBigWig_remote.py A431_novel_peptides.2017.gff3 out2_A431.txt`

The script will take a while to run, but it prints output that hopefully gives an idea about how long it will take.

## Scoring with downloaded files

In some scenarios (maybe the remote bigWig file moves or you have problems installing pyBigWig for some reason) you can use the following recipe to do the scoring based on downloading wig files. 

On the command line (e.g. in a terminal), run

`sh setup.sh`

This is only needed the first time. Afterwards, you can just use the `summarizeBigWig.py` Python script. The `setup.sh` script will:

- Attempt to install the UCSC wigToBigWig and bigWigSummary executables via BioConda
- Create a directory called wigFiles to where PhastCons wig files will be downloaded and converted to bigWig (note: by default, 46-way files will be used, but you can change the path to download [100-way files](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/phastCons100way/hg19.100way.phastCons/) instead)
- Download the PhastCons wig files, extract them, and convert them to bigWig.

After this is finished, you can use the `summarizeBigWig.py` Python script to summarize the conservation scores per regions with a command like this (which uses the gff3 file in this GitHub repo)

`python summarizeBigWig.py A431_novel_peptides.2017.gff3 wigFiles out_A431.txt`

# Post-processing

In addition, if you have multiple entries per ID, you can collapse these by using another Python script:

`python post_process_conservation.py out_A431.txt > collapsed_A431.txt`



conda install -c bioconda ucsc-wigtobigwig
conda install -c bioconda ucsc-bigwigsummary

mkdir wigFiles
cd wigFiles

for i in {1..22} X Y
do
wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/phastCons46way/vertebrate/chr${i}.phastCons46way.wigFix.gz
done

wget https://raw.githubusercontent.com/arq5x/bedtools/master/genomes/human.hg19.genome

for i in {1..22} X Y
do
gunzip chr${i}.phastCons46way.wigFix.gz
wigToBigWig -clip chr${i}.phastCons46way.wigFix human.hg19.genome chr${i}.bw
rm chr${i}.phastCons46way.wigFix;
done
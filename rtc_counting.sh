#!/bin/bash
set -e -x -o pipefail

dx download "$fastq_gz" -o reads.fq.gz
dx download "$fasta" -o subTag_ls.fasta
output_name="${fastq_gz_prefix}_${fasta_prefix}_RTC_count.txt"

gunzip reads.fq.gz 
mkdir -p out/direct_map
touch matched_sequence.txt
while read p; do
	if grep $p reads.fq; then
			grep $p reads.fq >> matched_sequence.txt
	fi
done < subTag_ls.fasta

sort -u matched_sequence.txt |wc -l >$output_name

mv $output_name out/direct_map/
dx-upload-all-outputs

import subprocess
 
# samples correspond to Het_1, Het_2, Imm_1, Imm_2
sra_numbers = [
     "SRR17060816","SRR17060817","SRR17060818","SRR17060819","SRR17060820","SRR17060821","SRR17060822","SRR17060823","SRR17060824",
"SRR17060825","SRR17060826","SRR17060827","SRR17060828","SRR17060829","SRR17060830","SRR17060831","SRR17060832","SRR17060833","SRR17060834",
"SRR17060835","SRR17060836","SRR17060837","SRR17060838","SRR17060839","SRR17060840","SRR17060841","SRR17060842","SRR17060843","SRR17060844"]

# this will download the .sra files to ~/ncbi/public/sra/ (will create directory if not present)
for sra_id in sra_numbers:
    print ("Currently downloading: " + sra_id)
    prefetch = "prefetch " + sra_id
    print ("The command used was: " + prefetch)
    subprocess.call(prefetch, shell=True)

# this will extract the .sra files from above into a folder named 'fastq'
for sra_id in sra_numbers:
    print ("Generating fastq for: " + sra_id)
    fastq_dump = "fastq-dump --outdir fastq --gzip --skip-technical  --readids --read-filter pass --dumpbase --split-3 --clip ~/ncbi/public/sra/" + sra_id + ".sra"
    print ("The command used was: " + fastq_dump)
    subprocess.call(fastq_dump, shell=True)

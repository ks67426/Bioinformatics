# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:43:55 2021

@author: LocalUser
"""

from Bio.Blast import NCBIWWW
fasta_string = open("seq.fa").read()
result_handle = NCBIWWW.qblast("blastn","nt", fasta_string)
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)
#%%
len(blast_record.alignments)
#%%
e = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < e :
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
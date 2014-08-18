from Bio import Entrez
from Bio import SeqIO
import requests

UNIPROT_URL = "http://www.uniprot.org/uniprot/{0}.fasta"

def uniprot(uniprot_ids):
    """Fetches each uniprot id and creates a file ready to upload in FASTA"""
    uniprot_ids = uniprot_ids.split(" ")
    for i, uniprot_id in enumerate(uniprot_ids):
        fasta = requests.get(UNIPROT_URL.format(uniprot_id)).text
        with open('SWAT{0}.fasta'.format(i), 'w') as f:
            f.write(fasta)

if __name__ == '__main__':
    uniprot("B3ET80 Q78PG9")

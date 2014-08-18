from Bio import Entrez
from Bio import SeqIO

def genbank(*genbank_ids):
    """Fetches each genbank id and creates a file ready to upload in FASTA"""
    Entrez.email = "adelq@sas.upenn.edu"

    for i, genbank_id in enumerate(genbank_ids):
        handle = Entrez.efetch(db="nucleotide", id=genbank_id, rettype="fasta")
        fasta = handle.read()
        with open('NEED{0}.fasta'.format(i), 'w') as f:
            f.write(fasta)

if __name__ == '__main__':
    genbank("JX205496.1", "JX469991.1")

from Bio import SeqIO
from collections import defaultdict
import multiprocessing as mp
import sys
import dendropy

n = 447
dataset_path = '/biological_mammalian/424genes/'
outgroup = 'GAL'
new_root = 'ORN'

if __name__ == '__main__':
    tns = dendropy.TaxonNamespace()
    t1 = dendropy.Tree.get(path='astralv5.7.8.tre', schema='newick', taxon_namespace=tns)
    print([t.label for t in tns])
    print(len([t.label for t in tns]))
    t1.prune_taxa_with_labels(["GAL"])
    new_outgroup = t1.find_node_with_taxon_label(new_root)
    t1.reroot_at_edge(new_outgroup.edge, update_bipartitions=False)
    with open('astralv5.7.8-no-GAL-rerooted-ORN.tre', 'w') as f:
        f.write(str(t1) + ';\n')


    sequence_map = defaultdict(str)
    for i in range(1, n+1):
        try:
            gene_alignment = dataset_path + str(i) + '/' + str(i) + '.fasta'
            for sequence in SeqIO.parse(gene_alignment, "fasta"):
                sequence_map[sequence.name.upper()] += str(sequence.seq)
        except Exception as e:
            print(e)
    with open("concat-align-no-GAL.fasta", 'w') as fp:
        for key in sorted(sequence_map.keys()):
            if key != outgroup:
                fp.write('>' + key + '\n')
                fp.write(sequence_map[key] + '\n')
    print([k for k in sequence_map])
    print(len([k for k in sequence_map]))

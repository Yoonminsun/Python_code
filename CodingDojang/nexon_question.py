num_set = set(range(5000))
gene=0
gene_set=set()
for i in range(5000):
    for j in str(i):
        gene+=int(j)
    gene+=i
    gene_set.add(gene)
    gene=0

print(sum(num_set - gene_set))




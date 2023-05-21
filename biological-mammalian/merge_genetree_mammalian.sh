# !/bin/bash

touch genetrees.tre

for i in {1..447}
do
  cat 424genes/${i}/raxmlboot.gtrgamma/RAxML_bipartitions.final.f200 >> genetrees.tre
done

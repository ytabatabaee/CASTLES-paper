## CASTLES Datasets

This repository contains the datasets used in the following paper:

- Y. Tabatabaee, C. Zhang, T. Warnow, S. Mirarab, Phylogenomic branch length estimation using quartets, Bioinformatics, Volume 39, Issue Supplement_1, June 2023, Pages i185–i193, https://doi.org/10.1093/bioinformatics/btad221

For experiments in this study, we studied a collection of simulated and biological datasets with incomplete lineage sorting (ILS). We generated a new quartet dataset and regenerated species trees with substitution-unit branch lengths for previously published datasets from [Zhang et. al. (2018)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2129-y) and [Mai et. al. (2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182238). We also analyzed the mammalian biological dataset from [Song et. al. (2012)](https://www.pnas.org/doi/full/10.1073/pnas.1211733109).

All datasets can be accessed from [this](https://drive.google.com/drive/folders/1Crzn_H-8m9WWr8WuZ_E2DQx0Cx2QXQJF?usp=share_link) Google Drive link.

### Simulated datasets

**Quartet simulations**

This dataset has six different model conditions that differ in the level of ILS (by varying population size) and varying rate heterogeneity multipliers, each with 200 replicates. The model conditions start from a strict molecular clock with no rate variation (i.e. Homogeneous, `no_variation`) and becomes successively more complex. Next, we add rate variations across species tree branches only (-hs option, `only_hs`), creating a model (Sp) akin to MSC + Substitution mentioned in the paper. We then create models that have rate variation only across genes but not species (Loc using -hl, `only_hl`) and both across species and across genes (Sp, Loc using -hs -hl, `hs_hl`). Finally, we add rate variations specific to each branch of each gene tree (Sp, Loc, Sp/Loc: -hs -hl -hg, `hs_hl_hg`), which creates heterotachy. The final condition (`hs_hl_hg_highr`) has similar rate variations to `hs_hl_hg` but with a smaller population size and therefore higher level of ILS. Raw dataset is available in `quartet_simulations.zip` and includes species trees, true gene trees and other SimPhy outputs. Results and intermediate data from the experiments in the paper are available in `quartets_results.tar.gz`.

Below is a description of files in each directory.
- `s_tree.trees`: true species tree in substitution units
- `truegenetrees`: true gene trees in substitution units
- `ultrametric-genetrees.tre`: ultrametric gene trees
- `s_tree.ralpha`: mutation rates for species tree branches in pre-order traversal
- `g_trees_ralpha.txt`: mutation rates for gene tree branches in pre-order traversal
- `l_trees.trees`: locus trees in generation units
- `ad.txt`: average RF distance between the model species tree and true gene trees
- `castles_truegenetrees_s_tree.trees`: true species tree furnished with CASTLES SU branch lengths
- `patristic_[MODE]_truegenetrees.mat`: patristic distance matrix calculated using minimum (`min`), average (`avg`) or all (`all`) pairwise distances
- `erable_patristic_all_truegenetrees_s_tree.trees.derooted.length.nwk`: true species tree furnished with ERaBLE SU branch lengths
- `fastme_BalLS_patristic_avg_truegenetrees_s_tree.trees.derooted`: true species tree furnished with FastME SU branch lengths with average distances
- `fastme_BalLS_patristic_min_truegenetrees_s_tree.trees.derooted`: true species tree furnished with FastME SU branch lengths with minimum distances

**30-taxon simulations**

This dataset has six model conditions with varying levels of deviation from the molecular clock and inclusion of an outgroup, each with 100 replicates. The model conditions are specified as `outgroup.[has-OG].species.[DEV].genes.[DEV]` where `[has-OG]` is 1 when the dataset has an outgroup and 0 otherwise, and `[DEV]` shows the level of deviation from the clock (parameter α of the gamma distribution) that is set to 5 (low), 1.5 (medium), or 0.15 (high). Original dataset is from [Mai at al. (2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182238) and available at [https://uym2.github.io/MinVar-Rooting/](https://uym2.github.io/MinVar-Rooting/). Species trees with SU branch lengths are available in `MVRoot_SU.tar.gz` and results and intermediate data from the experiments in the paper are available in `MVRoot_results.tar.xz`.

Below is a description of files in each directory.
- `s_tree.trees`: true species tree in substitution units
- `s_tree.ralpha`: mutation rates for species tree branches in pre-order traversal
- `g_trees_ralpha.txt`: mutation rates for gene tree branches in pre-order traversal
- `truegenetrees`: true gene trees in substitution units
- `estimatedgenetre.gtr`: estimated gene trees
- `ad.txt`: average RF distance between the model species tree and true gene trees
- `gtee_gtr.txt`: average RF distance between true and estimated gene trees
- `all-genes.phylip` and `concat_align.fasta`: concatenation of all gene alignments
- `castles_truegenetrees_s_tree.trees`: true species tree furnished with CASTLES SU branch lengths run on true gene trees
- `castles_estimatedgenetre.gtr_s_tree.trees`: true species tree furnished with CASTLES SU branch lengths run on estimated gene trees
- `erable_patristic_all_truegenetrees_s_tree.trees.derooted.length.nwk`: true species tree furnished with ERaBLE SU branch lengths on true gene trees
- `erable_patristic_all_estimatedgenetre.gtr_s_tree.trees.derooted.length.nwk`: true species tree furnished with ERaBLE SU branch lengths on estimated gene trees
- `fastme_BalLS_patristic_[MODE]_truegenetrees_s_tree.trees.derooted`: true species tree furnished with FastME SU branch lengths with minimum or average distances run on true gene trees
- `fastme_BalLS_patristic_[MODE]_estimatedgenetre.gtr_s_tree.trees.derooted`: true species tree furnished with FastME SU branch lengths with minimum or average distances run on estimated gene trees
- `patristic_[MODE]_truegenetrees.mat`: patristic distance matrix calculated using minimum (`min`), average (`avg`) or all (`all`) pairwise distances for true gene trees
- `patristic_[MODE]_estimatedgenetre.gtr.mat`: patristic distance matrix calculated using minimum (`min`), average (`avg`) or all (`all`) pairwise distances for estimated gene trees
- `RAxML_result.concat_align_s_tree.trees`: true species tree furnished with RAxML SU branch lengths

**101-taxon simulations**

This dataset has four model conditions with varying sequence lengths (1600bp, 800bp, 400bp, 200bp) corresponding to different levels of gene tree estimation error (23%, 31%, 42%, and 55%), each with 50 replicates. The original dataset is from [Zhang et. al. (2018)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2129-y) and available at [https://gitlab.com/esayyari/ASTRALIII/](https://gitlab.com/esayyari/ASTRALIII/). Species trees with SU branch lengths are available in `ASTRALIII_SU.tar.gz`. Results and intermediate data from the experiments in the paper are in `ASTRALIII_SU_results.tar.xz`. Below is a description of files in each directory.

- `s_tree.trees`: true species tree in substitution units
- `s_tree.ralpha`: mutation rates for species tree branches in pre-order traversal
- `g_trees_ralpha.txt`: mutation rates for gene tree branches in pre-order traversal
- `truegenetrees`: true gene trees in substitution units
- `fasttree_genetrees_[seq-len]_non`: gene trees estimated using FastTree2 from alignments with length [seq-len]bp
- `erable_patristic_all_fasttree_genetrees_[seq-len]_non_s_tree.trees.derooted.length.nwk`: true species tree furnished with ERaBLE SU branch lengths on gene trees estimated from alignments with length [seq-len]bp
- `patristic_[MODE]_fasttree_genetrees_[seq-len]_non.mat`: patristic distance matrix calculated using minimum (`min`), average (`avg`) or all (`all`) pairwise distances for gene trees estimated from alignments with length [seq-len]bp
- `concat_for_fasttree_[seq-len].fasta` or `all-genes_for_fasttree.phylip`: concatenation of all gene alignments with length [seq-len]bp
- `RAxML_result.concat_for_fasttree_[seq-len]_s_tree.trees`: true species tree furnished with RAxML SU branch lengths from concatenation of alignments with length [seq-len]bp
- `castles_fasttree_genetrees_[seq-len]_non_s_tree.trees`: true species tree furnished with CASTLES SU branch lengths run on gene trees estimated from alignments with length [seq-len]bp
- `fastme_BalLS_patristic_[MODE]_fasttree_genetrees_[seq-len]_non_s_tree.trees.derooted`: true species tree furnished with FastME SU branch lengths with minimum or average distances run on gene trees estimated from alignments with length [seq-len]bp

### Biological dataset
The preprocessed mammalian dataset (in which genes with mismatching names are removed) is available at https://drive.google.com/drive/folders/0B0lcoFFOYQf8SlZvQmlOSkFJaEE?resourcekey=0-ClOa-cr-C3TeBWQlQuxmZw and includes an estimated ASTRAL species tree, gene trees and alignments. The files generated for our analysis are available in `biological-mammalian.tar.gz`. Below is a description of files in each directory.

- `genetrees.tre`: gene trees after filtering
- `concat-align.fasta`: concatenated alignment of all filtered genes
- `astralv5.7.8.tre`: main species tree with CU branch lengths estimated using ASTRAL
- `RAxML_log.no_GAL.tre`: ASTRAL species tree furnished with RAxML SU branch lengths after removing the outgroup Chicken (`GAL`)
- `castles_rooted.tre`: ASTRAL species tree furnished with CASTLES SU branch lengths after removing the outgroup Chicken (`GAL`)
- `fastme_[MODE].tre`: ASTRAL species tree furnished with FastME SU branch lengths with minimum or average distances
- `erable.tre.length.nwk`: ASTRAL species tree furnished with ERaBLE SU branch lengths
- `patristic_[MODE].mat`: patristic distance matrix calculated using minimum (`min`), average (`avg`) or all (`all`) pairwise distances for gene trees
- `mammals-namemap.txt`: name mapping for taxa
- `mammalian-trees.nexus`: FigTree nexus file comparing CASTLES and Concatenation branch lengths

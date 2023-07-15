## CASTLES Datasets

This repository contains the datasets and scripts used in the following paper:

- Y. Tabatabaee, C. Zhang, T. Warnow, S. Mirarab, Phylogenomic branch length estimation using quartets, Bioinformatics, Volume 39, Issue Supplement_1, June 2023, Pages i185–i193, https://doi.org/10.1093/bioinformatics/btad221

For experiments in this study, we generated a new quartet dataset and regenerated species trees with substitution-unit branch lengths for previously published datasets from [Zhang et. al. (2018)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2129-y) and [Mai et. al. (2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182238). We also analyzed the mammalian biological dataset from [Song et. al. (2012)](https://www.pnas.org/doi/full/10.1073/pnas.1211733109).

All datasets can be accessed from [this](https://drive.google.com/drive/folders/1Crzn_H-8m9WWr8WuZ_E2DQx0Cx2QXQJF?usp=share_link) Google Drive link.

### Simulated datasets

**Quartet simulations**

- Raw dataset is available in [quartet_simulations.zip](https://drive.google.com/file/d/1fippeUuJi0itJOYSSIlsd7D4hz6tl6aB/view?usp=share_link) and includes species trees, true gene trees and other SimPhy outputs.
- Species trees with SU branch lengths are also available in this repository in [simulated-data/quartets](https://github.com/ytabatabaee/CASTLES-paper/tree/main/simulated-data/quartets).
- Results and intermediate data from the experiments in the paper are available in [quartets_results.tar.gz](https://drive.google.com/file/d/1EZC5WfN49ee8K-DJxoPdGFVUiQSh_fjm/view?usp=share_link).

**30-taxon MVRoot ILS simulations**
- Original dataset is from [Mai at al. (2017)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182238) and available at [https://uym2.github.io/MinVar-Rooting/](https://uym2.github.io/MinVar-Rooting/).
- Species trees with SU branch lengths are available in [MVRoot_SU.tar.gz](https://drive.google.com/file/d/1YiACTW3HIXyIXeBJrHxstp6d6bKk9E6V/view?usp=share_link) and also here in [simulated-data/MVroot](https://github.com/ytabatabaee/CASTLES-paper/tree/main/simulated-data/MVroot).
- Results and intermediate data from the experiments in the paper are available in [MVRoot_results.tar.xz](https://drive.google.com/file/d/1FEfksJt743C1Hzy8NpaDLSwhbvIlXwNb/view?usp=share_link).

**101-taxon ASTRALIII ILS simulations**
- Original dataset is from [Zhang et. al. (2018)](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2129-y) and available at [https://gitlab.com/esayyari/ASTRALIII/](https://gitlab.com/esayyari/ASTRALIII/).
- Species trees with SU branch lengths are available in [ASTRALIII_SU.tar.gz](https://drive.google.com/file/d/1Icy9Mg0KhCB-1U0Fp7KPBL4QVF2UI_Cx/view?usp=share_link) and also in [simulated-data/ASTRALIII](https://github.com/ytabatabaee/CASTLES-paper/tree/main/simulated-data/ASTRALIII).
- Results and intermediate data from the experiments in the paper are in [ASTRALIII_SU_results.tar.xz](https://drive.google.com/file/d/13ZrOhOliKCEpXebBlMg01WlRTGmnCXza/view?usp=share_link).

### Biological dataset
The preprocessed mammalian dataset (in which genes with mismatching names are removed) is available [here](https://drive.google.com/drive/folders/0B0lcoFFOYQf8SlZvQmlOSkFJaEE?resourcekey=0-ClOa-cr-C3TeBWQlQuxmZw) and includes an estimated ASTRAL species tree, gene trees and alignments. The files generated for our analysis are available in [biological-mammalian](https://github.com/ytabatabaee/CASTLES-paper/tree/main/biological-mammalian).

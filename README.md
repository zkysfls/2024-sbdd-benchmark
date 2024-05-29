# Structure-based Drug Design Benchmark: Do 3D Methods Really Dominate?

---

[![GitHub Repo stars](https://img.shields.io/github/stars/zkysfls/2024-sbdd-benchmark)](https://github.com/zkysfls/2024-sbdd-benchmark/stargazers)
[![GitHub Repo forks](https://img.shields.io/github/forks/zkysfls/2024-sbdd-benchmark)](https://github.com/zkysfls/2024-sbdd-benchmark/network/members)


This repository hosts an open-source benchmark for Structure-based Drug Design, to facilitate the transparent and reproducible evaluation of algorithmic advances in molecular optimization. This repository supports 16 Structure-based Drug Design algorithms on 7 tasks.

## Installation 

There are two environments: Test Env and TDC Env. Test Env is used to run these models: 3DSBDD, Pocket2mol, PockFlow, ResGen and Autogrow4.
TDC Env is used to run the rest of the models and evaluate all the models' generated molecules.

```bash
conda env create -f environment_TestEnv.yml
conda activate TestEnv2
```


<!-- pip install guacamol  -->
<!-- pip install networkx  -->
<!-- pip install joblib  -->



## 16 Methods


Based the ML methodologies, all the methods are categorized into: 
* virtual screening
    * **screening** randomly search ZINC database. 
* GA (genetic algorithm)
    * **graph\_ga** based on molecular graph.
    * **smiles\_ga** based on SMILES
    * **Autogrow4** based on SMILES 
* VAE (variational auto-encoder)
    * **smiles\_vae** based on SMILES
    * **selfies\_vae** based on SELFIES
* RL (reinforcement learning)
    * **reinvent** 
    * **moldqn** 
* HC (hill climbing)
    * **smiles\_lstm\_hc** is SMILES-level HC. 
    * **mimosa** is graph-level HC
* gradient (gradient ascent)
    * **dst** is based molecular graph. 
    * **pasithea** is based on SELFIES. 
* Auto-regressive
    * **3DSBDD**  
    * **Pocket2mol** 
    * **PocketFlow**
    * **ResGen** 

`time` is the average rough clock time for a single run in our benchmark and do not involve the time for pretraining and data preprocess. 
We have processed the data, pretrained the model. Both are available in the repository. 

|                  `Model`                                                                                        | `Dimension` | `Generated Number `   | `requires_gpu` |
|-----------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------|---------|
| **[3DSBDD](https://pubs.rsc.org/en/content/articlehtml/2021/sc/d0sc06805e)**                              | -      |  -          |    yes     |
| **[AUTOGROW](https://pubs.rsc.org/en/content/articlelanding/2019/sc/c8sc05372c)**                        | -     |  -          |   yes    |
| **[POCKET2MOL](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                       | -     | -          |    yes     |
| **[POCKETFLOW](https://chemrxiv.org/engage/chemrxiv/article-details/60c753f00f50db6830397c37)**               | -    | -          |    yes    |
| **[RESGEN](https://openreview.net/forum?id=H1lmyRNFvr)**                                             | -    |  -          |    yes     |
| **[DST](https://pubs.rsc.org/en/content/articlelanding/2019/sc/c8sc05372c)**                      | -       |  -          |    no     |
| **[GRAPH GA](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                 | -     | -          |    yes    |
| **[MIMOSA](https://arxiv.org/pdf/2212.01385.pdf)**                                                   | -     |  -          |    yes     |
| **[MOLDQN](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                | -    |  -          |    yes    |
| **[PASITHEA](https://arxiv.org/pdf/1610.02415.pdf)**                                                   | -     |  -          |    yes     |
| **[REINVENT](https://arxiv.org/pdf/1610.02415.pdf)**                                                  | -    |  -          |    yes     |
| **[SCREENING](https://arxiv.org/pdf/1802.04364.pdf)**                                                       | -   | -          |    yes     |
| **[SELFIES VAE BO](https://openreview.net/forum?id=gS3XMun4cl_)**                                                   | -   | -          |    yes     |
| **[SMILES GA](https://arxiv.org/abs/1704.07555)**                                                          | -     |  -          |    yes    |
| **[SMILES LSTM HC](https://arxiv.org/pdf/2310.05365)**                                             | -     | -          |    yes    |
| **[SMILES VAE BO](https://arxiv.org/abs/1704.07555)**                                                 | -    | -          |    yes     |







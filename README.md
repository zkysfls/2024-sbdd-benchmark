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
| **[3DSBDD](https://arxiv.org/abs/2203.10446)**                              | 3D      |  771          |    yes     |
| **[AutoGrow4](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00429-4)**                        | 2D     |  1233          |   yes    |
| **[Pocket2mol](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                       | 3D     | 928          |    yes     |
| **[PocketFlow](https://arxiv.org/abs/2205.07249)**               | 3D    | 1000          |    yes    |
| **[RenGen](https://www.nature.com/articles/s42256-023-00712-7)**                                             | 3D    |  631          |    yes     |
| **[DST](https://arxiv.org/abs/2109.10469)**                      | 2D       |  1001          |    yes     |
| **[Graph GA](https://pubs.rsc.org/en/content/articlelanding/2019/sc/c8sc05372c)**                                 | 2D     | 643          |    yes    |
| **[MIMOSA](https://arxiv.org/abs/2010.02318)**                                                   | 2D     |  1001          |    yes     |
| **[MolDQN](https://arxiv.org/abs/1810.08678)**                                | 2D    |  501          |    yes    |
| **[Pasithea](https://arxiv.org/abs/2012.09712)**                                                   | 1D     |  914          |    yes     |
| **[REINVENT](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0235-x)**                                                  | 1D    |  100          |    yes     |
| **[SCREENING](https://arxiv.org/pdf/1802.04364.pdf)**                                                       | -   | 1000          |    yes     |
| **[SELFIES-VAE-BO](https://arxiv.org/abs/1610.02415)**                                                   | 1D   | 200          |    yes     |
| **[SMILES-GA](https://arxiv.org/abs/1804.02134)**                                                          | 1D     |  584          |    yes    |
| **[SMILES-LSTM-HC](https://arxiv.org/abs/1811.09621)**                                             | 1D     | 501          |    yes    |
| **[SMILES-VAE-BO](https://arxiv.org/abs/1610.02415)**                                                 | 1D    | 200          |    yes     |







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

|                  `Models`                                                                                        | `Dimension` | `Generated Number `   | `requires_gpu` |
|-----------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------|---------|
| **screening**                                                                                             | -          | -                                             |     no     |
| **[molpal](https://pubs.rsc.org/en/content/articlehtml/2021/sc/d0sc06805e)**                              | -          | ray, tensorflow, ConfigArgParse, pytorch-lightning       |    no     |
| **[graph\_ga](https://pubs.rsc.org/en/content/articlelanding/2019/sc/c8sc05372c)**                        | fragment   | joblib                                        |   no    |
| **[smiles\_ga](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                       | SMILES     | joblib, nltk                                    |    no     |
| **[stoned](https://chemrxiv.org/engage/chemrxiv/article-details/60c753f00f50db6830397c37)**               | SELFIES    | -                                              |    no    |
| **[selfies\_ga](https://openreview.net/forum?id=H1lmyRNFvr)**                                             | SELFIES    | selfies                                        |    no     |
| **[graph\_mcts](https://pubs.rsc.org/en/content/articlelanding/2019/sc/c8sc05372c)**                      | atom       | -                                            |    no     |
| **[smiles\_lstm\_hc](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                 | SMILES     | guacamol                                       |    no     |
| **[smiles\_ahc](https://arxiv.org/pdf/2212.01385.pdf)**                                                   | SMILES     |                                                |    no     |
| **[selfies\_lstm\_hc](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839)**                                | SELFIES    | guacamol, selfies                             |    yes    |
| **[smiles\_vae](https://arxiv.org/pdf/1610.02415.pdf)**                                                   | SMILES     | botorch                                         |    yes     |
| **[selfies\_vae](https://arxiv.org/pdf/1610.02415.pdf)**                                                  | SELFIES    | botorch, selfies                               |    yes     |
| **[jt\_vae](https://arxiv.org/pdf/1802.04364.pdf)**                                                       | fragment   | botorch                                         |    yes     |
| **[gpbo](https://openreview.net/forum?id=gS3XMun4cl_)**                                                   | fragment   | botorch, networkx                             |    no     |
| **[reinvent](https://arxiv.org/abs/1704.07555)**                                                          | SMILES     | pexpect, bokeh                               |    yes    |
| **[reinvent\_transformer](https://arxiv.org/pdf/2310.05365)**                                             | SMILES     | pexpect, bokeh                                   |    yes    |
| **[reinvent\_selfies](https://arxiv.org/abs/1704.07555)**                                                 | SELFIES    | selfies, pexpect, bokeh                        |    yes     |
| **[smiles\_aug\_mem](https://chemrxiv.org/engage/chemrxiv/article-details/6464dc3ea32ceeff2dcbd948)**     | SMILES     | reinvent-models==0.0.15rc1                     |    yes     |
| **[smiles\_bar](https://pubs.acs.org/doi/full/10.1021/acs.jcim.2c00838)**                                 | SMILES     | reinvent-models==0.0.15rc1                      |    yes     |
| **[reinvent\_selfies](https://arxiv.org/abs/1704.07555)**                                                 | SELFIES    | selfies                                        |    yes     |
| **[moldqn](https://www.nature.com/articles/s41598-019-47148-x?ref=https://githubhelp.com)**               | atom       | networks, requests                            |     yes    |
| **[mimosa](https://arxiv.org/abs/2010.02318)**                                                            | fragment   | -                                           |     yes    |
| **[mars](https://openreview.net/pdf?id=kHSu4ebxFXY)**                                                     | fragment   | chemprop, networkx, dgl                         |    yes     |
| **[dog\_gen](https://proceedings.neurips.cc/paper/2020/file/4cc05b35c2f937c5bd9e7d41d3686fff-Paper.pdf)** | synthesis  | extra conda                                    |     yes    |
| **[dog\_ae](https://proceedings.neurips.cc/paper/2020/file/4cc05b35c2f937c5bd9e7d41d3686fff-Paper.pdf)**  | synthesis  | extra conda                                    |    yes     |
| **[synnet](https://openreview.net/forum?id=FRxhHdnxt1)**                                                  | synthesis  | dgl, pytorch_lightning, networkx, matplotlib  |    yes     |
| **[pasithea](https://arxiv.org/pdf/2012.09712.pdf)**                                                      | SELFIES    | selfies, matplotlib                             |    yes     |
| **[dst](https://openreview.net/pdf?id=w_drCosT76)**                                                       | fragment   | -                                              |    no     |
| **[gflownet](https://arxiv.org/abs/2106.04399)**                                                          | fragment   | torch_{geometric,sparse,cluster}, pdb          |     yes    |
| **[gflownet\_al](https://arxiv.org/abs/2106.04399)**                                                      | fragment   | torch_{geometric,sparse,cluster}, pdb           |    yes     |





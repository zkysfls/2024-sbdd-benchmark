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
| **[DST](https://arxiv.org/abs/2109.10469)**                      | 2D       |  1001          |    no     |
| **[Graph GA](https://pubs.rsc.org/en/content/articlelanding/2019/sc/c8sc05372c)**                                 | 2D     | 643          |    no    |
| **[MIMOSA](https://arxiv.org/abs/2010.02318)**                                                   | 2D     |  1001          |    yes     |
| **[MolDQN](https://arxiv.org/abs/1810.08678)**                                | 2D    |  501          |    yes    |
| **[Pasithea](https://arxiv.org/abs/2012.09712)**                                                   | 1D     |  914          |    yes     |
| **[REINVENT](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-017-0235-x)**                                                  | 1D    |  100          |    yes     |
| **[SCREENING](https://arxiv.org/pdf/1802.04364.pdf)**                                                       | -   | 1000          |    no     |
| **[SELFIES-VAE-BO](https://arxiv.org/abs/1610.02415)**                                                   | 1D   | 200          |    yes     |
| **[SMILES-GA](https://arxiv.org/abs/1804.02134)**                                                          | 1D     |  584          |    no    |
| **[SMILES-LSTM-HC](https://arxiv.org/abs/1811.09621)**                                             | 1D     | 501          |    no    |
| **[SMILES-VAE-BO](https://arxiv.org/abs/1610.02415)**                                                 | 1D    | 200          |    yes     |


## PDB information

All the PDB files can be downloaded from **[RCSB Protein Data Bank](https://www.rcsb.org/)**. The blinding sites are as follow:

| PDB   | center(x,y,z)    | bounding box size |
| 1iep  | 15.6138918, 53.38013513, 15.454837    | 15    |
| 3eml  | -9.06363, -7.1446, 55.86259999    | 15    |
| 3ny8  | 2.2488, 4.68495, 51.39820000000001    | 15 (23 for Pocket2mol)    |
| 4rlu  | -0.73599, 22.75547, -31.23689     | 15    |
| 4unn  | 5.684346153, 18.1917, -7.3715     | 15    |
| 5mo4  | -44.901, 20.490354, 8.48335       | 15    |
| 7l11  | -21.81481, -4.21606, -27.98378    | 15 (23 for Pocket2mol)    |


## Sampling and evaluating

For 3DSBDD and Pocket2mol, we use this command to generate:

```bash
python sample_for_pdb.py --pdb_path [your pdb] --center=[centers] --bbox_size [box size] --outdir [your outdir]
```

Also need to change the num_samples in the sample_for_pdb.yml

For PocketFlow, we use this command to generate:

```bash
python main_generate.py -pkt [your pdb] --ckpt ckpt/ZINC-pretrained-255000.pt -n 1000 -d cuda:0 --root_path [your outdir] --name [pdb name] -at 1.0 -bt 1.0 --max_atom_num 35 -ft 0.5 -cm True --with_print True
```

For ResGen, we first convert our pdb file to sdf file and use this command to generate:

```bash
python gen.py --pdb_file [your pdb] --sdf_file [correspond sdf] --outdir [your outdir]
```

For Autogrow4, we recommend following their tutorial before running the generation command:

```bash
python RunAutogrow.py \
    --filename_of_receptor [your pdb] \
    --center_x [center x] --center_y  [center y] --center_z [center z] \
    --size_x [box size] --size_y [box size] --size_z [box size] \
    --source_compound_file /autogrow4/autogrow/source_compounds/naphthalene_smiles.smi \
    --root_output_folder /PATH_TO/output_directory/ \
    --number_of_mutants_first_generation 50 \
    --number_of_crossovers_first_generation 50 \
    --number_of_mutants 50 \
    --number_of_crossovers 50 \
    --top_mols_to_seed_next_generation 50 \
    --number_elitism_advance_from_previous_gen 50 \
    --number_elitism_advance_from_previous_gen_first_generation 10 \
    --diversity_mols_to_seed_first_generation 10 \
    --diversity_seed_depreciation_per_gen 10 \
    --num_generations 5 \
    --mgltools_directory /PATH_TO/mgltools_x86_64Linux2_1.5.6/ \
    --number_of_processors -1 \
    --scoring_choice VINA \
    --LipinskiLenientFilter \
    --start_a_new_run \
    --rxn_library ClickChem \
    --selector_choice Rank_Selector \
    --dock_choice VinaDocking \
    --max_variants_per_compound 5 \
    --redock_elite_from_previous_gen False \
    --generate_plot True \
    --reduce_files_sizes True \
    --use_docked_source_compounds True \
    >  /PATH_TO/OUTPUT/text_file.txt 2>  /PATH_TO/OUTPUT/text_errormessage_file.txt
```

These above models only produce molecules, to evalute these molecules with docking and heuristic oracles, using following command:
```bash
python evaluation.py --smiles_path [your path] --pdb [your pdb] --model [model name]
```


For the rest of models that are under PMO, we use the following command to generate, note that you should running under TDC enviornment:
```bash
oracle_array=('1iep_docking' '3eml_docking' '3ny8_docking' '4rlu_docking' '4unn_docking' '5mo4_docking' '7l11_docking')

for oralce in ${oracle_array[@]}
do
python -u run.py [model name] --task production --n_runs 1 --max_oracle_calls 1000 --oracles ${oralce}
done
```

After generation, you could use mol_opt_process to convert the generated yaml file to csv file and evaluate the heuristic oracles.

To know the statistics of the docking or property score, you can use following code:
```bash
python results_compare.py --eval_folder_path [your generated result] --pdb_list [your pdb list] --file_type [docking or property] --output_folder [your outdir]
```
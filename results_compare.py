import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import re
import csv
import os
import pandas as pd

def calculate_and_store_stats(all_data, models, pdb_code, file_type):
    
    if file_type == 'docking':
        stats_file = f'{pdb_code}_{file_type}_stats.txt'
        grouped = all_data.groupby('model')
            # Calculate min, max, and median
        min_values = grouped['Docking score'].min()
        max_values = grouped['Docking score'].max()
        median_values = grouped['Docking score'].median()
        mean_values = grouped['Docking score'].mean()

        # Write statistics for the model to the file
        with open(stats_file, 'w') as file:
            for model in models:
                min_val = min_values[model]
                max_val = max_values[model]
                median_val = median_values[model]
                mean_val = mean_values[model]
                file.write(f'PDB {pdb_code} - Model {model}: \
                        Min {min_val}, Max: {max_val}, Median: {median_val}, Mean: {mean_val}\n')
        
    elif file_type == 'property':
        stats_file = f'{pdb_code}_{file_type}_stats.txt'
        grouped = all_data.groupby('model')
        min_values_sa = grouped['SA'].min()
        max_values_sa = grouped['SA'].max()
        median_values_sa = grouped['SA'].median()
        mean_values_sa = grouped['SA'].mean()

        min_values_qed = grouped['QED'].min()
        max_values_qed = grouped['QED'].max()
        median_values_qed = grouped['QED'].median()
        mean_values_qed = grouped['QED'].mean()

        min_values_logp = grouped['LogP'].min()
        max_values_logp = grouped['LogP'].max()
        median_values_logp = grouped['LogP'].median()
        mean_values_logp = grouped['LogP'].mean()

            # Write statistics for the model to the file
        with open(stats_file, 'w') as file:
            for model in models:
                min_val_sa = min_values_sa[model]
                max_val_sa = max_values_sa[model]
                median_val_sa = median_values_sa[model]
                mean_val_sa = mean_values_sa[model]

                min_val_qed = min_values_qed[model]
                max_val_qed = max_values_qed[model]
                median_val_qed = median_values_qed[model]
                mean_val_qed = mean_values_qed[model]

                min_val_logp = min_values_logp[model]
                max_val_logp = max_values_logp[model]
                median_val_logp = median_values_logp[model]
                mean_val_logp = mean_values_logp[model]
                file.write(f'PDB {pdb_code} - Model {model} - SA: \
                            Min {min_val_sa}, Max: {max_val_sa}, Median: {median_val_sa}, Mean: {mean_val_sa}\n \
                            QED: Min {min_val_qed}, Max: {max_val_qed}, Median: {median_val_qed}, Mean: {mean_val_qed}\n \
                            LogP: Min {min_val_logp}, Max: {max_val_logp}, Median: {median_val_logp}, Mean: {mean_val_logp}\n')



def process_files(pdb_code, folder_path, file_type):
    all_data = pd.DataFrame()
    models = []

    for filename in os.listdir(folder_path):
        if filename.startswith(f"{pdb_code}_{file_type}"):
            model = filename.split('_')[2].split('.')[0]  # Extract the model name
            full_path = os.path.join(folder_path, filename)
            df = pd.read_csv(full_path)
            df['model'] = model  # Add a column for the model
            all_data = pd.concat([all_data, df])
            models.append(model)

    return all_data, models

def create_boxplot(all_data, models, pdb_code, file_type):
    
    if file_type == 'docking':
        plt.figure()
        sns.boxplot(x='model', y='Docking score', data=all_data)
        plt.title(f'{pdb_code} {file_type.title()} Boxplot')
        plt.suptitle('')
        plt.xlabel('Model')
        plt.ylabel('Docking score')
        plt.savefig(f'{pdb_code}_{file_type}_combined_boxplot.png')
    elif file_type == 'property':
        for property_type in ['SA', 'QED', 'LogP']:
            plt.figure()
            sns.boxplot(x='model', y=property_type, data=all_data)
            plt.title(f'{pdb_code} {property_type} Boxplot')
            plt.suptitle('')
            plt.xlabel('Model')
            plt.ylabel(property_type)
            plt.savefig(f'{pdb_code}_{property_type}_combined_boxplot.png')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--eval_folder_path', type=str,
                        help='Path to the evaluation folder')
    parser.add_argument('--pdb', type=str,
                        help='The PDB that want to compare')
    parser.add_argument('--file_type', type=str,
                        help='docking or property')
    args = parser.parse_args()

    all_data, models = process_files(args.pdb, args.eval_folder_path, args.file_type)
    print(all_data)
    print(models)
    create_boxplot(all_data, models, args.pdb, args.file_type)
    calculate_and_store_stats(all_data, models, args.pdb, args.file_type)




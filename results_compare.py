import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import re
import csv
import os
import pandas as pd

def calculate_and_store_stats(all_data, models, pdb_code, file_type, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if file_type == 'docking':
        stats_file = f'{pdb_code}_{file_type}_stats.txt'
        grouped = all_data.groupby('model')
            # Calculate min, max, and median
        min_values = grouped['Docking score'].min()
        max_values = grouped['Docking score'].max()
        median_values = grouped['Docking score'].median()
        mean_values = grouped['Docking score'].mean()
        save_path = os.path.join(output_folder, stats_file)
        # Write statistics for the model to the file
        with open(save_path, 'w') as file:
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

        save_path = os.path.join(output_folder, stats_file)
        # Write statistics for the model to the file
        with open(save_path, 'w') as file:
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
    pattern = re.compile(rf'{re.escape(pdb_code)}_' + re.escape(file_type) + r'_(.+)\.csv')

    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            model = pattern.match(filename).group(1)
            full_path = os.path.join(folder_path, filename)
            df = pd.read_csv(full_path)
            df['model'] = model
            all_data = pd.concat([all_data, df])
            if model not in models:
                models.append(model)
    return all_data, models

def create_top_n_avg_scores(df, top_n, pdb, file_type):
    if file_type == 'docking':
        top_n_avg_scores = df.groupby('model')['Docking score'].apply(lambda x: x.nsmallest(top_n).mean())
        top_n_avg_scores_df = top_n_avg_scores.reset_index()
        top_n_avg_scores_df.columns = ['Model', f'Top {top_n} Average Docking Score']
        top_n_avg_scores_df['pdb'] = pdb
    

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--eval_folder_path', type=str,
                        help='Path to the evaluation folder')
    parser.add_argument('--pdb_list', type=str,
                        help='The list of PDB that want to compare',
                        default=['1iep', '3eml', '3ny8', '4rlu', '4unn', '5mo4', '7l11'])
    parser.add_argument('--file_type', type=str,
                        help='docking or property')
    parser.add_argument('--output_folder', type=str,
                        help='the path to save the output')
    args = parser.parse_args()

    all_data_list = []
    for pdb in args.pdb_list:
        all_data, models = process_files(pdb, args.eval_folder_path, args.file_type)
        all_data = all_data[~all_data.duplicated(keep=False)]
        all_data = all_data.reset_index(drop=True)
        
    







"""
def create_boxplot(all_data, models, pdb_code, file_type, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if file_type == 'docking':
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='model', y='Docking score', data=all_data, order=models)
        plt.xticks(rotation=45)  # Rotate labels
        plt.title(f'{pdb_code} {file_type.title()} Boxplot', fontsize=20)
        plt.suptitle('')
        plt.xlabel('Model')
        plt.ylabel('Docking score')
        plt.tick_params(axis='x', which='both', labelsize=10)  # Adjust font size as needed
        plt.tick_params(axis='y', which='both', labelsize=12)
        save_path = os.path.join(output_folder, f'{pdb_code}_{file_type}_combined_boxplot.png')
        plt.savefig(save_path)
        plt.close()
    elif file_type == 'property':
        for property_type in ['SA', 'QED', 'LogP']:
            plt.figure(figsize=(12, 8))
            sns.boxplot(x='model', y=property_type, data=all_data, order=models)
            plt.xticks(rotation=45)  # Rotate labels
            plt.title(f'{pdb_code} {property_type} Boxplot', fontsize=20)
            plt.suptitle('')
            plt.xlabel('Model')
            plt.ylabel(property_type)
            plt.tick_params(axis='x', which='both', labelsize=10)  # Adjust font size as needed
            plt.tick_params(axis='y', which='both', labelsize=12)
            save_path = os.path.join(output_folder, f'{pdb_code}_{property_type}_combined_boxplot.png')
            plt.savefig(save_path)
            plt.close()

def create_kdeplot(all_data, models, pdb_code, file_type, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    palette = sns.color_palette('bright', len(models))
    color_dict = dict(zip(models, palette))

    if file_type == 'docking':
        # Create a KDE plot
        plt.figure(figsize=(12, 8))
        for model in models:
            model_data = all_data[all_data['model'] == model]
            sns.kdeplot(model_data['Docking score'], bw_adjust=0.5, label=model, color=color_dict[model])
        # Set the title and labels
        plt.title(f'KDE Plot for {pdb_code} {file_type}', fontsize=20)
        plt.xlabel('Docking score')  # Adjust label as needed
        plt.ylabel('Density')
        plt.tick_params(axis='x', labelsize=12)  # Adjust font size as needed
        plt.tick_params(axis='y', labelsize=12)
        plt.legend()
        # Save the plot
        save_path = os.path.join(output_folder, f'{pdb_code}_{file_type}_kde_plot.png')
        plt.savefig(save_path)
        plt.close()
    elif file_type == 'property':
        for property_type in ['SA', 'QED', 'LogP']:
            plt.figure(figsize=(12, 8))
            for model in models:
                model_data = all_data[all_data['model'] == model]
                sns.kdeplot(model_data[property_type], bw_adjust=0.5, label=model, color=color_dict[model])
            plt.title(f'{pdb_code} {property_type} kdeplot', fontsize=20)
            plt.xlabel(property_type)
            plt.ylabel('Density')
            plt.tick_params(axis='x', which='both', labelsize=12)  # Adjust font size as needed
            plt.tick_params(axis='y', which='both', labelsize=12)
            plt.legend()
            save_path = os.path.join(output_folder, f'{pdb_code}_{property_type}_combined_kdeplot.png')
            plt.savefig(save_path)
            plt.close()
"""


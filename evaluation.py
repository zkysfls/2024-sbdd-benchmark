from tdc import Oracle
import argparse
import re
import csv

def extract_smiles(file_path):
    smiles_strings = []
    # Example regex pattern for a SMILES string; adjust as needed
    smiles_pattern = r'^[A-Za-z0-9@+\-\[\]\(\)\/%=#$]+'

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(smiles_pattern, line)
            if match:
                smiles_string = match.group()
                smiles_strings.append(smiles_string)

    return smiles_strings

def docking_score_eval(docking_oracle, smiles_list, csv_path):
    with open(csv_path, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Input smiles', 'Docking score'])
        for smiles in smiles_list:
            docking = docking_oracle(smiles)
            csv_writer.writerow([smiles, docking])

def property_score_eval(sa_oracle, qed_oracle, logp_oracle, smiles_list, csv_path):
    with open(csv_path, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['Input smiles', 'SA', 'QED', 'LogP'])
        for smiles in smiles_list:
            sa = sa_oracle(smiles)
            qed = qed_oracle(smiles)
            logp = logp_oracle(smiles)
            csv_writer.writerow([smiles, sa, qed, logp])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--smiles_path', type=str,
                        help='Path to the smiles file')
    parser.add_argument('--pdb', type=str,
                        help='The PDB that the smiles file generated from')
    parser.add_argument('--model', type=str,
                        help='The model used to generate smiles')
    args = parser.parse_args()

    smiles_list = extract_smiles(args.smiles_path)
    
    docking = args.pdb + '_docking'
    docking_oracle = Oracle(name = docking)
    docking_csv_path = '../evaluation_outputs/' + args.pdb + '_docking_' + args.model + '.csv' 
    docking_score_eval(docking_oracle, smiles_list, docking_csv_path)
    
    oracle_sa = Oracle(name = 'SA')
    oracle_qed = Oracle(name = 'QED')
    oracle_logp = Oracle(name = 'LogP')
    property_csv_path = '../evaluation_outputs/' + args.pdb + '_property_' + args.model + '.csv'
    property_score_eval(oracle_sa, oracle_qed, oracle_logp, smiles_list, property_csv_path)


    
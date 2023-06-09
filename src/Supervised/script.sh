#!/bin/bash
#SBATCH --account marasovic-gpu-np
#SBATCH --partition marasovic-gpu-np
#SBATCH --ntasks=32
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:1
#SBATCH --time=8:00:00
#SBATCH --mem=80GB
#SBATCH --mail-user=jacob.k.johnson@utah.edu
#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH -o filename-%j

#echo 0

source /scratch/general/vast/u0403624/miniconda3/etc/profile.d/conda.sh

#echo conda

conda activate 38

#echo activated

wandb disabled
export TRANSFORMER_CACHE="/scratch/general/vast/u0403624/huggingface_cache"

#echo setup

bash run_single_unifiedqa.sh unifiedqa-v2-t5-large-1251000 /scratch/general/vast/u0403624/condaqa_predictions/0Wonly/
bash eval_single_unifiedqa_model.sh unifiedqa-v2-t5-large-1251000 /scratch/general/vast/u0403624/condaqa_predictions/0Wonly/
bash compute_unifiedqa_stats.sh unifiedqa-v2-t5-large-1251000 /scratch/general/vast/u0403624/condaqa_predictions/0Wonly/

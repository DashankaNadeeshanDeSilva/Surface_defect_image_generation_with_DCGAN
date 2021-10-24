#!/bin/bash
#SBATCH -p ib
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 6
#SBATCH --mem-per-cpu 16000
#SBATCH --mail-type ALL
#SBATCH --mail-user dedimuni.de.silva@tuhh.de
#SBATCH --time 48:00:00


python3 train.py --dataroot data/severstal_steel_defect/train_contrast_changed_2/ --num_epochs 1 --batch_size 25 --lr 0.0001


exit
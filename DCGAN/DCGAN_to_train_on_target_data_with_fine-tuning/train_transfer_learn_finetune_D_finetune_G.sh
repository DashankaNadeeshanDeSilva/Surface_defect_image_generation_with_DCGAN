#!/bin/bash
#SBATCH -p ib
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 6
#SBATCH --mem-per-cpu 16000
#SBATCH --mail-type ALL
#SBATCH --mail-user dedimuni.de.silva@tuhh.de
#SBATCH --time 24:00:00


python3 train_transfer_learn_finetune_D_finetune_G.py --dataroot data/ifpt/train_aug/ --num_epochs 10 --batch_size 36 --lr 0.00001 --netG checkpoints/netG.pth --netD checkpoints/netD.pth


exit
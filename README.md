# DCGAN development to generate surface defect images.

## The repository contains the following implementations:

1. DCGAN model implementation with fine-tuning.
2. Image pre-processing and dataset creating scripts.
3. CNN Classifier to test the generated images.

## 01. Training the DCGAN to generate surface defect images.

### (a) Training the DCGAN on source dataset (Severstal Steel Defect Detection dataset).

1. Change the working directory to `DCGAN/DCGAN_to_train_on_source_data/`.
2. Install the dependencies with `requirements.txt`
```console
$ pip install -r requirements.txt
```
3. Place the dataset in the `data/severstal_steel_defect/train/` (as done in the repo).
4. To train from the scratch:
```console
$ python3 train.py --dataroot data/source_data/ --num_epochs 10 --batch_size 25 --lr 0.0001
```
One can define their arguments. 
6. To continue training, place the saved model in the `checkpoints` directory (or begin with the saved model from the last training session) and run:
```console
$ python3 train.py --dataroot data/source_data/ --num_epochs 10 --batch_size 25 --lr 0.0001 --netG checkpoints/netG.pth --netD checkpoints/netD.pth
```
7. After training one can test the images by generating images with the trained model. 

### (b) Fine-tuning the DCGAN on the targe dataset (IFPT dataset).

1. Change the working directory to `DCGAN/DCGAN_to_train_on_target_data_with_fine-tuning`
2. Place the image dataset for each class in the relevant directory.
(eg: `data/ifpt/with_defects` for `with defects` class)
3. To start training (or continue training), place the saved model in the `checkpoints` directory and run (arguments can be changed):
```console
$ python3 train_transfer_learn_finetune_D_finetune_G.p --dataroot data/source_data/ --num_epochs 10 --batch_size 25 --lr 0.0001 --netG checkpoints/netG.pth --netD checkpoints/netD.pth
```
Fine-tuning and training on the target dataset should be done for both classes.

## 02. Image pre-processing and dataset creating scripts.

### This section contains 3 scripts:
1. Image splitting to create the source dataset from the original images.
2. Resizing images for both source and target datasets.
3. Renaming images to annotate the images to create an image dataset.

## 03. CNN Classifier to test the generated images.

CNN Classifier to test the generated images after Fine-tuning and training on the target (IFPT) dataset. The classifier is first trained only on generated images and then tested on original images from the target dataset.



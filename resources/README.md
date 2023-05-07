# Lab 1-4:  Neural Network Training

Now that we have seen how to run simple networks using PyTorch, our next goal will be to train our own network for a classic computer vision task. The task we will focus on is based on the CIFAR-10 dataset. Our goal is to come up with the simplest network to correctly classify the supplied images into one of 10 classes.

This lab can be broken down into two large parts: 1) train your neural network that satisfies the constraints, and 2) estimate the energy and latency of processing inference using your neural network with Timeloop/Accelergy tools. The first part of this lab will require GPU support, and we outline GPU options below. The second part will be using the Docker same as in previous questions in Lab1. The neural network training and Timeloop/Accelergy profiling both take **multiple hours to finish**, so please start early.

## Summary of Your Result

- Your Name: Guangxuan Xiao
- Your Model's Final Score (according to grading rubric): 90
- Your Model's Test Accuracy: 79.66%`
- Your Model's Energy (should match the result in `run_profile.ipynb`): `0.32204000mJ`
- Your Model's Number of Cycles (should match the result in `run_profile.ipynb`): `0.04634400M Cycles`
- Your Model's Peak Activation Size (should match the result in `run_profile.ipynb`): `98304.0Bytes`

## GPU Platform

This lab requires GPU support. The starter codes will outline basic training and utility functions you can use for this lab, depending on your GPU platform. We recommend using Google Colab, which offers free GPU acceleration (NVIDIA K80), for the training purpose. However, if you have a personal GPU platform that you have been already using (e.g., GPU Laptops, AWS or Google Cloud Platform), please feel free to use it. 

For the starter code for training your neural network, please refer to [./run_training.ipynb](./run_training.ipynb). The notebook works for both a personal GPU and Google Colab,

1. Personal GPU Available

If you have a personal GPU that can be used for this lab, please install [PyTorch](https://pytorch.org/) with GPU support. The docker we are using does not support GPU, and you can separately install PyTorch for GPU using virtual environments (e.g., Ananconda) on your personal computer. 

2. Google Colab (Recommended)

Google Colab offers free GPU acceleration. You can copy the starter code in [./run_training.ipynb](./run_training.ipynb) to your Google Drive, and follow instructions in the starter code to start using Google Colab. You don't have to install any other programs locally to your personal computer in this case! The GPU types in Colab vary over time, including Nvidia K80s, T4s, P4s and P100s.

## TODO

1. Determine which GPU platform you are going to use for this lab. In case you are using personal GPU, make sure you install PyTorch with GPU support, independent of this Docker. Note that this Docker does not support GPU. 
2. Train your neural network. You can use the starter code, or can write your own script. Please commit the updated training code you are using. 
3. Now, launch the Docker, and run the energy/latency estimation for the model you trained (you can start running the estimation before the training is completed - all you need for this part is the description of the model, not the exact parameters).
4. Update your result summary in this README.md file. Also, make sure to commit and push your training code that includes your model description, training method (hyperparameters), and the updated `run_profile.ipynb`. 

## Rules (Please Read Carefully)

0. You are only allowed to explore different (1) Network Architecture, (2) Parameters of SGD optimizer, and (3) Number of epochs (<30). Please do not use other training techniques such as augmentation or different optimizers.
1. ***Number of epochs is limited to < 30***, please do not train your model over 30 epochs.
2. Please do not use or reverse-engineer the test set to improve the performance of your model. You can only use the training set (and choose a subsample of it as the validation set) to train the model and choose pre-processing and hyperparameters.
3. Please do not use any pre-trained models that were trained using other datasets, such as ImageNet.
4. Please commit and push your training code and the pytorch model description to this repository. If we cannot reasonably reproduce your error rate, we will not award the grading points. Specify your hyperparameters and random seed numbers as well.
5. Please do not change Timeloop/Accelergy settings in `./simple_weight_stationary` and `./profiler.py`.
6. Finally, sign this agreement form:  https://forms.gle/GQ7Rzsa4kZM8ZU4j9

## Grading Rubric

In this lab, you can design your own neural network, aiming for high accuracy while achieving low energy and latency. With this is mind, you need to construct the a single neural network to maximize your grade on the assignment. All error rates below are on the **test set**. 

- Hard constraints (violation of any of these conditions will result in 0 point)
    - The peak activation size (sum of both the input activation size and the output activation size to any given layer) should be smaller than 1MB.
    - Error rate on the test set should be less than 50%. 
    
- Base Points (Maximum: 100 Points)
    - Error rate
    
    | Error rate  | 40%~49%  |  30%~39% |  20%~29% |  < 20%   |
    | :---------: | :------: | :------: | :------: | :------: |
    | Point       | 30       | 40       | 50       | 60       |
    
    - Energy
    
    | Energy  | < 2mJ   | < 1.5mJ  | < 1mJ    | < 0.5mJ  |
    | :-----: | :-----: | :-----:  | :-----:  | :-----:  |
    | Point   | 5       | 10       | 15       | 20       |
    
    - Latency
    
    | Latency  | < 1M cycles | < 0.5M cycles | < 0.25M cycles | < 0.1M cycles |
    | :-----:  | :---------: | :-----------: | :------------: | :-----------: |
    | Point    | 5           | 10            | 15             | 20            |
     

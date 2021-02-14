# Recommendation systems

## Introduction

This repository contains two Collaborative filtering techniques to predict movie ratings from data. The two algorithms are **nearest neighbour** and **latent factor models**. Inside the repository, you can find my report (coming soon) which describes these two algorithms in details and evaluates their performance.

## The data-set used

The data-set used in this repository is from [MovieLens](https://grouplens.org/datasets/movielens/). I have used the small data-set (100,000 ratings) that is recommended for education and development.

## Interesting features

### Config file

In the config file (config.json), you can change the parameters for the two programs.

### Multiprocessing

For the nearest neighbour program, multiprocessing will be used to create multiple processes to speed up the program. Each process will be assigned a chunk to of the data-set to predict the ratings for.

### Hyper-parameter optimization

The latent factors model program has the ability to optimize the hyper-parameters (e.g., number of latent factors). [Optuna](https://optuna.org/) is used for this feature. You can enable this feature in the config file and set the number of iterations for the optimizations process.

Beware that hyper-parameter optimization is computationally intensive can take a large amount of time.

### Matrix maker

The MatrixMaker class creates numpy arrays needed for the two programs and saves them. This helps in reducing the time needed as these arrays don't need to be built again.

### Logger

The Logger class appends to a CSV file (logs.csv) meta-data about the last execution of one of the two programs. This log file can be later used for further analysis about the two algorithms.

## How to use the provided Jupyter Notebooks

First, you need to have Python installed. The version used for the development of this project is Python 3.7 so it is recommended to use Python 3.7 or higher. Second, you need to install Jupyter Lab. The installation instructions can be found [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html). Then you run the notebooks (nearest_neighbour.ipynb and latent_factors.ipynb). It is recommended to use Linux when running nearest_neighbour.ipynb as using Multiprocessing with Jupyter Notebook on Windows causes some issues (you could try to set the number of processes to 1).

# BLDAP Intro to Python / Data Science Curriculum

## Introduction

This repository contains the Jupyter notebooks for the intro to Python / Data Science course for [Berkeley Lab Director's Apprenticeship Program (BLDAP)](https://k12education.lbl.gov/programs/high-school/BLDAP).

This course is designed for students with little to no experience in coding to learn skills in Python necessary for data science. Students utilize Jupyter notebooks throughout the course.

The overall goal is for students to learn how to use Python to clean, analyze, and visualize large data sets in order to communicate effectively their conclusions about the data set. Students apply the skills they learned on actual data sets provided by researchers in Berkeley Lab.

This repo contains the following:

- **00 Intro to Python:** Students learn the basics of Python, as well as libraries utilized in data science ([numPy,](https://numpy.org/) [pandas,](https://pandas.pydata.org/) [matplotlib](https://matplotlib.org/))
- **01 Cell Phone Design Challenge:** Students work with a dataset compiled from the [Materials Project](https://materialsproject.org/) database of calculated materials properties to design a cell phone that fulfills criteria such as low cost, lightweight, and durability
- **02 Energy Consumption Data Challenge:** Students work with energy consumption data from a pilot site that was used to test a software platform, “Solar+ Optimizer” (SPO), which aims to reduce the overall operational cost for buildings by taking into account time-varying costs of energy and status of the grid connection
- **03 Genomics Data Challenge:** Students work with RNA sequencing data of the algae *Chromochloris zofingiensis*, which is of interest due to its potential as a biofuel sources


## Installing Anaconda

The easiest way to run Python and Jupyter notebooks locally on the computer is through Anaconda. Anaconda is an open-source (free!) Python distribution platform.

Click here to download [Anaconda Distribution (Python 3.9, 64-Bit Graphical Installer)](https://www.anaconda.com/products/distribution). Make sure to download the correct version for the computer's operating system (Windows, Mac, or Linux).

## Running Jupyter Notebooks

First, download the coding bootcamp materials from this repository:

1. Click the green "Code" button on the top right of the repository information page.
2. Click "Download Zip". Extract the file to a folder where it can be easily accessed (such as the Desktop).

Then, use the Anaconda Navigator application to open the notebooks:

1. Open the Anaconda Navigator application (note that it might take a few minutes to load up when the application is launched for the first time).
2. Click the 'Launch' button under 'Jupyter Notebook' (NOT JupyterLab). A new tab in the internet browser should open with a file system. Navigate through the file system to the `BLDAP-Python-Data-Science` folder that was just downloaded.
3. Go to any folder and click on a notebook file (ends in `.ipynb`). A new tab should open with the notebook.

## Alternative to Anaconda

An alternative option is to run the Jupyter notebooks in the cloud through binder. Just keep in mind that work is not saved in binder.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LBNLnext/EinR-Coding-Bootcamp/HEAD?urlpath=tree)

## Acknowledgements

The Berkeley Lab K-12 team is truly grateful to the following who contributed to the development of these notebooks:

**Intro to Python:**

UC Berkeley's Data Science Modules Program, Division of Computing, Data Science, and Society

Kseniya Usovich (UC Berkeley), Karla Palos (UC Berkeley), Eric Van Dusen (UC Berkeley), Rachel McCarty (UC Berkeley), Baishakhi Bose (Berkeley Lab), Laurel Hales (Stanford)

**Cell Phone Design Challenge:**

Alex Ganose (Imperial College London), Ryan Kingsbury (Berkeley Lab), Jianli Cheng (Berkeley Lab)

**Energy Consumption Data Challenge:**

Anand Krishnan Prakash, Kun Zhang, Lazlo Paul and Dave Blum, Marco Pritoni and Rich Brown (Berkeley Lab)

Marc Marshall, James Zoellick, Peter Alstone (Schatz Energy Research Center, Humboldt State University)

Rachel McCarty (UC Berkeley)

**Genomics Data Challenge:**

Sharon Greenblum (Berkeley Lab), Ciara Acosta (UC Berkeley)

*Repo format inspired from UC Berkeley's [D-Lab](https://github.com/dlab-berkeley)*
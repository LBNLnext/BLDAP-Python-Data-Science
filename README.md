# BLDAP Intro to Python / Data Science Curriculum

## Introduction

This repository contains the Jupyter notebooks for the intro to Python / Data Science course for [Berkeley Lab Director's Apprenticeship Program (BLDAP)](https://k12education.lbl.gov/programs/high-school/BLDAP).

This course is designed for students with little to no experience in coding to learn skills in Python necessary for data science. Students utilize Jupyter notebooks throughout the course.

The overall goal is for students to learn how to use Python to clean, analyze, and visualize large data sets in order to communicate effectively their conclusions about the data set. Students apply the skills they learned on actual data sets provided by Berkeley Lab researchers.

More details on the curriculum, including more context for each section of the curriculum and possible curriculum sequence and standards covered can be found on our [website.](https://k12education.lbl.gov/programs/educators/data-science-curriculum)

## Repo Contents

This repo contains the following:

- **00 Intro to Python:** Students learn the basics of Python, as well as libraries utilized in data science ([numPy,](https://numpy.org/) [pandas,](https://pandas.pydata.org/) [matplotlib](https://matplotlib.org/)). Notebooks 00, 01, 02, 03, 04, 05, and 07 contain an auto-grader for some exercises called [Otter Grader](https://otter-grader.readthedocs.io/en/latest/). For those that do not want to use the auto-grader, duplicates of these notebooks without Otter Grader is also included.
- **01 Cell Phone Design Challenge:** Students work with a dataset compiled from the [Materials Project](https://materialsproject.org/) database of calculated materials properties to design a cell phone that fulfills criteria such as low cost, lightweight, and durability
- **02 Energy Consumption Data Challenge:** Students work with energy consumption data from a pilot site that was used to test a software platform, “Solar+ Optimizer” (SPO), which aims to reduce the overall operational cost for buildings by taking into account time-varying costs of energy and status of the grid connection
- **03 Genomics Data Challenge:** Students work with RNA sequencing data of the algae *Chromochloris zofingiensis*, which is of interest due to its potential as a biofuel sources
- **04 Neural Networks:** Students model a simple neural network, adding more complexities incrementally, with the goal of generating an image representing their neural network
- **05 Sustainable Biofuels Machine Learning Application:** Students use spectra data from jet fuels to train a machine learning model to predict properties of fuels, in the search for promising blends of fuels that are more sustainble for the aviation industry
- **06 kNN:** Students are introduced to classification in machine learning by implementing the k-Nearest Neighbors (kNN) algorithm
- **07 p-Value:** Students use Python to calculate the p-value for various data sets
- **08 Challenge Notebook Game:** These bonus challenges are for students to practice further the concepts that are covered in the 00 Intro to Python notebooks by creating a game. Each section within the challenge identifies which notebook(s) need to be completed before starting
- **Slides:** Slides to introduce concepts for each notebook


## Running Jupyter Notebooks

First, download the coding bootcamp materials from this repository:

1. Click the green "Code" button on the top right of the repository information page.
2. Click "Download Zip". Extract the file to a folder where it can be easily accessed (such as the Desktop).
3. We recommend using Google Colab to access these notebooks. Note that Otter Grader is set up to only work in Google Colab. To use Google Colab, upload the folders to a Google Drive. Alternatives to Google Colab are listed on our [website.](https://k12education.lbl.gov/programs/educators/data-science-curriculum)

## Binder

A very quick alternative option is to run the Jupyter notebooks in the cloud through binder. Please keep in mind that work is *not* saved in binder, unlike Google Colab or other options.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LBNLnext/BLDAP-Python-Data-Science/HEAD)

*Please note that binder takes a while to load when launching it for the first time.*
 

## Feedback and Suggestions

We welcome any feedback and suggestions for our curriculum resources so we can continuously improve them. Any questions about the curriculum resources can also be asked and a K-12 team member will email back.

The feedback form can also be used to request for answer keys for the Jupyter notebooks, assessments that instructors can use for the intro notebooks, and the pre/post coding assessment that can be used to assess the curriculum's overall impact on student learning and understanding. For the pre/post coding assessment, all students take the survey on day 1 before any coding lessons. Then at the very end of the program we have students take the same survey to see how much students learned and what concepts need more review.

**In an effort to keep this curriculum as open source, please do not post the answer keys on any public websites.**

[Fill out the feedback form](https://docs.google.com/forms/d/e/1FAIpQLSdIbIhiRG-rME3fNFWbnB3w2tdw20GFTloFg-6poYPWCd5OJg/viewform)

## Acknowledgements

The Berkeley Lab K-12 team is truly grateful to the following who contributed to the development of these notebooks:

***Intro to Python:***

UC Berkeley's Data Science Modules Program, Division of Computing, Data Science, and Society. Kseniya Usovich, Karla Palos, Eric Van Dusen, Rachel McCarty (UC Berkeley); Baishakhi Bose, Samanvitha Murthy, Arianna Formenti, Sage Miller (Berkeley Lab); Laurel Hales (Stanford).

[Otter-Grader from the UC Berkeley Data Science Education Program Infrastructure Team](https://otter-grader.readthedocs.io/en/latest/)
Otter-Grader was implemented in the notebooks by: Lawrence Chen (UC Berkeley) and Evan Neill (Berkeley Lab)

***Cell Phone Design Challenge:***

Alex Ganose (Imperial College London); Ryan Kingsbury (Princeton University); Barbara Bonfim (WWF-Brazil); Jianli Cheng, Rishabh Guha (Schrödinger Inc.); Ruoxi Yang (Tesla); Oxana Andriuc (UC Berkeley); Jingyang Wang (Beijing Normal University); Aaron Kaplan, Roberta Pascazio (Berkeley Lab).

***Energy Consumption Data Challenge:***

Anand Krishnan Prakash, Kun Zhang, Lazlo Paul and Dave Blum, Marco Pritoni and Rich Brown (Berkeley Lab); Marc Marshall, James Zoellick, Peter Alstone (Schatz Energy Research Center, Humboldt State University); Rachel McCarty, Kseniya Usovich (UC Berkeley); Laurel Hales (Stanford)

***Genomics Data Challenge:***

Sharon Greenblum (Berkeley Lab); Ciara Acosta, Kseniya Usovich (UC Berkeley)

***Neural Networks:***

Arianna Formenti (Berkeley Lab)

***Sustainable Biofuels for Aviation Machine Learning Challenge:***

Ana Comesana, Vi Rapp (Berkeley Lab). 

The above contributors would like to acknowledge DOE’s Bioenergy Technologies Office for funding this work. They would like to acknowledge Kyle Niemeyer at Oregon State University as the PI and collaborator for this work. They would also like to acknowledge Christopher Hagen at Oregon State University for his early support with FTIR spectra, Joshua Heyne at WSU-PNNL Bioproducts Institute for providing experimental property data, and Sharon Chen for her efforts collecting data.

***kNN & p-Value:***

Sage Miller (Berkeley Lab)

***Challenge Notebook Game:***

Laurel Hales (Stanford); Sage Miller (Berkeley Lab)

*Repo format inspired from UC Berkeley's [D-Lab](https://github.com/dlab-berkeley)*

© 2021-2025 The Regents of the University of California, through the Lawrence Berkeley National Laboratory

*** Copyright Notice ***

BLDAP Intro to Python/Data Science Curriculum Copyright (c) 2025, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy) and University of California, Berkeley.  All rights reserved.

If you have questions about your rights to use or distribute this software,
please contact Berkeley Lab's Intellectual Property Office at
IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department
of Energy and the U.S. Government consequently retains certain rights.  As
such, the U.S. Government has been granted for itself and others acting on
its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the
Software to reproduce, distribute copies to the public, prepare derivative 
works, and perform publicly and display publicly, and to permit others to do so.
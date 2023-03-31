# Creating a server for protein disorder prediction based on deep neural networks.

## Project Description
- We developed deep neural networks to predict intrinsic disorder within protein sequences.
- These deep neural networks have been trained and evaluated using the PyTorch machine learning framework. 
- We have also developed a Django server to provide an accessible user interface to use our models.

The entire project repository can be found at: https://github.com/ryangregson01/L4-dissertation
<br><br>

## Build instructions

**The following build instructions assist setting up the web server, the user interface for our deep neural network model. Instructions for using our deep neural networks (to reproduce the development and evaluation) is discussed below in neural network build instructions.**

### Requirements
- Python 3.8+. Development was completed using Python 3.8, and it cannot be guaranteed other versions are supported.
- Necessary packages are listed in requirements.txt, and are discussed in the following build steps.
- Application has been tested on MacOS.

### Build steps

- First obtain the source folder.
- Git must be installed and added to PATH, then:
```
$ git clone https://github.com/ryangregson01/L4-dissertation.git
```
or 
```
$ git clone git@github.com:ryangregson01/L4-dissertation.git
```

- Then navigate to the source folder
```
$ cd L4-dissertation/src
```

- Note again, Python 3.8 was used, therefore the following use of 'python' may be 'python3' in your environment. To ensure your python environment is suitable check what version of Python you have using:
```
$ python --version
```

- To run the web server, first install necessary dependencies:
```
$ cd django_server/django_server
$ python -m pip install -r requirements.txt --user
```
- Set-up the Django models
```
$ python manage.py makemigrations dashboard
$ python manage.py migrate
```
- Run the server
```
$ python manage.py runserver
```

#### Using the web server:
- Browse to https://127.0.0.1:8000/
- On the Home page you can enter a protein sequence in valid FASTA format.
- Try using the protein sequence here for example: https://rest.uniprot.org/uniprotkb/P03265.fasta

<br><br>

## Build instructions - neural networks

This set-up is more involved. The following provides instructions for how to setup the file structure such that the Notebooks can be ran successfully.
Each Notebook is self-documented using additional markdown throughout.

### Requirements
- Gmail account. We will be utilising Google Colab notebooks. An introduction to Google Colab can be found [here](https://colab.research.google.com/).
- Within notebook environments, we install appropriate requirements as necessary.

### Build steps

#### Setting up your file structure on Google Drive.

- Navigate to the main source directory.
```
$ cd L4-dissertation/src
```

If you do not have a 'Colab Notebooks' folder:
- Manually copy the 'Notebooks' folder into the root of your Google Drive. This should be called 'My Drive'
- Rename this folder to 'Colab Notebooks'. This is important for read operations within the Notebooks.

Otherwise:
- Manually copy the contents of the 'Notebooks' folder into the 'Colab Notebooks' folder on Google Drive.


This Colab Notebook folder contains a 'diss_files' folder, which contains pre-processed data and trained model weights. This folder name must remain as is as paths in the notebooks require access to these files to prevent long pre-processing steps before every use of the neural networks.
If you have obtained a source folder without the diss_files folder, or during reading file operations within a notebook there are errors, the pre-processed data exists here:
- These files can be downloaded from: [Google Drive](https://drive.google.com/drive/folders/1dr4T8FAzbF8yLS4pWyYgH_1lJnnmbmMC?usp=share_link)
- Furthermore, if you wish to carry out this pre-processing, the Dataset_preprocessing notebook can be executed. PSSMs must be created using an external library. We used the [MMSeqs2 software suite](https://github.com/soedinglab/MMseqs2). Note conducting this pre-processing may take a long time depending on resources you have access to.

<br>

#### Replicating training.
- There are 3 Notebooks in which neural networks are trained:
  - FCN_2DConvolutions - contains a CNN using 2D convolutional kernels.
  - FCN_1DConvolutions - contains a CNN using 1D convolutional kernels.
  - RNN_LSTM - contains a RNN using the LSTM architecture.
- Markdown is used throughout these Notebooks to provide context about training these models.

<br>

#### Evaluation.
- The evaluation_metrics notebook contains all evaluations for every model:
  - Machine learning metrics.
  - Confusion matrices.
  - ROC curves.
  - Statistical tests.
  - Using both test data and CASP10 benchmark data. These test files are in diss_files which is set-up earlier in this readme.
- Notebooks will contain output from previous executions.
- Testing our models does not require a GPU, therefore it is not computationally expensive to run the entire notebook.

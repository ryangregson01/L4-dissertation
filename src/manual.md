# User manual 

Please read readme.md first to ensure you have access to the src folder and have satisifed the requirements to run the web server. This user manual assumes you are at the root of the src folder and have access to a browser.

## Web server user manual

- Inside the source folder, navigate to the following directory containing the Django server and install requirements for this server.
```
$ cd django_server/django_server
$ python -m pip install -r requirements.txt --user
```
- Set-up the Django models.
```
$ python manage.py makemigrations dashboard
$ python manage.py migrate
```
- Run the server.
```
$ python manage.py runserver
```

- To use the web server:
  - Browse to https://127.0.0.1:8000/

<br>

- The following is a step-by-step guide for how to use the web server for the first time:
  - On the Home page you can enter a protein sequence in valid FASTA format.
  - Try using the protein sequence here for example: https://rest.uniprot.org/uniprotkb/P03265.fasta
  - Click submit sequence to make a prediction.
  - The sequence-based visualisation uses blue to identify ordered regions and red to identify disordered regions.
  - This visualisation can be saved using the 'Download Prediction as PNG' button.
  - Finally, navigate back to our home page using the hyperlink on the web page. 

<br>

## Training and evaluating neural networks on Colab
- Please read 'Build instructions - neural networks' in the readme.md to set-up the notebooks.
- Each notebook contains markdown to guide you through their contents.
- The following is a summary of the contents of each notebook:
  - Dataset_preprocessing - uses disordered sequences to generate all feature encoded sequences, labels and datasets.
  - FCN_1DConvolutions - used for implementing and training our CNN with 1D convolutions.
  - FCN_2DConvolutions - used for implementing and training our CNN with 2D convolutions.
  - RNN_LSTM - used for implementing and training our RNN using LSTMs.
  - evaluation_metrics - evaluates our models' performance.

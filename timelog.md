# Timelog

* Creating a server for protein disorder prediction based on deep neural networks.
* Ryan Gregson
* 2469038G
* Kevin Bryson

## Week 1

### 19 Sep 2022
* *2 hours* Read the project guidance notes.
* *6 hours* Read over the project list.

### 21 Sep 2022
* *6 hours* Refined and submitted choices.

## Week 2

### 28 Sep 2022
* *1 hour* Project receieved and thought about what I could do from description.

### 30 Sep 2022
* *0.5 hour* Arranged meeting with supervisor.

### 2 Oct 2022
* *3 hours* Read through recommended wikipedia readings.

## Week 3

### 3 Oct 2022

* *3 hours* Read through both seed papers and made a few notes.
* *1 hour* Downloaded and reviewed project template.
* *1 hour* Wrote up some discussion bullet points for my first meeting with my supervisor, and questions about seed papers and deep learning.

### 4 Oct 2022

* *1.5 hours* Initial meeting with supervisor (Kevin) and Alexandros (similar project with protein domains). Discussed previous research published that is similar to this project, what proteins are and discussed potential first initial plans.

### 11 Oct 2022

* *1.5 hours* Went through the introduction lectures for the first week of the Deep Learning (M) course.
* *0.5 hour* Set-up new Google account for using Google Colab with Jupyter notebooks.
* *2.5 hours* Went through the introductory deep learning with PyTorch document: https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html.

### 13 Oct 2022

* *1 hour* Explored GraphQL documentation.

### 14 Oct 2022

* *1 hour* Met with Kevin to discuss project. Helped me get a clearer understanding of deep learning. Discussed viable technologies. 
* *1 hour* Created minutes from this which lets me see my long-term goals and what I want to complete next week.

### 17 Oct 2022

* *1 hour* Went through lab 1 part 1, the 60 minute blitz tutorial, again.
* *1.5 hours* Went through lab 1 part 2 which was a Jupyter notebook on PyTorch basics. 

### 18 Oct 2022

* *3 hours* Read the seed paper on protein disorder again. Researched about paper. Set up and used Mendeley and techniques from RMT to write a level 1 and some level 3 summary sections about the paper.

### 19 Oct 2022

* *3 hours* Read the DISOPRED paper and analysed it using RMT techniques (L1 and L2 summaries). Created questions to ask at the meeting about this paper.
* *2 hours* Read the DISOPRED3 paper and analysed it using RMT techniques.

### 20 Oct 2022

* *2 hours* Finishing analysing the DISOPRED3 paper and made questions from annotations I’d made.
* *1 hour* Meeting with Kevin. Discussed forming a dataset and current databases with disordered proteins.
* *1 hour* Wrote up detailed minutes after meeting.

### 23 Oct 2022
* *3.5 hours* Worked through most of lab 2 from DL moodle - "Experiments with basic networks and visualising the results".

### 24 Oct 2022
* *1 hour* Fixed GitHub.

### 25 Oct 2022
* *3 hours* Went through Datasets and Dataloaders PyTorch document: https://pytorch.org/tutorials/beginner/basics/data_tutorial.html. Made my own Dataset. Experimented with pandas and Disprot data.

### 26 Oct 2022
* *2 hours* Querying UniProt to get sequence. Encoding a sequence as disordered or ordered.

### 27 Oct 2022
* *0.5 hours* Creating separate Google colab to present at meeting.
* *1.5 hours* Making sure encoding sequences worked for all sequences in Disprot data. Pre-processing of data.
* *1.5 hours* Meeting with Kevin. Discussed Dataset loader, how the data could look and kernels.
* *1 hour* Wrote up minutes after meeting.

### 1 Nov 2022
* *2 hours* Dataloader class trialing.

### 3 Nov 2022
* *1 hour* Wrote up Dataloader class developments and errors to discuss at the meeting.
* *1 hour* Meeting with Kevin. Discussed problems and steps for next week.
* *1 hour* Wrote up minutes after meeting

### 7 Nov 2022
* *1 hour* Made corrections to custom class. Now getitem returns the label for the sequence (0 for ordered, 1 for disordered).

### 8 Nov 2022
* *2 hours* Read through lab 3 (Convolutional networks) from DL moodle. It is primarily running cells and understanding their functionality.
* *1.5 hours* Unsuccessfully attempted to apply network models to the protein sequence data. Errors thrown when model is used. Better understanding of input into the model now.
* *2 hours* Read through book (https://www.deeplearningbook.org/) using assigned reading from DL lectures to strengthen understanding. Read Chapter 1 (Introduction) and some of Chapter 6 (Deep Feedforward Networks).

### 9 Nov 2022
* *2 hours* Redesigning dense model in lab 3 from DL moodle - so I can understand it better. Focused primarily on dense model even though two models are in this lab.
* *3 hours* Used dense model design learnt from lab 3 and applied this to loaded protein sequence data. Runs on sequences without errors; however, questions to be raised about the model at the meeting.

### 10 Nov 2022
* *2 hours* Read 'Fully Convolutional Networks for Semantic Segmentation' paper. Took brief notes on the paper and highlighed parts I didn't understand.
* *0.5 hours* Meeting with Kevin. Discussed problems with current neural network setup.
* *0.5 hours* Wrote up minutes after meeting.

### 14 Nov 2022
* *2 hours* Going through 'Fully Convolutional Networks for Semantic Segmentation' paper and looking into parts I didn't understand.

### 16 Nov 2022
* *3 hours* Continuing to go through the same paper, making comparisons to my project and researching concepts I didn't understand.
* *1 hour* Meeting with Kevin. Discussed FCN paper together
* *0.5 hours* Wrote up minutes after meeting.

### 17 Nov 2022
* *1.5 hours* Experiments with conv2D on random tensors, then applying convolution to a single protein sequence.

### 23 Nov 2022
* *1.5 hours* Applying multiple convolutions to two protein sequences. Experimented with padding.

### 24 Nov 2022
* *2 hours* Created a loose neural network model. Multiple convolution layer, followed by activation function. Tested with two protein sequences under a training loop. Not concentrated on what training loop really doing yet - mostly assessing loss can be calculated from model output and labels.
* *2 hours* Combining previous work from Notebooks with new FCN model. All preprocessing. Now have access to more than two protein sequences.
* *1 hour* Meeting with Kevin. Discussed current model, and potential refactoring.
* *1 hour* Wrote up minutes after meeting.
* *1 hour* Cleaned up Notebook. Inserted markdown throughout notebook to help the notebook read well and be understandle. Can commit this code so far (src/Notebooks).

### 9 Dec 2022
* *1 hour* Refactored amino acid map so that protein images now have 20 channels. Vectorised one protein with this map. Tested a 1D convolution on this protein.
* *1 hour* Meeting with Kevin.
* *0.5 hours* Wrote up minutes after meeting.

### 12 Dec 2022
* *2 hours* Implemented my FCN model with 1D convolutions.

### 13 Dec 2022
* *2 hours* Debugging training loop. Realised there was protein data incompatible with my solution. Implemented dataset cleaning for deprecated sequences. Looking up this protein accession number using the UniProt API returned an empty string otherwise.
* *2 hours* Further debugging of training loop. More protein data that was incompatible with my solution. Added data cleaning for sequences that have amino acid letter codes outwith the basic 20 amino acids. This only removes a few proteins, so should not impact my solution.

### 14 Dec 2022
* *1 hour* Debugging training loop. Although incompatible protein data had been dropped from dictionary, the indices were not consecutive, causing errors. Wrote cleaned data into new dictionary where indices are consecutive and training loop runs fully without crashing.
* *0.5 hour* Added gradient accumulation within training loop to see if training loss improved. This creates an effect of batching, as we only have a batch of size one in our dataloader.
* *1 hour* Wrote up first half of status report: proposal and progress.

### 15 Dec 2022
* *1.5 hours* Wrote up plan for semester 2 on status report.
* *1 hour* Meeting with Kevin. Discussed status report.
* *0.5 hours* Wrote up minutes after meeting.
* *1 hour* Tidied up status report.

### 16 Dec 2022
* *0.5 hours* Submitted status report.


## Winter

### 20 Dec 2022
* *1.5 hours* Started a practice web application by going through the start of the tango with django book for a quick refresher. Set up urls, an index view, an index template and ensured the static and media folders worked with the template.
* *1 hour* Brief reading on Docker and Nginx. Familiarising myself with technologies I have used but not implemented before.

### 21 Dec 2022
* *2 hours* Continued with the tango with django book. Created a model and form. Now made practice web application more aligned to goal application. Form takes in a string (e.g. protein sequence) and returns it out to the webpage.

### 22 Dec 2022
* *2 hours* Focusing on form with input as a protein sequence. Wrapped output of form so that you could see the whole sequence on the webpage without scrolling. Handled cleaning and validating data (e.g. removing '\n' characters).
* *2 hours* Used resizable form box from previous project for input form. Created a random disorder label, and in the template the amino acids that match each element of the label have a background colour of green or red for ordered or disordered prediction respectively.

### 23 Dec 2022
* *1.5 hours* Worked on CNN. Separated entire dataset and dataloader into train/validation/test datasets and dataloaders. Ran training loop with much more epochs (100), and plotted the average loss per epoch. Used trained model and test data to check the similarity of predicted protein sequences. Unsure if this similarity check has been carried out correctly.
* *0.5 hours* Saved and reloaded model.

### 24 Dec 2022
* *1 hour* Prepared a test sequence for the loaded model to be used with the Django app. Tested it with an external Python file with just the model and single sequence.

### 27 Dec 2022
* *2 hours* Following the work from 24 Dec, fitted the saved model into the Django app, and ensured the model could take its input from the Django form.

### 28 Dec 2022
* *1.5 hours* Created the django server I will use for this project. Created index view and template, protein sequence model and form using experimental web application created at the start of the winter break.
* *1 hour* Added funtionality for the website that had been worked on on 22 December and fixed problems with it.

### 29 Dec 2022
* *0.5 hour* Added work from 27 Dec into project django server (trained model making predictions being outputted to user) and merged the django app setup branch with the main repository.

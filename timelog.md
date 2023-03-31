# Timelog

* Creating a server for protein disorder prediction based on deep neural networks.
* Ryan Gregson
* 2469038G
* Kevin Bryson

## Week 0

### 19 Sep 2022
* *2 hours* Read the project guidance notes.
* *6 hours* Read over the project list.

### 21 Sep 2022
* *6 hours* Refined and submitted choices.

## Week 1

### 28 Sep 2022
* *1 hour* Project receieved and thought about what I could do from description.

### 30 Sep 2022
* *0.5 hour* Arranged meeting with supervisor.

### 2 Oct 2022
* *3 hours* Read through recommended wikipedia readings.

## Week 2

### 3 Oct 2022

* *3 hours* Read through both seed papers and made a few notes.
* *1 hour* Downloaded and reviewed project template.
* *1 hour* Wrote up some discussion bullet points for my first meeting with my supervisor, and questions about seed papers and deep learning.

### 4 Oct 2022

* *1.5 hours* Initial meeting with supervisor (Kevin) and Alexandros (similar project with protein domains). Discussed previous research published that is similar to this project, what proteins are and discussed potential first initial plans.

## Week 3

### 11 Oct 2022

* *1.5 hours* Went through the introduction lectures for the first week of the Deep Learning (M) course.
* *0.5 hour* Set-up new Google account for using Google Colab with Jupyter notebooks.
* *2.5 hours* Went through the introductory deep learning with PyTorch document: https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html.

### 13 Oct 2022

* *1 hour* Explored GraphQL documentation.

### 14 Oct 2022

* *1 hour* Met with Kevin to discuss project. Helped me get a clearer understanding of deep learning. Discussed viable technologies. 
* *1 hour* Created minutes from this which lets me see my long-term goals and what I want to complete next week.

## Week 4

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

## Week 5

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

## Week 6

### 1 Nov 2022
* *2 hours* Dataloader class trialing.

### 3 Nov 2022
* *1 hour* Wrote up Dataloader class developments and errors to discuss at the meeting.
* *1 hour* Meeting with Kevin. Discussed problems and steps for next week.
* *1 hour* Wrote up minutes after meeting

## Week 7

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

## Week 8

### 14 Nov 2022
* *2 hours* Going through 'Fully Convolutional Networks for Semantic Segmentation' paper and looking into parts I didn't understand.

### 16 Nov 2022
* *3 hours* Continuing to go through the same paper, making comparisons to my project and researching concepts I didn't understand.
* *1 hour* Meeting with Kevin. Discussed FCN paper together
* *0.5 hours* Wrote up minutes after meeting.

### 17 Nov 2022
* *1.5 hours* Experiments with conv2D on random tensors, then applying convolution to a single protein sequence.

## Week 9

### 23 Nov 2022
* *1.5 hours* Applying multiple convolutions to two protein sequences. Experimented with padding.

### 24 Nov 2022
* *2 hours* Created a loose neural network model. Multiple convolution layer, followed by activation function. Tested with two protein sequences under a training loop. Not concentrated on what training loop really doing yet - mostly assessing loss can be calculated from model output and labels.
* *2 hours* Combining previous work from Notebooks with new FCN model. All preprocessing. Now have access to more than two protein sequences.
* *1 hour* Meeting with Kevin. Discussed current model, and potential refactoring.
* *1 hour* Wrote up minutes after meeting.
* *1 hour* Cleaned up Notebook. Inserted markdown throughout notebook to help the notebook read well and be understandle. Can commit this code so far (src/Notebooks).

## Week 11

### 9 Dec 2022
* *1 hour* Refactored amino acid map so that protein images now have 20 channels. Vectorised one protein with this map. Tested a 1D convolution on this protein.
* *1 hour* Meeting with Kevin.
* *0.5 hours* Wrote up minutes after meeting.

## Week 12

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

### 4 Jan 2023
* *1.5 hours* Learnt about Docker, made a Dockerfile. Ran webapp through docker build and docker run. This is currently on an uncommitted branch.

### 7 Jan 2023
* *3.5 hours* Setup basic nginx and gunicorn alongside Docker so my webapp can be deployed. Some parts working, but some less successful. More work is needed on this setup.

## Semester 2

## Week 13

### 9 Jan 2023
* *4 hours* Read through chapter 10 of the deep learning book: "Sequence Modeling: Recurrent and Recursive Nets".

### 10 Jan 2023
* *2 hours* Watched the deep learning lectures on RNNs.
* *2 hours* Went through the lab relevant to the deep learning lecture on RNNs.

### 11 Jan 2023
* *1 hour* Created a training vs validation dataset plot. Uses the training loop and a validation loop each epoch (tested 50 epochs). Stores the total loss for training and total loss for the validation dataset each epoch and plots this. Validation plot not very readable.
* *1 hour* Tried fixing Docker setup. Setup not working with the newer, less basic setup.
* *2 hours* Created a docker compose file and got a better understanding of this Docker file and Nginx.

### 13 Jan 2023
* *2 hours* Went through lab from 10 Jan again. Tried the additional exercise of making my own RNN. This doesn't work how as I expected as with the new dataset the predictions compared to true values are very far off. I will fix this.

## Week 14

### 16 Jan 2023
* *1 hour* Worked on lab from 13 Jan seeing if I can tweak anything to improve the predictive model. Stopped and will wait to go over this with Kevin.
* *1 hour* Worked on FCN: worked on training and validation loop by increasing number of epochs and monitoring plots to understand how model is behaving (e.g., when it is overfitting). Realised I wasn't utilising the cuda GPU, so set this up to move my tensors and model onto cuda. Greatly increased training speed.
* *1 hour* Looking at disordered protein datasets and dataset augmentation techniques in deep learning as more data benefits deep learning architectures. Haven't got anything totally conclusive for dataset augmentation for my project.

### 17 Jan 2023
* *1 hour* Experimented with FCN model during training. Increased the number of layers the model had and increased regularisation up to 0.1 to see its effect on the validation dataset. Still not a very readable plot.
* *2 hours* Followed different tutorials on how to setup my docker compose and how to setup Nginx correctly. Currently have a 502 bad gateway when ran using Nginx, but without Nginx docker compose works under localhost.
* *1.5 hours* Downloaded the repository from https://testdriven.io/blog/dockerizing-masonite-with-postgres-gunicorn-and-nginx/ and took parts away from the Docker setup to see why different parts worked and why I would need them in my setup.

### 18 Jan 2023
* *1.5 hours* Continuing to break down the downloaded repository from yesterday.
* *2 hours* Moved this new broken down Dockerfile and Nginx setup to my project django server. Some libraries, such as PyTorch did not work with the setup, so fixed these issues. The setup now works as expected, and should make future deployment easier. This branch can now be merged.

### 19 Jan 2023
* *1 hour* Prepared a powerpoint for easy discussion during my meeting.
* *0.5 hours* Meeting with Kevin. Discussed progress on the project.
* *0.5 hours* Wrote up minutes after meeting.

## Week 15

### 23 Jan 2023
* *3.5 hours* Added random shuffling of Disprot dataset before allocating sequences to train/validation/test datasets. Implemented functionality to evaluate the Matthews correlation coefficient (MCC) during the training and validation loop, and over the entire test dataset.

### 24 Jan 2023
* *2 hours* Bullet pointing ideas for structure of introduction and background sections in dissertation.

### 25 Jan 2023
* *2 hours* Implemented an RNN to predict protein disorder. Currently performs quite poorly.

### 26 Jan 2023
* *1 hour* Continued bullet pointing ideas for the structure of the sections from 24 Jan.
* *1 hour* Experimented with RNN implementation, but made no progressing changes.

### 27 Jan 2023
* *1 hour* Meeting with Kevin. Discussed RNN, BCELoss, PSSM matrix from literature and encodings.
* *1 hour* Wrote up minutes after meeting.

### 29 Jan 2023
* *2 hours* Vectorised MCC computations.
* *1 hour* Tried to implement class weighting with loss function, but was unsuccessful.

## Week 16

### 30 Jan 2023
* *3 hours* Went back to the Notebook using 2D Convolutionals to see if the workflow I have learnt from the other Notebooks can be used with this model.

### 1 Feb 2023
* *2.5 hours* Wrote up introduction section of dissertation.

### 2 Feb 2023
* *2 hours* Created files with my training sequences so I can generate position-specific weight matrices (PSSMs) for input to my network.
* *2 hours* Got weighted loss function working. This required a 1x1 tensor due to the binary classification and changed loss function from BCELoss to BCEWithLogitsLoss. 

### 3 Feb 2023
* *0.5 hours* Identified test datasets papers I have reviewed are using. Namely CASP9 and CASP10 were aimed for IDR prediction. Recent papers also use Disprot and Mobi withheld test datasets.
* *1 hour* Meeting with Kevin. Discussed progress on the project.
* *1 hour* Wrote up minutes after meeting.
* *3 hours* Updated Notebooks. Removed unnecessary output of contents of datasets, starting models and their training loops.

### 4 Feb 2023
* *2.5 hours* Reread DISOPRED paper and reannotated the paper as I had a better understanding of it now. Wrote a L3 summary (from RMT) to help me review the paper in my background section.

### 5 Feb 2023
* *3.5 hours* Reread DISOPRED3 paper and reannotated the paper. Wrote a L3 summary about this paper.
* *1.5 hours* Created Dataset_preprocessing, which separates the downloading and cleaning of data from Disprot and Uniprot. Included an easier way to get an updated version of the Disprot dataset. Removed these initial preprocessing sections from my other Notebooks.

## Week 17

### 6 Feb 2023
* *2.5 hours* Wrote up background sections about CNNs and proteins.
* *0.5 hours* Updated Dataset_preprocessing to use json instead of pickle for saving files.
* *2 hours* Set up [Ray Tune](https://docs.ray.io/en/latest/tune/index.html) with FCN training loop for hyperparameter tuning. Only carried out a short experiment with the learning rate.
* *0.5 hours* Figured out how to generate a PSSM using NCBI's online resource: https://blast.ncbi.nlm.nih.gov/Blast.cgi.

### 7 Feb 2023
* *1 hour* Wrote up the background section about IDPs.
* *2.5 hours* Revised and added written background sections to the dissertation file and updated the bibliography.
* *0.5 hours* Removed testing of the model to check if it would work in the Django server, from the FCN 1D notebook. Created a separate notebook for this test.
* *1 hour* Updated RNN notebook and experimented using more epochs during training as it did not overfit with just 100 epochs.

### 8 Feb 2023
* *1.5 hours* Tried to bulk generate my PSSMs for input data. Was unsuccessful.

### 9 Feb 2023
* *1 hour* Reading about previous approaches to my problem for the Background section.
* *1 hour* Conducted an experiment between BCELoss (sigmoid included in model) and BCEWithLogitsLoss (sigmoid excluded from model), and saw no important differences in training and testing of model.
* *1 hour* Set up RayTune with LSTM Notebook for hyperparameter tuning but have not evaluated this yet.

### 10 Feb 2023
* *0.5 hours* Meeting with Kevin.
* *0.5 hours* Wrote up minutes after meeting.

### 12 Feb 2023
* *1 hour* Trying to generate a sequence alignment and pssm using HH-Suite locally (with subset database).
* *1 hour* Working with Biopython to try and read the files produced by hhblits. Unsuccessful with this.

## Week 18

### 13 Feb 2023
* *1.5 hours* Bullet pointed ideas for analysis section. Considered analysis of the supervised learning problem, dataset choice, use of batching and analysis of evaluation metrics.

### 14 Feb 2023
* *2.5 hours* Created a PSSM parser that works. Given one hhm file (MSA) generated by hhblits, can create a PSSM that is the correct shape for my models input.
* *1 hour* Made an evaluations Notebook that I will load saved models and test them. Created a confusion matrix.

### 15 Feb 2023
* *2.5 hours* Wrote analysis for the deep learning approaches, architectures and django server.
* *2.5 hours* Read and annotated paper proposing SPOT-DISORDER as I have a better understanding and will use this in my background.

### 16 Feb 2023
* *1.5 hours* Updated evaluation metric Notebook to include accuracy, precision, recall and f1 score calculations.

### 17 Feb 2023
* *1.5 hours* Meeting with Kevin. Discussed PSSMs, the Django server and datasets.
* *1 hour* Wrote up minutes after meeting.

## Week 19

### 21 Feb 2023
* *1.5 hours* From the top-down analysis points from last week, wrote the analysis for the general problem and Disprot.

### 22 Feb 2023
* *3.5 hours* Wrote analysis of labelled data, approaches, evaluation metrics and django server.
* *1 hour* Analysed homologous sequences that were generated by mmseqs. Created a possible movement of sequences between datasets.

### 23 Feb 2023
* *3 hours* Redrafting and polishing analysis written.

### 24 Feb 2023
* *0.5 hours* Meeting with Kevin.
* *0.5 hours* Wrote up minutes after meeting.
* *1 hour* Polishing analysis.

### 25 Feb 2023
* *1.5 hours* Filling out LaTeX file with analysis and ensuring BibTeX is up to date.

### 26 Feb 2023
* *1 hour* Wrote a high level overview of how my current approach section will be laid out.
* *4 hours* Generated PSSMs for all my datasets using MMSeqs2. Created a parser for getting a tensor from the PSSM file and looked at how to map the generated PSSM back to the sequence using the lookup table also generated by MMSeqs2. Have not yet made any evaluation using the deep learning models.

## Week 20

### 27 Feb 2023
* *4.5 hours* Expanded on high level overview of current approach section, and read further resources if needed.
* *2 hours* Evaluated the LSTM model with the PSSMs. Bugs to fix as one accession code (A0A0F7RL08) from the DisProt dataset redirects to the A0A6L8PPD0 accession code on the UniProt website, and this is the accession code that the PSSM lookup database uses. Therefore, using accession codes as dictionary keys could not find this PSSM. Issue has been noted and fixed by overwriting this key. Full dataloader can be looped through without causing any problems such as giving the model an empty input.

### 28 Feb 2023
* *3.5 hours* Tidied up current approach writing so far and kept writing this section.

### 1 Mar 2023
* *1 hour* Finished current approach section.
* *4.5 hours* Redrafted this section, filled it out in LaTeX and updated the BibTeX file. Created the figures in the document.

### 2 Mar 2023
* *2 hours* Read through all of the dissertation so far, making corrections if necessary. Sent these first sections to Kevin.
* *1 hour* Wrote a very rough bullet point list of what I want to include in my design and implementation sections of the dissertation.

### 3 Mar 2023
* *0.5 hours* Meeting with Kevin.
* *0.5 hours* Wrote up minutes after meeting.
* *1.5 hours* Wrote further detail for design section.
* *2 hours* Moved PSSM translation to a 2D matrix and data leakage prevention from MMSeqs2 clustering results to my data processing Notebook. This will make easier to maintain code that all of the different neural network architectures will use.

### 4 Mar 2023
* *2 hours* Finished adding further detail to bullet points for design section (still bullet format).
* *1 hour* Moved one-hot encoding of the sequences to the data processing Notebook. I think this will improve maintenance between Notebooks.
* *1 hour* Updated 1D CNN Notebook dataset class. This makes use of pre-processed one-hot encoded vectors so that we do not need separate classes for one-hot representations and PSSM representations as the get item function was different using already created PSSMs.
* *1 hour* Expanded on bullet points for implementation section.

### 5 Mar 2023
* *3 hours* Wrote up design sections for data pre-processing and training the neural networks.
* *0.5 hours* Combined PSSMs into one large file.

## Week 21

### 6 Mar 2023
* *2 hours* Wrote up design sections for the evaluation, the web server and tools and technologies. Some parts still need refined.
* *1 hour* Expanded on more bullet points for implementation section.

### 7 Mar 2023
* *1 hour* Finished bullet point expansions for implementation section.

### 8 Mar 2023
* *3.5 hours* Put together first full draft of design section.

### 9 Mar 2023
* *2 hours* Editing yesterdays first draft: sentence structure and filling in blanks.
* *1.5 hours* Identifying which blanks I cannot fill in. Noting these as questions for tomorrows meeting.
* *2.5 hours* Got all of the links for citations in design section. Built figures in dissertation design section.

### 10 Mar 2023
* *1 hour* Meeting with Kevin. Discussed design section of dissertation.
* *1 hour* Wrote up minutes after meeting.
* *0.5 hours* Filled in the blanks in the design section.
* *4 hours* Moved dataset splitting to pre-processing notebook. This makes the notebooks with the models simpler. Edited the data class for these notebooks (only updated 1D FCN so far) to make it easier to get information about protein sequences in our separate datasets after they have been sorted post homology detection and sorting in dataset preprocessing. Also experimented with loss function, but reached no real result.
* *2.5 hours* Filled the design section out in LaTeX and updated the BibTeX file.

### 11 Mar 2023
* *1.5 hours* Redrawed web server wireframes using Figma, so they could be included in the dissertation.
* *1.5 hours* Fixed bugs with data files.
* *2.5 hours* Went through RayTune and set it up to do with my current training functions.
* *1 hour* Tidied up web server. Updated one hot encoding methods in views helper, and made better data cleaner for Django form.

### 12 Mar 2023
* *2 hours* Trying to add stronger regularisation to 1D CNN model which was overfitting quickly.
* *2 hours* Restarting RayTune so that it runs. Getting the best parameters. Saving these.

## Week 22

### 13 Mar 2023
* *6 hours* Wrote up implementation section in more detail. (Regularly restarting RayTune, letting it run due to computational time/needing to be active so that Colab does not timeout).

### 14 Mar 2023
* *4.5 hours* Continued to write implementation section. Put it into LaTeX format (citations, refernces). Worked out best method to draw DNN diagrams.

### 15 Mar 2023
* *2 hours* Drew diagrams and created tables in LaTeX.
* *2 hours* Finished implementation section / finished running RayTune. RayTune has been run with every model, however, further manual parameters may need to be selected due to losing GPU priviledge and losing access to our runtime with the LSTM model.

### 16 Mar 2023
* *6 hours* Conducting evaluation, working with CASP10 data, making notes about evaluation, improving layout of Notebook.

### 17 Mar 2023
* *1 hour* Meeting with Kevin.
* *0.5 hours* Wrote up the minutes after the meeting.
* *4 hours* Continued with evaluation.
* *0.5 hours* Downloaded all files from google drive.

### 18 Mar 2023
* *6 hours* Evaluation. Editing Notebook to make visualisations clearer, creating ROC curves, trying to implement statistical tests. Also inputting information to LaTex document: filling out tables and placing images appropriately in evaluation. Wrote analysis of ROC curves and thresholding.

### 19 Mar 2023
* *4 hours* Evaluation Notebook. Changed visualisations so they fit better in the dissertation. Expanded on parts of evaluation.
* *1.5 hours* Filled and edited the written parts of the evaluation in the overleaf file.

## Week 23

### 20 Mar 2023
* *5.5 hours* Made corrections to dissertation (intro-analysis sections) and fixed poor labelling. Mostly changing/adding biology discussion and looking over Kevin's feedback. Also looked over Turnitin feedback on moodle plagiarism checker.
* *1.5 hours* Wrote missing background section: RNNs.

### 21 Mar 2023
* *3.5 hours* Working on LaTeX file. There were errors, fixed some of these. Filling in missing citations/references of new content. Generating all of the figures for evaluation as I had been using one confusion matrix multiple times until I was happy with its layout.
* *2 hours* Writing dissertation. Filling in missing sections of background.

### 22 Mar 2023
* *3 hours* Writing dissertation (filling in missing analysis) and updating LaTeX file.
* *1.5 hours* Working on web server feedback. Keeping ID with output. Tried to get the download table button working.
* *2.5 hours* Set up validation for statistical tests. Implemented Wilcoxon test given MCC values comparing features and architectures.

### 23 Mar 2023
* *2.5 hours* On evaluation notebook, created every test I will run (MCC and AUC), automated the output.
* *2 hours* Wrote up the statistical test methods for dissertation.
* *3.5 hours* Added test tables to dissertation. Discussed these when relevant.
* *2.5 hours* Aimed to evaluate CASP10 dataset against other external models. Found relevant paper. Numbers didn't add up, so modified data processing notebook. CASP10 labels correct. Got new results for CASP10 evaluation.

### 24 Mar 2023
* *5 hours* Dissertation evaluation. Recorded all new CASP10 results, updated everything in dissertation as required. Read through the evaluation section tidying parts up. Wrote comparison of external models.
* *1 hour* Dissertation editing.

### 25 Mar 2023
* *2.5 hours* Fixing bibliography. Using Google Scholar citation extension. Accessing all used websites to add last accessed date and check content still exists.
* *2.5 hours* Drafting conclusion.

### 26 Mar 2023
* *1.5 hours* Finishing conclusion and putting it into the dissertation.
* *2 hours* Tidying up web server. PNG download. Updated model.
* *1.5 hours* Wrote evaluation of web server.
* *1.5 hours* Edited dissertation.

## Week 24

### 27 Mar 2023
* *3 hours* Editing dissertation.
* *2 hours* Presentation. Started slides.

### 28 Mar 2023
* *5 hours* Presentation. Finished slides, started writing some script notes.

### 29 Mar 2023
* *6.5 hours* Presentation. Redefined slides. Added design through powerpoint.

### 30 Mar 2023
* *1 hour* Worked on feedback of evaluation section.
* *3.5 hours* Dissertation work. Formulating abstract, making corrections to red/green colour scheme. Now red/blue for colour blind accessibility.
* *2.5 hours* Presentation. Full video downloaded.

### 31 Mar 2023
* *5 hours* Tidied everything and submitted.

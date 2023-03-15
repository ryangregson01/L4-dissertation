import pickle
import json
import os
import torch 
import numpy as np
import torch.nn as nn
import torch.nn.functional as F


def get_model():
    class FCN_Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv1d(20, 10, 21, padding=10)
            self.conv2 = nn.Conv1d(10, 10, 21, padding=10)
            self.conv3 = nn.Conv1d(10, 1, 21, padding=10)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = F.relu(self.conv2(x))
            x = torch.sigmoid(self.conv3(x))
            return x

    # Loading model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    # Where cnn_net.pth has been downloaded from google colab
    model_path = STATIC_DIR+'/models/cnn_net.pth'
    loaded_model = FCN_Net()
    loaded_model.load_state_dict(torch.load(model_path))
    return loaded_model

def make_empty_channels(seq):
  seq_channels = {
    'A' : np.zeros(len(seq)),
    'C' : np.zeros(len(seq)),
    'D' : np.zeros(len(seq)),
    'E' : np.zeros(len(seq)),
    'F' : np.zeros(len(seq)),
    'G' : np.zeros(len(seq)),
    'H' : np.zeros(len(seq)),
    'I' : np.zeros(len(seq)),
    'K' : np.zeros(len(seq)),
    'L' : np.zeros(len(seq)),
    'M' : np.zeros(len(seq)),
    'N' : np.zeros(len(seq)),
    'P' : np.zeros(len(seq)),
    'Q' : np.zeros(len(seq)),
    'R' : np.zeros(len(seq)),
    'S' : np.zeros(len(seq)),
    'T' : np.zeros(len(seq)),
    'V' : np.zeros(len(seq)),
    'W' : np.zeros(len(seq)),
    'Y' : np.zeros(len(seq))
  }
  return seq_channels

def make_channels(seq):
  channeled_seq = make_empty_channels(seq)
  for i, char in enumerate(seq):
    channeled_seq.get(char)[i] = 1

  return channeled_seq

def get_vector(seq):
    channeled_seq = make_channels(seq)
    seq_vector = np.array(list(channeled_seq.values()))
    seq_vector = torch.tensor(seq_vector)
    seq_vector = seq_vector.type(torch.FloatTensor)
    return seq_vector

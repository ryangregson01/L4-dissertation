import pickle
import json
import os
import torch 
import numpy as np
import torch.nn as nn
import torch.nn.functional as F


def get_model():
  class RNN_Net(nn.Module):
    def __init__(self):
      super().__init__()
      # 20 inputs - for each amino acid
      self.input_dim = 20
      self.hidden_dim = 32
      self.num_layers = 2
      self.rnn1 = nn.LSTM(input_size=20, hidden_size=self.hidden_dim, num_layers=self.num_layers, batch_first=True, bidirectional=True)
      self.linear = nn.Linear(self.hidden_dim*2, 8)
      self.relu1 = nn.ReLU()
      self.linear2 = nn.Linear(8, 1)
      #self.sig1 = nn.Sigmoid()

    def init_hidden(self, batch_size):
      # Initialise hidden state
      return (torch.zeros(self.num_layers*2, batch_size, self.hidden_dim), 
              torch.zeros(self.num_layers*2, batch_size, self.hidden_dim))

    def forward(self, x):
      batch_size = x.size(0)
      h    = self.init_hidden(batch_size)

      y, h = self.rnn1(x,h)
      y = self.relu1(self.linear(y))
      y = self.linear2(y)
      
      return y, h
    
  # Loading model
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  STATIC_DIR = os.path.join(BASE_DIR, 'static')
  # Where DNN has been downloaded from google colab
  model_path = STATIC_DIR+'/models/server_net.pth'
  loaded_model = RNN_Net()
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

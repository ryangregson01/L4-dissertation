import pickle
import os
import torch 
import numpy as np
import torch.nn as nn
import torch.nn.functional as F


def make_empty_image(seq_len):
  img = np.array([np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len),
         np.zeros(seq_len)])
  return img

def make_image(seq):
    img_map = {
      'A' : 0,
      'C' : 1,
      'D' : 2,
      'E' : 3,
      'F' : 4,
      'G' : 5,
      'H' : 6,
      'I' : 7,
      'K' : 8,
      'L' : 9,
      'M' : 10,
      'N' : 11,
      'P' : 12,
      'Q' : 13,
      'R' : 14,
      'S' : 15,
      'T' : 16,
      'V' : 17,
      'W' : 18,
      'Y' : 19
    }

    # Makes 20 empty channels
    channeled_img = make_empty_image(len(seq))
    for i, char in enumerate(seq):
        # Updates array
        main_index = img_map.get(char)
        channeled_img[main_index][i] = 1.0

    channeled_img = torch.tensor(channeled_img)
    channeled_img = channeled_img.type(torch.FloatTensor)
    return channeled_img

def model_class():
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

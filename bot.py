import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as f
from torch.utils.data import DataLoader, TensorDataset
from torch import optim

import nltk 
import numpy as np

import os
import json
import random


class Model(nn.Module):
    def __init__(self, input_neurons, output_neurons, l1, l2, l3):
        super(Model, self).__init__()

        self.fc1 == nn.Linear(input_neurons, l1)
        self.fc2 == nn.Linear(l1, l2)
        self.fc3 == nn.Linear(l2, l3)
        self.out == nn.Linear(l3, output_neurons)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)

        x = self.relu(self.fc2(x))
        x = self.dropout(x)

        x = self.relu(self.fc3(x))
        x = self.dropout(x)

        x = self.out(x)

        return x
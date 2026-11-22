import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as f
from torch.utils.data import DataLoader, TensorDataset
from torch import optim

import nltk 
import numpy as np

import math

import os
import json
import random



class Model(nn.Module):
    def __init__(self, input_neurons, output_neurons, l1 = 64, l2 = 32, l3 = 16):
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

class Predictor():
    def __init__(self, data_location):

        self.state_date = []
   
        self.my_df = pd.read_csv(data_location)

        self.X = None
        self.y = None

        self.model = None

        self.my_df["commit_cadence"] = self.my_df["commit_cadence"].replace("frequent", 0)
        self.my_df["commit_cadence"] = self.my_df["commit_cadence"].replace("daily", 1)
        self.my_df["commit_cadence"] = self.my_df["commit_cadence"].replace("sporadic", 2)

        bool_columns = self.my_df.select_dtypes(include="bool").columns
        self.my_df[bool_columns] = self.my_df[bool_columns].astype(int)

        wanted_columns = ["number_of_commits", "active_commit_day", "project_span_days", "commit_cadence", "pct_commits_weekend", "is_forked_from_template", "author_prior_projects", "author_account_age_years"]

        self.my_df = self.my_df.loc[:, wanted_columns]

        # Will be predicting log_hours
        print(self.my_df)

    @classmethod
    def convert_log_hours_to_hours(cls, log_hours):
        return math.e ** log_hours

    @classmethod
    def combine_state_data(cls, number_of_commits, active_commit_day, project_span_days, commit_cadence, pct_commits_weekend, is_forked_from_template, author_prior_projects, author_account_age_years):
        entry = {
            "num_commits": number_of_commits,
            "active_commit_days": active_commit_day,
            "project_span_days": project_span_days,
            "commit_cadence": commit_cadence,
            "pct_commits_weekend": pct_commits_weekend,
            "is_forked_from_template": is_forked_from_template,
            "author_prior_projects": author_prior_projects,
            "author_account_age_years": author_account_age_years

        }

        return list(entry.values())

    def prepare_date(self):
        for col in self.my_df.column:
            

    def train(self, batch_size, lr, epochs):
        X_tensor = torch.tensor(self.X, dtype=torch.float32) # input array
        y_tensor = torch.tensor(self.y, dtype=torch.float32) # output for log_hours

        

        dataset = TensorDataset(X_tensor, y_tensor)
        loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

        self.model = Model(len(self.my_df.columns))




Predictor("train.csv")
"""

Values changed:
* commit_cadence
    - 0 = frequent
    - 1 = daily
    - 2 = sporadic

* any column with booleans:
    - 0 = false
    - 1 = true

"""
        
import numpy as np
import pandas as pd

df = pd.read_csv('./data/raw/marketing_campaign.csv')

df.isnull().sum()
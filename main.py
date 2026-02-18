import matplotlib.pyplot as plt
import pandas as pd

from src.cleaner import clean_data

input_path = "data/raw/messy_housing_data.csv"
output_path = "data/cleaned/housing_cleaned.csv"

clean_data(input_path, output_path)



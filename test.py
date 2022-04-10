import pandas as pd
import pytest


def test_some_func(x):
    a = x["WeightKg"]/(x["HeightCm"]/100)
    b = "Underweight" if a < 18.4 else "Normal weight" if a >= 18.5 and a <= 24.9 else  "Overweight" if a >= 25 and a <= 29.9 else "Moderately obese" if a >=30 and a <= 34.9 else "Severely obese" if a >= 35 and a <= 39.9 else "Very severely obese"
    c = "Malnutrition risk" if b == "Underweight"  else "Low risk" if b == "Normal weight" else "Enhanced risk" if b == "Overweight" else "Medium risk" if b == "Moderately obese" else "High risk" if b == "Severely obese" else "Very high risk"
    return a,b,c
def test_bmi_calculator(df):
    df[['BMI','BMI Cat','Health risk']] = df.apply(some_func,axis=1, result_type ='expand')
    df.to_json("sample2.json", orient = 'records', index = 'false')

def test_count_weight(col_name):
    return (df[df["Health risk"] == col_name]["Gender"].count())
    
df = pd.read_json("sample1.json")    
test_bmi_calculator(df)
assert test_count_weight("Very high risk") == 5
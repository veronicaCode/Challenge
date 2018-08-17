import os
import json
import argparse
import pandas as pd

def load_data(lan="en"):
    serving = pd.read_csv("data/{0}/servings_per_day-{0}_ONPP.csv".format(lan))
    food = pd.read_csv("data/{0}/foods-{0}_ONPP_rev.csv".format(lan))
    return serving, food

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Show balance diet.')
    parser.add_argument("-g", "--gender", help = "Target gender.")
    parser.add_argument("-a", "--age", help = "Target age.")
    
    args = parser.parse_args()
    serving, food = load_data()
    df = serving[(serving["gender"] == args.gender) & (serving["ages"] == args.age)]
    print df
    for x, y in zip(df["fgid"], df["servings"]):
        food_cho = food[(food["fgid"] == x)]
        print food_cho.sample(int(y))



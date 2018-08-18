import os
import json
import argparse
import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)
import pandas as pd

def load_data(lan="en"):
    serving = pd.read_csv("data/{0}/servings_per_day-{0}_ONPP.csv".format(lan), index_col=False, encoding="ISO-8859-1")
    food = pd.read_csv("data/{0}/foods-{0}_ONPP_rev.csv".format(lan), index_col=False, encoding="ISO-8859-1")
    group = pd.read_csv("data/en/foodgroups-en_ONPP.csv")
    return serving, food, group

class RequestDiet():
    
    def to_df(self, csv_path):
        df = pd.read_csv(csv_path, encoding="ISO-8859-1")
        col = df.columns
        col = [x.strip() for x in col]
        df.columns = col
        return df
    
    def print_handle(slef, msg):
        msg = msg.replace("\u00bd", " 1/2")
        msg = msg.replace("\u00bc", " 1/4")
        msg = msg.replace("\u00be", " 3/4")
        return msg
    
    
    def __init__(self):
        self.serving = self.to_df("data/en/servings_per_day-en_ONPP.csv")
        self.food = self.to_df("data/en/foods-en_ONPP_rev.csv")
        self.group = self.to_df("data/en/foodgroups-en_ONPP.csv")
    
    def request(self, request):
        try:
            meta = json.loads(request)
        
        except ValueError as e:
            return None
        
        df = self.serving[(self.serving["gender"] == meta["gender"]) & \
                     (self.serving["ages"] == meta["ages"])]
        
        food_cho = []
        for fgid, serving in zip(df["fgid"], df["servings"]):
            food_cho.append(self.food[(self.food["fgid"] == fgid)].sample(int(serving)))
        
        food_cho_df = pd.concat(food_cho)
        food_cho_df = food_cho_df.merge(self.group, on=["fgid", "fgcat_id"])
        
        reply_format = ["food", "fgcat", "srvg_sz"]
        
        response = food_cho_df.groupby(["foodgroup"])\
                              .apply(lambda x: x[reply_format].to_dict('r'))\
                              .reset_index().rename(columns={0:'serving'})\
                              .to_json(orient='records')
        
        response = self.print_handle(response)
        
        return json.loads(response.decode('utf-8'))

            


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Show balance diet.')
    parser.add_argument("-g", "--gender", help = "Target gender.")
    parser.add_argument("-a", "--age", help = "Target age.")
    
    args = parser.parse_args()
    
    get = RequestDiet()
    print get.request('{"gender": "Female", "ages": "4 to 8"}')
    
    serving, food, group = load_data()
    df = serving[(serving["gender"] == args.gender) & (serving["ages"] == args.age)]
    food_cho = []
    for x, y in zip(df["fgid"], df["servings"]):
        food_cho.append(food[(food["fgid"] == x)].sample(int(y)))
    
    food_cho_df = pd.concat(food_cho)
    col = food_cho_df.columns
    col = [x.strip() for x in col]
    food_cho_df.columns = col
    fod_cho_df = food_cho_df.drop(columns=['Unnamed: 4'])
    food_cho_df = food_cho_df.merge(group, on=["fgid", "fgcat_id"])
    reply_format = ["food", "fgcat", "srvg_sz"]
    response =  food_cho_df.groupby(["foodgroup"])\
                           .apply(lambda x: x[reply_format].to_dict('r'))\
                           .reset_index().rename(columns={0:'serving'})\
                           .to_json(orient='records')
    print json.loads(response)
    #print response.replace("\xbd", " 1/2")

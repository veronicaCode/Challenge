F_GENDER_LIST = ["female", "f"]
M_GENDER_LIST = ["male", "m"]

AGE_LIST = ["2 to 3", "4 to 8", "9 to 13", "14 to 18", "19 to 30", "31 to 50", "51 to 70", "71+"]
AGE_MAP = [3, 8, 13, 18, 30, 50, 70]


def is_valid_key(request):
    if "gender" not in request.args or "ages" not in request.args:
        return False
    else:
        return True

def is_valid_data(request):
    if request.args["gender"].lower() in F_GENDER_LIST or \
       request.args["gender"].lower() in M_GENDER_LIST:
        if request.args["ages"].lower() in AGE_LIST or \
           (request.args["ages"].isdigit() and\
           int(request.args["ages"]) >= 2):
            return True
        return False
    return False
    
def wrapper(request):
    query_data = {}
    
    if request.args["gender"].lower() in F_GENDER_LIST:
        query_data["gender"] = "Female"
    elif request.args["gender"].lower() in M_GENDER_LIST:
        query_data["gender"] = "Male"
    
    if request.args["ages"].lower() in AGE_LIST:
        query_data["ages"] = request.args["ages"].lower()
    elif request.args["ages"].isdigit():
        age = int(request.args["ages"])
        for idx, val in enumerate(AGE_MAP):
            if val >= age:
                query_data["ages"] = AGE_LIST[idx]
                break
    
    return query_data            
    
    


    
    

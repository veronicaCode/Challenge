F_GENDER_LIST = ["female", "f"]
M_GENDER_LIST = ["male", "m"]

AGE_LIST = ["2 to 3", "4 to 8", "9 to 13", "14 to 18", "19 to 30", "31 to 50", "51 to 70", "71+", "71+"]
AGE_MAP = [3, 8, 13, 18, 30, 50, 70, 120]


def is_valid_key(request):
    if "gender" not in request or "ages" not in request:
        return False
    else:
        return True

def is_valid_data(request):
    if request["gender"].lower() in F_GENDER_LIST or \
       request["gender"].lower() in M_GENDER_LIST:
        if request["ages"].lower() in AGE_LIST or \
           (request["ages"].isdigit() and \
           120 >= int(request["ages"]) >= 2):
            return True
        return False
    return False
    
def wrapper(request):
    query_data = {}
    
    if request["gender"].lower() in F_GENDER_LIST:
        query_data["gender"] = "Female"
    elif request["gender"].lower() in M_GENDER_LIST:
        query_data["gender"] = "Male"
    
    if request["ages"].lower() in AGE_LIST:
        query_data["ages"] = request["ages"].lower()
    elif request["ages"].isdigit():
        age = int(request["ages"])
        for idx, val in enumerate(AGE_MAP):
            if val >= age:
                query_data["ages"] = AGE_LIST[idx]
                break
    
    return query_data            
   

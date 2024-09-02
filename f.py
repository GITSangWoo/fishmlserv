import os 

f = __file__
print(f)

dir_name = os.path.dirname(f)
print(dir_name)

pkl_name=os.path.join(dir_name, "model.pkl")
print(pkl_name)

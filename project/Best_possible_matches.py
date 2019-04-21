
# coding: utf-8

#####################################################################################################
##instruction
'''
Maintain the folder structure:
    project:
        -.py file
        - data
        - template folder:
            -html file
        
Run .py file using command prompt
    command: python Best_possible_matches.py
    
Then hit the url (present in prompt like: http://127.0.0.1:5000/) and follow the instruction

Pass search query through the URL(atleast 3 char)
Example:
    1) http://127.0.0.1:5000/kar
    2) http://127.0.0.1:5000/rao
'''
####################################################################################################


#importing necessary library
from flask import Flask, render_template
import pandas as pd
import numpy as np
from difflib import get_close_matches 
import time
import os
#path = r'C:\Users\rajeev\Desktop'
#os.chdir(path)
#get_ipython().magic('pwd')

####################################################################################################
#loading the data
data = pd.read_csv("data.csv", error_bad_lines=False)
names = data['givenName']
names = names.dropna()
names = [i.lower() for i in names]



####################################################################################################
app = Flask(__name__)
@app.route("/")
def hello():
    return "please enter name(atleast 3 char) through url,,, thank you!!!"


# @app.route("/check/<name>")
# def check(name=None):    
#     return render_template("test.html", name=name)

@app.route("/<name>")
def namelist(name=None):    
    st = time.time()
    if len(name)>=3:
        name_list = get_close_matches(name, names ,n=10, cutoff=0.2)
        unique_wrd = []
        for i in name_list:
            if i not in unique_wrd:
                unique_wrd.append(i)
        print(time.time()-st)
    else:
        unique_wrd = "please enter atleast three character!!!"
    return render_template("test.html", name=unique_wrd)



####################################################################################################
if __name__ == "__main__": # if __name__ == "__main__":
    app.run()
else:
    print("else0.1")


import re

import glob

import os
# print(os.listdir(".\\Precis\\results\\*"))

def extract(regex, text):
    found = ""
    try:    
        m = re.search(regex, text)
        if m:
            found = m.group(1)
    except: 
        found = "" 
        
    return found
    
    
    
for file in glob.glob("results\\*"):
    with open(file, 'r') as content_file:
        content = content_file.read()
        
        benchmarks = content.split("PUT: ")
        
        print("*******")
        print(file)
            
        for putoutput in benchmarks:
        
            name = extract('===== Final Result for (.*)\s', putoutput)
            rounds = extract('rounds:\s*(\d+)\s', putoutput)
            teacher_time = extract('pex time:\s*([\d\.]+)\s', putoutput)
            learner_time = extract('learn time:\s*([\d\.]+)\s', putoutput )
            samples = extract('Samples:\s*(\d+)\s', putoutput)
            
                 = str(extract('simplified post k == 0\n(.*)\n', putoutput).count("&&") +1 )
            
            try: 
                total_time = str(round(float(teacher_time) + float(learner_time), 1))
            except: 
                total_time = ""
            
            try:
                teacher_time = str(round(float(teacher_time), 1))
                learner_time = str(round(float(learner_time), 1))
            except: 
                pass
            
            
            csv_string = ", ".join([name, rounds, samples, teacher_time, learner_time, total_time, size ])
            print(csv_string) 
    
import os

#INDEX format: 
# E_SUBJECT_UNIT_SOURCE_YEAR_REV_SOLUTIONS.filetype

sources = ["VCAA", "NEAP", "TSFX", "INSIGHT", "TSSM", "KILBAHA", "CHEMOLOGY", "STAV", "KBT", "ENGAGE", "MAV", 
            "HEFFERNAN", "AEA", "ITUTE", "LISACHEM", "FSG"]

#sources = (("VCAA", "VCAA"), ("NEAP", "NEAP"), ("TSFX", "TSFX"), ("Insight", "INSIGHT"), 
#            ("TSSM", "TSSM"), ("Kilbaha", "KILBAHA"), ("Chemology", "CHEMOLOGY"), ("STAV", "STAV"), ("KBT", "KBT"),
#            ("Engage", "ENGAGE"), ("MAV", "MAV"), ("Heffernan", "HEFFERNAN"), ("AEA", "AEA"), ("iTute", "ITUTE")
#            ("LisaChem", "LISACHEM"), ("FSG", "FSG"))

subjects = ["METHODS", "CHEMISTRY", "PHYSICS"]

filetypes = [".pdf", ".doc", ".docx"]

years = list(range(2000,2019))

#print(os.listdir("."))

for filename in os.listdir("."):
    print(filename)
    
    for subject in subjects:
        if subject in filename.upper():
            final_subject = subject
            break
        else:
            final_subject = ""

    print("Subject: " + final_subject)

    if "Unit 3" in filename:
        unit = "3"
    elif "Unit 4" in filename:
        unit = "4"
    else:
        unit = "34"
    print("Unit: " + unit)
    
    for source in sources:
        if source in filename.upper():
            final_source = source
            break
        else:
            final_source = ""
    
    print("Source: " + final_source)

    for year in years:
        if str(year) in filename:
            final_year = str(year)
            break
        else:
            final_year = ""
    print("Year: " + final_year)
    
    if "trial" in filename.lower():
        rev = 2
    else:
        rev = 1
    print("Rev: " + str(rev))
    
    sol_except = False
    if "exam and solution" in filename.lower():
        sol_except = True
    elif "solution" in filename.lower():
        sol = "_SOLUTIONS"
    else:
        sol = ""

    for filetype in filetypes:
        if filetype in filename.lower():
            final_filetype = filetype
            break
        else:
            final_filetype = ""

    try:
        if final_subject and final_source and final_year and final_filetype and not sol_except:
            new_filename = "E_" + final_subject + "_" + unit + "_" + final_source + "_" + final_year + "_" + str(rev) + sol + final_filetype
            print("Renamed " + filename + " to " + new_filename)
            os.rename(filename, new_filename)
    except FileExistsError:
        rev += 1
        

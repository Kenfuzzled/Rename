import os
import csv

#INDEX format: 
# E_SUBJECT_UNIT_SOURCE_YEAR_REV_SOLUTIONS.filetype

sources = ["VCAA", "NEAP", "TSFX", "INSIGHT", "TSSM", "KILBAHA", "CHEMOLOGY", "STAV", "KBT", "ENGAGE", "MAV", 
            "HEFFERNAN", "AEA", "ITUTE", "LISACHEM", "FSG"]

#sources = (("VCAA", "VCAA"), ("NEAP", "NEAP"), ("TSFX", "TSFX"), ("Insight", "INSIGHT"), 
#            ("TSSM", "TSSM"), ("Kilbaha", "KILBAHA"), ("Chemology", "CHEMOLOGY"), ("STAV", "STAV"), ("KBT", "KBT"),
#            ("Engage", "ENGAGE"), ("MAV", "MAV"), ("Heffernan", "HEFFERNAN"), ("AEA", "AEA"), ("iTute", "ITUTE")
#            ("LisaChem", "LISACHEM"), ("FSG", "FSG"))

subjects = [("METHODS", "MATHMETH"), ("CHEMISTRY", "CHEMISTRY"), ("PHYSICS", "PHYSICS")]

filetypes = [".pdf", ".doc", ".docx"]

years = list(range(2000,2019))

#print(os.listdir("."))


for filename in os.listdir("."):
    print(filename)
    
    exception_check = True
    while exception_check:

        #obtains subject and notes that if dealing with methods, there are 2 possible exam types
        for subject in subjects:
            if subject[0] in filename.upper():
                if subject[0] == "METHODS":
                    if "exam 1" in filename.lower():
                        final_subject = subject[1] + "1"
                        break
                    elif "exam 2" in filename.lower():
                        final_subject = subject[1] + "2"
                        break
                else:
                    final_subject = subject[1]
                    break
            else:
                final_subject = ""

        print("Subject: " + final_subject)


        #obtains the unit for the exam
        if "Unit 3" in filename:
            unit = "3"
        elif "Unit 4" in filename:
            unit = "4"
        else:
            unit = "34"
        print("Unit: " + unit)
        
        #obtains the source of the exam
        for source in sources:
            if source in filename.upper():
                final_source = source
                break
            else:
                final_source = ""
        
        print("Source: " + final_source)

        #obtains the year of the exam
        for year in years:
            if str(year) in filename:
                final_year = str(year)
                break
            else:
                final_year = ""
        print("Year: " + final_year)
        
        #if "trial" in filename.lower():
        #    rev = 2
        #else:
        #    rev = 1
        #print("Rev: " + str(rev))
        
        #checks if file is a solutions file
        sol_except = False
        if "exam and solution" in filename.lower():
            sol_except = True
        elif "solution" in filename.lower():
            sol = "_SOLUTIONS"
        else:
            sol = ""

        #obtains filetype
        for filetype in filetypes:
            if filetype in filename.lower():
                final_filetype = filetype
                break
            else:
                final_filetype = ""

        rev = 1

        try:
            if final_subject and final_source and final_year and final_filetype and not sol_except:
                new_filename = "E_" + final_subject + "_" + unit + "_" + final_source + "_" + final_year + "_" + str(rev) + sol + final_filetype
                print("Renamed " + filename + " to " + new_filename)
                os.rename(filename, new_filename)
                exception_check = False
        except FileExistsError:
            rev += 1

        #exception_check = False
        

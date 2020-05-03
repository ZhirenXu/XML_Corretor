## ask user how to continue when encounter error in xml
# @return   True/False depend on user input
def askBypass():
    print("\nIf there is attributes that can't be found in xml files, do you perfer quit the program of keep running?")
    print("Press Q to stop when encounter errors; Press B to ignore errors and keep going: ", end = "")
    key = input()
    if(key == "Q" or key == "q"):
        return False
    elif(key == "B" or key == "b"):
        return True
    

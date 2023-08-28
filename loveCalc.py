import time
import os 
import os.path
import sys
import random
import pickle
results = list()
precents = list ()


def start():
    if os.path.exists("resultsLC") == False:
        results = ["dawsonsam", "samdawson"]
        pickle.dump(results, open("resultsLC", "wb"))
        input("")
    if os.path.exists("precentsLC") == False:
       precents = [100, 100]
       pickle.dump(precents, open("precentsLC", "wb"))
    else:
        main()
    main()
    
       
def main():
    results = pickle.load(open("resultsLC", "rb"))
    precents = pickle.load(open("precentsLC", "rb"))
    calculating = bool
    calculating = False
    print("Hello welcome to my love calculator")
    time.sleep(1)
    name1 = input("Name 1: ")
    name2 = input("Name 2: ")
    print("Calculating")
    calculating = True
    secconds = 0
    while calculating == True:
        secconds += 1
        print(str(secconds) + "%")
        time.sleep(.01)
        if secconds == 100:
            result(name1, name2, results, precents)
            calculating = False
def result(n1,n2,r1,p1):
    results = r1
    precents = p1
    compatibilty = random.randrange(0, 100)
    check = str(n1+n2).lower()
    if check in results:
       resultprecent = results.index(check)
       compatibilty = precents[resultprecent]

    print(n1 + " + " + n2 + " Compatiblity " +str(compatibilty)+"%")
    if not check in results:
        results.append(check)
        precents.append(compatibilty)
        pickle.dump(results, open("resultsLC", "wb"))
        pickle.dump(precents, open("precentsLC", "wb"))
    
    

    time.sleep(1)
    end()
def end():
    a = input("again?(Y/N): ")
    a = a.upper()
    if a == "YES":
        os.system("cls")
        main()
    elif a == "Y":
        os.system("cls")
        main()
    elif a == "NO":
        sys.exit()
    elif a == "N":
        sys.exit()
    else:
        print("Please enter yes or no")
        end()
start()

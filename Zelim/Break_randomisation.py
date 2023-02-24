import csv
import math
import sys
from collections import defaultdict

def fctTempsOcc(filename,i2):
    D = {}
    with open(filename, 'r') as text_file:
        i=0
        reader = csv.reader(text_file, delimiter=';')
        for ligne in reader:
            if i>i2:
                for key,value in list(D.items()):
                    if value[0]==0:
                        del D[key]
                return D
            time = float(ligne[0])
            name = ligne[1]
            if name in D:
                avg, nb, max_time = D[name]
                avg = (avg * (nb-1) + (time-max_time)) /nb
                nb += 1
                D[name] = (avg, nb, max_time)
            else:
                D[name] = (0, 1, time)
            i+=1
    for key, value in list(D.items()):
        if value[0] == 0:
            del D[key]
    return D

def afficher(d):
    for key, value in d.items():
        print(key, ":", value)

def fctMoy(dict):
    result = {}
    avg_times = {}
    for key, value in dict.items():
        avg, nb, dT = value
        if math.floor(dT) in avg_times:
            d=avg_times[math.floor(dT)]
            d.append(key)
            avg_times[math.floor(dT)]=d
        else:
            avg_times[math.floor(dT)] = [key]

    for a,li in avg_times.items():
        nb_sum = 0
        for key in li:
            if key in dict:
                avg,nb,dT=dict[key]
                nb_sum+=nb
        for key in li:
            if key in dict:
                avg,nb,dT=dict[key]
                moy = nb / nb_sum
                result[key] = (avg, moy,math.floor(dT))

    return result

"""def fctDistance2(Dict,A,B,c):
    if(Dict[B][2]==Dict[A][2]):
        return  abs(Dict[B][1] - (Dict[A][1]) + (Dict[B][1] + Dict[A][1]) / 2) * abs((Dict[B][0] - Dict[A][0]))
        if((A=='1B:B5:91:85:11:ED' and B=='73:0D:9F:5A:5C:8E') or (B=='1B:B5:91:85:11:ED' and A=='73:0D:9F:5A:5C:8E')):
            a= c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))
            print(a)
        return c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))

    return (1 - Dict[A][1]) * (abs(Dict[B][1]) + (Dict[B][1] / 2) * abs(Dict[B][0]) + (abs(Dict[A][1]) + (Dict[A][1]) / 2) * abs(Dict[A][0]))
    return abs(Dict[B][1]) + (Dict[B][1] / 2) * abs(Dict[B][0]) + abs((Dict[A][1]) + (Dict[A][1]) / 2) * abs(Dict[A][0])"""

def fctDistance(Dict,A,B,c):
    if ((A == '1B:B5:91:85:11:ED' and B == '73:0D:9F:5A:5C:8E') or (
            B == '1B:B5:91:85:11:ED' and A == '73:0D:9F:5A:5C:8E')):
        a = c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))
        print("ICI")
        print(a)
    return c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))

def fctDistanceMin(dict,S,list,dict2,t,c):
    s = ((key,fctDistance(dict,S,key,c)) for key in list)
    dmin = min(s, key=lambda x: x[1], default=(None, float('inf')))
    if dmin[1] < t:
        print("\n")
        print("\n")
        print("\n")
        print(S)
        print(dmin)
        print("\n")
        print("\n")
        print("\n")
        dict2[S]=dict2[dmin[0]]
    else:
        dict2[S] = S
    return dict2

def compare_dictionnaires(dict1, dict2):
    non_associe=0
    bonne_assoc=0
    mauvaise_assoc=0
    for key,value in dict1.items():
        if key==value:
            non_associe += 1
        elif dict2[key] == dict2[value]:
            bonne_assoc += 1
        else :
            """print(key)
            print("\n")
            print(value)"""
            mauvaise_assoc +=1
    print("non_assoc")
    print(non_associe)
    print("\n")
    print("bonne_assoc")
    print(bonne_assoc)
    print("\n")
    print("mauvaise_assoc")
    print(mauvaise_assoc)
    print("\n")

def ouvrir(file):
    data = {}
    try:
        f = open(file, "r")
        for line in f:
            key, value = line.strip().split(';')
            data[key] = value
        f.close()
        return data
    except FileNotFoundError:
        print('Fichier introuvable')
        sys.exit(0)


def main():
    i =0
    Data = fctTempsOcc("donnee",5000)

    Data = fctMoy(Data)
    print(Data)
    Data2=ouvrir("rando_dataset_label")
    A={}
    D=[]
    print(len(Data))
    for key in Data.keys():
        A=fctDistanceMin(Data,key,D,A,0.4,7)
        D.append(key)
        i+=1
        if(i%500==0):
            print(i)
        if i>len(Data):
            raise Exception("Sorry,too much")
    compare_dictionnaires(A,Data2)



main()



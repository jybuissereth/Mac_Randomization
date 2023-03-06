import csv

text_file = open('test', 'r')
a = csv.reader(text_file)

liste=[(''.join(ligne)).split(";")[0:2]  for ligne in a ]
print(liste[0])
print("\n")


#with open("test","r") as datafile:
 #   print (datafile.read().split(";")[0:2])

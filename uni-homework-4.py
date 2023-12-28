# 4.	A beolvasott adatokból a matplotlib modul segítségével készítsen legalább 3 féle grafikont (pl. bar chart, pie chart, line chart ). Értelmezze pár mondatban a kapott ábrát.  (20pont)

print('4. feladat megoldása: ')

import csv
import sys

def read_file(file_name):
    csv_list = []

    try:
        file = open(file_name)
        try:
            file_content = csv.reader(file)

            for row in file_content:
                csv_list.append(row)
        finally:
            file.close()
    except OSError:
        sys.exit('Hiba a fájl kezelése közben!')
    else:
        return csv_list

database = read_file('phones.csv')


def get_datas(original_list, phone_type):
    new_list = []
    for lists in original_list:
        if phone_type in lists:
            for piece in lists:           
                piece = 1
                new_list.append(piece)
    return len(new_list)

def print_datas(data, phone_type):   
    print(phone_type + ' eladott darabszáma: ' + str(data)) 
                        
phone_type_1 = 'Nokia'       
phone_type_2 = 'ALCATEL'  
phone_type_3 = 'Motorola'   
phone_type_4 = 'Apple'       
phone_type_5 = 'ZTE'     
phone_type_6 = 'Honor'

print_datas(get_datas(database, phone_type_1), phone_type_1)
print_datas(get_datas(database, phone_type_2), phone_type_2)
print_datas(get_datas(database, phone_type_3), phone_type_3)
print_datas(get_datas(database, phone_type_4), phone_type_4)
print_datas(get_datas(database, phone_type_5), phone_type_5)
print_datas(get_datas(database, phone_type_6), phone_type_6)

phone_types = [phone_type_1, phone_type_2, phone_type_3, phone_type_4, phone_type_5, phone_type_6]
sold = [get_datas(database, phone_type_1), get_datas(database, phone_type_2), get_datas(database, phone_type_3), get_datas(database, phone_type_4), get_datas(database, phone_type_5), get_datas(database, phone_type_6)]

piechart_datas = []

def sum_for_piechart(list):
    sum = 0
    for elements in list:
        sum += elements
    return sum

def datas_for_piechart(list, new_list, sum):
    for elements in list:
        percent = (elements / sum)*100
        new_list.append(percent)
    return new_list

datas_for_piechart(sold, piechart_datas, sum_for_piechart(sold))


import matplotlib.pyplot as plt
import numpy as np

# barchart, amely oszlopdiagrammon ábrázolja az egyes telefontípusok egymáshoz viszonyított eladási adatait:

x = np.array(phone_types)
y = np.array(sold)
plt.bar(x, y, color = "green")
plt.show()


#linechart, amely vonaldigrammon ábrázolja az egyes telefontípusok egymáshoz viszonyított eladási adatait:

x = np.array(phone_types)
y = np.array(sold)

plt.plot(x, y, marker = '*', ms = 20, mfc = 'r', linestyle = 'dotted')

plt.xlabel("Phone type")
plt.ylabel("Sold")

plt.show()



# piechart, amely kördiagrammon ábrázolja az egyes telefontípusok egymáshoz viszonyított eladási adatait:

y = np.array(piechart_datas)
mylabels = phone_types

plt.pie(y, labels = mylabels)
plt.show() 


    

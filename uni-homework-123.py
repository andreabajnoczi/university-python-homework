# 1.	Hozzon létre egy tetszőleges adatokat tartalmazó csv állományt. Lehet fiktív adat vagy a KSH, Felvi stb oldalakról származó szabadon hozzáférhető adat. (10pont)
# 2.	A Python csv modul használatával olvassa be az adatokat. Ellenőrzésnek írja ki a képernyőre az adathalmaz első 5 sorát. (10 pont)
# 3.	Egy tetszőleges kiválasztott adatsort (oszlopot) elemezzen Python segítségével. Írja ki a változó átlagát, minimum és maximum értékét, szórását és közép értékét.  (10pont)
# 4.	A beolvasott adatokból a matplotlib modul segítségével készítsen legalább 3 féle grafikont (pl. bar chart, pie chart, line chart ). Értelmezze pár mondatban a kapott ábrát.  (20pont)

# 1. feladat megoldása külön fájlban: phones.csv

print('2. feladat megoldása: ')

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

print(read_file('phones.csv')[0:5])


print('3. feladat megoldása: ')

database = read_file('phones.csv')
                     
alcatel_price_list = []

def get_price_list(original_list, new_list, phone_type):
    for lists in original_list:
        if phone_type in lists:
            for price in lists:           
                price = float(lists[5])
                new_list.append(price)
    return new_list   

get_price_list(database, alcatel_price_list, 'ALCATEL')


def get_min_max(list):
    print('A legalacsonyabb ár: ' + str(min(list)))
    print('A legmagasabb ár: ' + str(max(list)))

get_min_max(alcatel_price_list)  


def get_sum(list):
    sum = 0

    for element in list:
        sum += int(element)
    return sum

def get_average(list, sum):
    average = sum / len(list)
    return average

print('Az átlagos ár: ' + str((get_average(alcatel_price_list, get_sum(alcatel_price_list)))))


def get_defraction(list):
    sum = 0
    index = 0

    while index < len(list):
        sum = sum + (list[index] - get_average(alcatel_price_list, get_sum(alcatel_price_list)))**2
        index += 1
    
    defraction = (sum / len(list)) **0.5
    return defraction

print('A lista szórása ' + str(get_defraction(alcatel_price_list)))



def change_numbers(list):
    for previous_element in range(len(list)-1):
        for next_element in range(previous_element+1, len(list)):
            if list[previous_element] > list[next_element]:
                list[previous_element], list[next_element] = list[next_element], list[previous_element]
    return list 

def get_median(list):
    new_list = change_numbers(alcatel_price_list)
    
    if len(list) %2 != 0:
        index = len(list)/2
        print(new_list[index])
    else:
        index_1 = int(len(list)/2-0.5)
        index_2 = int(len(list)/2+0.5)
        number_1 = new_list[index_1]
        number_2 = new_list[index_2]
        median = (number_1 + number_2)/2
        return median

print('A lista mediánja: ' + str(get_median(alcatel_price_list)))


print('4. feladat megoldása másik fájlban. ')

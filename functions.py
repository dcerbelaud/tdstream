#!/usr/bin/python
# -*-coding:utf-8 -*

import csv,codecs

def append_to_file(buf,file_name):
    with open(file_name,"a") as file:
        file.write(buf)

def load_points_from_csv(csv_file):
    with codecs.open(csv_file, 'rb',encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        list_points = []
        for row in reader:
            list_points.append(row)
        file.close()
        return list_points

def append_to_csv(data_list,csv_file):
    with codecs.open(csv_file,'ab',encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(data_list)
        file.close()

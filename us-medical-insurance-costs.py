#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:45:40 2021

@author: fredjohnson
"""
import csv

#Extracting information from the csv file and saving it as a list of dictionaries
with open('insurance.csv', newline = '') as insurance_csv:
    dictionary = csv.DictReader(insurance_csv)
    data = list(dictionary)
    
#Add the ID tag to each entry to allow for updating
id_no = 0
for entry in data:
    entry['id'] = id_no
    id_no += 1
    
    
#Count the number of people, the number of males, and the number of females
total_count = len(data)
male_count = 0
female_count = 0
for entry in data:
    if entry['sex'] == 'male':
        male_count += 1
    else:
        female_count += 1
    
#Calculating averages and totals
def average_age(data):
    total_age = 0
    for entry in data:
        total_age += int((entry['age']))
    return total_age/total_count

def average_bmi(data):
    total_bmi = 0
    for entry in data:
        total_bmi += float((entry['bmi']))
    return total_bmi/total_count

def average_cost(data):
    total_cost = 0
    for entry in data:
        total_cost += float((entry['charges']))
    return total_cost/total_count
    
def count_smokers(data):
    count = 0
    for entry in data:
        if entry['smoker'] == 'yes':
            count += 1
    return count
count_non_smokers = total_count - count_smokers(data)

def count_region(inp):
    count = 0
    for entry in data:
        if entry['region'] == inp:
            count += 1
    return "The number of people living in the {} is {}".format(inp, count)

#Calcualting the insurance costs
def estimated_insurance_cost(age, sex, bmi, children, smoker):
    if sex == "male":
        gend = 1
    else:
        gend = 0
    if smoker == 'yes':
        smok = 1
    else:
        smok = 0
    estimated_cost = 250 * age - 128 * gend + 370 * bmi + 425 * children + 24000 * smok - 12500
    return estimated_cost

#Create a patient class for updating and adding records
class Patient:
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.id_no = len(data)
    
    #creating a dictionary for the patient and adding it to the dataset
    def add_to_data(self):
        patient_information = {}
        patient_information["age"] = self.age
        patient_information["sex"] = self.sex
        patient_information["bmi"] = self.bmi
        patient_information["children"] = self.children
        patient_information["smoker"] = self.smoker
        patient_information["region"] = self.region
        patient_information["charges"] = estimated_insurance_cost(self.age, self.sex, self.bmi, self.children, self.smoker)
        patient_information["id"] = self.id_no
        data.append(patient_information)

#Updating values
def update_age(id_no, new_age):
    print("The new age is " + str(new_age))
    #Editing the value in the dataset
    for entry in data:
        if entry['id'] == id_no:
            entry['age'] = new_age
            entry['charges'] = estimated_insurance_cost(new_age, entry['sex'], entry['bmi'], entry['children'], entry['smoker'])
                
def update_bmi(id_no, new_bmi):
    print("The new bmi is " + str(new_bmi))
    for entry in data:
        if entry['id'] == id_no:
            entry['bmi'] = new_bmi
            entry['charges'] = estimated_insurance_cost(entry['age'], entry['sex'], new_bmi, entry['children'], entry['smoker'])

def update_smoker(id_no, new_smoker):
    for entry in data:
        if entry['id'] == id_no:
            entry['smoker'] = new_smoker
            entry['charges'] = estimated_insurance_cost(entry['age'], entry['sex'], entry['smoker'], entry['children'], new_smoker)
    
def update_children(id_no, new_children):
    print("The new number of childre is " + str(new_children))
    for entry in data:
        if entry['id'] == id_no:
            entry['children'] = new_children
            entry['charges'] = estimated_insurance_cost(entry['age'], entry['sex'], entry['smoker'], new_children, entry['smoker'])
    
def update_region(id_no, new_region):
    for entry in data:
        if entry['id'] == id_no:
            entry['region'] = new_region
            
#Output all the averages
def update_counts():
    print("The average age for the dataset is {}".format(average_age(data)))
    print("The average BMI for the dataset is {}".format(average_bmi(data)))
    print("The number of smokers is {}".format(count_smokers(data)))
    print("The number of non-smokers is {}".format(count_non_smokers))
    print("The average insurance cost for the dataset is {}".format(average_cost(data)))

#Query how many people live in a specific region
print(count_region('northwest'))

#Adding a new patient to the dataset as a class object
Fred = Patient(20, 'male', 23.1, 0, 'no', 'southeast')
Fred.add_to_data()
Kathy = Patient(50, 'female', 29.1, 4, 'no', 'northwest')
Kathy.add_to_data()

#Updating a patients records using their ID
update_age(1338, 46)
print(data)
update_counts()
import numpy as np
import csv

def find_total_visits():
    visit_counter = 0
    # parse each file (3)
    for week_number in range(1, 4):
        file_path = f"./files/week-{week_number}.csv"
        
        # opened each file and extracted data for each row as an object
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # sum every " 1" and update counter
                days_of_week = [' S', ' M', ' T', ' W', ' Th', ' F', ' S']
                visits_list = [int(row[day]) for day in days_of_week]
                visit_counter += sum(visits_list)

    # return sum
    return visit_counter

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")
ex2()


people_list = [
    {'name': 'alice', 'age': 20},
    {'name': 'dave', 'age': 29}
]

new = [person['age'] for person in people_list]
# print(new)

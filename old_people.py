"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import sqlite3
import os
from create_db import db_path, script_dir
import pandas as pd

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Getting People Data from the Database"
    conn = sqlite3.connect(db_path) 
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM people where age > 50 or age = 50')
    all_people = cursor.fetchall()
    L =[]
    for i in all_people:
        T = (i[1],i[7])
        L.append(T)

    conn.commit() 
    conn.close()
    return L

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # TODO: Create function body
    # Hint: Use a for loop to iterate the list of tuples to print a sentence for each old person
    for i in name_and_age_list:
        print(f"{i[0]} is {i[1]} years old.")
    return

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # TODO: Create function body
    # Hint: In Lab 3, we converted a list of tuples into a pandas DataFrame and saved it to a CSV file
    df = pd.DataFrame(name_and_age_list, columns=['Name', 'Age'])
    df.to_csv(csv_path, index=False)
    return

if _name_ == '_main_':
   main()
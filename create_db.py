"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    create_ppl_tbl_query = """ CREATE TABLE IF NOT EXISTS people 
    ( 
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL, 
    address TEXT NOT NULL, 
    city TEXT NOT NULL, 
    province TEXT NOT NULL, 
    bio TEXT, 
    age INTEGER, 
    created_at DATETIME NOT NULL, 
    updated_at DATETIME NOT NULL 
    
    ); 
    """
    
    cursor.execute(create_ppl_tbl_query)
    conn.commit()
    conn.close()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    
    fake = Faker("en_CA")

    insert_query = """
        INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
    for _ in range(200):

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        nm = fake.name()
        email_id = fake.email()
        addr = fake.address()
        city = fake.city()
        province = fake.administrative_unit()
        bio = fake.word(ext_word_list=['Quite and Calm', 'Smart and Detail-oriented Person', 'Enjoys making funny sounds when talking.', 'Lovable and Kind'])
        age = fake.random_int(min=18, max=80)
        created_at = datetime.now()
        updated_at = datetime.now()
        
        new_person = (nm, email_id, addr, city, province, bio, age, created_at, updated_at)
        cursor.execute(insert_query, new_person)
    
    
        conn.commit()
        conn.close()
        
    return

if __name__ == '__main__':
   main()
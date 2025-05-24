#!/usr/bin/env python3
import os
import sys
import json
from datetime import *

def add():
    try:
        file = open("tasks.json", "r+")
    except FileNotFoundError:
        file = open("tasks.json", "w+")
    except Error as e:
        print(f"Err: {e}")

    if os.path.getsize("tasks.json") == 0:
        id = 1
        tasks = []
        desc = input("Description of task: ")
        stat = "To-Do"
        date_now = datetime.now()
        date = date_now.strftime("%b %d %Y %H:%M:%S") 
        update = date
        data = {
            "ID":id,
            "Description":desc,
            "Status":stat,
            "Date":date,
            "Date Updated":update}
        tasks.append(data)
        json.dump(tasks, file, indent = 4)
        print("\n")
    else:
        read_file = open("tasks.json", "r")
        read_data = json.load(read_file)
        id = len(read_data) + 1
        desc = input(f"Description of task[{id}]: ")
        stat = "To-Do"
        date_now = datetime.now()
        date = date_now.strftime("%b %d %Y %H:%M:%S") 
        update = date
        data = {
            "ID":id,
            "Description":desc,
            "Status":stat,
            "Date":date,
            "Date Updated":update}
        read_data.append(data)
        json.dump(read_data, file, indent = 4)
        print("\n")

def update():
    pass

def delete():
    pass
 
def listAll():
    file = open("tasks.json", "r")
    if os.path.getsize("tasks.json") == 0:
        print("List is Empty!")
    else:
        read_data = json.load(file)
        for _ in range(len(read_data)):
            print("ID: ", read_data[_].get("ID"))
            print("Description: ", read_data[_].get("Description"))
            print("Status: ", read_data[_].get("Status"))
            print("Date-Created: ", read_data[_].get("Date"))
            print("Date-Updated: ", read_data[_].get("Date Updated"))
            print("\n")        
        print("\n")
   

def listDone():
    pass

def listNotdone():
    pass

def listLive():
    pass




print("TaskManCLI v1.0")
while True:
    print("Enter Operation to perform")
    des = input("\n1.Add Task\n2.List All Tasks\n3.Coming Soon..\n")
    try:
        if 1 == int(des) :
            add()
        elif 2 == int(des):
            listAll()
        else:
            break
    except ValueError:
        print("Invalid Option!!")
        print("\n")


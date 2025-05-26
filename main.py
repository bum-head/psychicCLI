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
    print("TO UPDATE DESCRIPTION \n \'update-desc [task-id] [updated-description]\'") #print the syntax of how to type the command
    print("TO UPDATE TASK-PROGRESS \n Type progress,done and ndone as your task-state \n \'update-task [task-id] [updated-task-state]\'") #prints the syntax of updating tasks 

    print("TO EXIT TYPE \'back\'") #show other options eg. exit update function


    update_i = input().split()
    print("")

    if update_i[0] == "update-desc":
        try:
            file = open("tasks.json", "r+")
            read_data = json.load(file)
            new_file = open("temp.json", "w+")
            for _ in read_data:
                if _.get('ID') == int(update_i[1]):
                    _["Description"] = update_i[2]
            json.dump(read_data, new_file, indent = 4)
            os.remove("tasks.json")
            os.rename("temp.json", "tasks.json")
        except FileNotFoundError:
            print("Are you sure you have created a task to modify it ?")
        except Error as e:
            print(f"Err: {e}")

    elif update_i[0] == "update-task":
        try:
            file = open("tasks.json", "r+")
            read_data = json.load(file)
            new_file = open("temp.json", "w+")
            for _ in read_data:
                if _.get("ID") == int(update_i[1]):
                    if update_i[2] == "progress":
                        _["Status"] = "In-Progress"
                    elif update_i[2] == "done":
                        _["Status"] = "Done!"
                    elif update_i[2] == "ndone" or "notdone":
                        _["Status"] = "To-Do"
                    else:
                        print("Incorrect option")
            json.dump(read_data, new_file, indent = 4)
            os.remove("tasks.json")
            os.rename("temp.json", "tasks.json")
        except FileNotFoundError:
            print("Are you sure you have created a task to modify it ?")
        except Error as e:
            print(f"Err: {e}")


    elif update_i == "back":
        return
    else:
        print("Invalid option!\n Please refer to the instructions")


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
    des = input("\n1.Add Task\n2.List All Tasks\n3.Update Tasks\n4.Exit\n")
    print("")
    try:
        if 1 == int(des) :
            add()
        elif 2 == int(des):
            listAll()
        elif 3 == int(des):
            update()
        else:
            break
    except ValueError:
        print("Invalid Option!!")
        print("\n")



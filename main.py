from bs4 import beautifulsoup
import pandas as pd 
import requests
import csv

def link_manager():
    global url
    url = input("paste your link hear : ")

def request_handler():
    while True:
        link = request.get(url)
        soup = Beautifulsoup(link.text,"html.parser")

def find_all():
    the_id = input("what is the id:")
    room = input("class = ")

    find= soup.findAll(f"id={the_id}, attrs ={"class":{room}}")

def convert_to_csv():
    choice = input("do you want it as a csv file? (y/n)")
    if choice == y:
        file_name = input("write you file name: ")
        

link_manager()
request_hander()
find_all()
convert_to_csv()

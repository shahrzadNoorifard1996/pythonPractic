from  insert import *
from delete import *
from select import *
from update import *

def print_menu():
    print("1.show customer")
    print("2.add customer")
    print("3.remove customer")
    print("4.update customer")
    print("5.quit")
    print("6.any key showing menu")
    print()

def insercustomer():
    print("add customer...:")
    customername=input("FirstName: ")
    customerfamily = input("LastName: ")
    nationalcode = input("NationalCode: ")
    insert(customername,customerfamily,nationalcode)

def selectcustomer():
    print("customer.....:")
    select()

def updatecustomers():
    print("update.....:")
    nationalcode=input("NationalCode: ")
    customername=input("CustomerName: ")
    update(customername,nationalcode)

def deletecustomer():
    print("delete.....:")
    nationalcode=input("National code: ")
    delete(nationalcode)

menu_choice=0
print_menu()
while menu_choice !=5:
    menu_choice=input("select between 1 to 5 : ")
    if menu_choice =="1":
        selectcustomer()
    elif menu_choice=="2":
        insercustomer()
    elif menu_choice=="3":
        deletecustomer()
    elif menu_choice=="4":
        updatecustomers()
    elif menu_choice=="5":
        break
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:05:09 2022

@author: garim
"""

from tabulate import tabulate
import os
from tkinter import Tk, filedialog

def main_menu(): 
    print("____________________________________________:PLAGIARISM DETECTION APP:_______________________________________________")
    print("\n\n")
    print("\t\t\t MAIN MENU:\n")
    print("\t\t\t 1: Compare two texts\n \t\t\t 2: Compare two text files\n \t\t\t 3.Compare all the files present in the folder")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        two_texts()
    elif choice==2:
        two_files()
    elif choice==3:
        folder()
    else:
        print("Wrong input.")
        
def w_shinglings(string,shingle_size):
 token=[i for i in string.split()]
 TOKEN=[]
 unique_token=[]
 for i in range(len(string)-shingle_size):
     if len(token[i:i+shingle_size])<shingle_size:
         break
     TOKEN.append(token[i:i+shingle_size])
     [unique_token.append(x) for x in TOKEN if x not in unique_token]
 return unique_token

def intersection(lst1, lst2):
 lst3 = [item for item in lst1 if item in lst2]
 return lst3

def union_(list1,list2):
 list_sum=list1+list2
 final_list=[]
 [final_list.append(x) for x in list_sum if x not in final_list]
 return final_list

def similarity(file_1,file_2,shingle_size):
 w_shingling1=w_shinglings(file_1, shingle_size)
 w_shingling2=w_shinglings(file_2, shingle_size)
 shingling_intersection=intersection(w_shingling1, w_shingling2)
 shingling_union=union_(w_shingling1,w_shingling2)
 similarity_index=len(shingling_intersection)/len(shingling_union)
 return similarity_index
 

def two_texts():
 string1=input("Enter the first text.")
 string2=input("Enter the second text.")
 similarity_max=similarity(string1, string2,4)
 if similarity_max==0:
     plagiarism_status="NOT PLAGIARISED"
 elif similarity_max>=0.5:
     plagiarism_status="PLAGIARISED"
 elif similarity_max>0.2 and similarity_max<0.5:
     plagiarism_status="PARTIALLY PLAGIARISED"
 else:
     plagiarism_status="NOT PLAGIARISED"
 print("\n\tEntered two contents are ",similarity_max*100,"% similar, so we conclude its",plagiarism_status)
 
def two_files():
 from tkinter.filedialog import askopenfilename
 print("Select the first file: ")
 path1 = askopenfilename()
 file1=open(path1,"r")
 string1=file1.read()
 print("Select the second file: ")
 path2 = askopenfilename()
 file2=open(path2,"r")
 string2=file2.read()
 similarity_max=similarity(string1, string2,4)
 if similarity_max==0:
     plagiarism_status="NOT PLAGIARISED"
 elif similarity_max>=0.5:
     plagiarism_status="PLAGIARISED"
 elif similarity_max>0.2 and similarity_max<0.5:
     plagiarism_status="PARTIALLY PLAGIARISED"
 else:
     plagiarism_status="NOT PLAGIARISED"
 print("\n\n Provided two files are ",similarity_max*100,"% similar, so we conclude its",plagiarism_status)
 file1.close()
 file2.close()
 
def folder():
 root = Tk() # pointing root to Tk() to use it as Tk() in program.
 root.withdraw() # Hides small tkinter window.
 root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
 path= filedialog.askdirectory() # Returns opened path as str
##path = r"C:\Users\garim\plagiarism_project" 
 # Change the directory
 os.chdir(path)
 file_path=[]
 for file in os.listdir():
 # Check whether file is in text format or not
   if file.endswith(".txt"):
      file_path.append(f"{path}\{file}")
      file_names_list=os.listdir(path)
       #Function gives w-shinglings for the selected file. 
 mydata_list=[]
 for i in range(0,len(file_path)): 
    file_name1=file_path[i]
    for j in range(i+1,len(file_path)):
        file_name2=file_path[j]
        file1=open(file_name1,"r")
        string1=file1.read()
        file2=open(file_name2,"r")
        string2=file2.read()
        similarity_max=similarity(string1, string2,4)
        if similarity_max==0:
           plagiarism_status="-"
        elif similarity_max>=0.5:
           plagiarism_status="PLAGIARISED"
        elif similarity_max>0.2 and similarity_max<0.5:
           plagiarism_status="PARTIALLY PLAGIARISED"
        else:
           plagiarism_status="NOT PLAGIARISED"
        mydata_list.append([file_names_list[i],file_names_list[j],similarity_max,plagiarism_status]) 
        file1.close()
        file2.close() 
 head=["file1","file2","maximum similarity","Plagiarism status"]
 print("Similarity Results:")
 print(tabulate(mydata_list, headers=head, tablefmt="grid"))
while True:
   main_menu()
   return_menu=input(" Return to main menu? (y/n): ")
   if return_menu=='y':
     pass
   else:
     break
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 00:06:57 2022

@author: premjethwa
Name : Prem Atul Jethwa
UTA ID : 1001861810
"""

class Employee:
    def __init__(self,name,ID_number,department,job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    def get_name(self):
        return self.__name
        
    def get_ID_number(self):
        return self.__ID_number
        
    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title
    
    def __str__(self):
        return "Name: " + self.__name + \
               "\nID_Number: " + self.__ID_number + \
               "\nDepartment: " + self.__department + \
               "\nJob_Title: " + self.__job_title    
    



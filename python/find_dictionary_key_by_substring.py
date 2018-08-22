#!/bin/python3

import math
import os
import random
import re
import sys

Contacts = {}
def addContact(c):
    global Contacts
    for i in range(0, len(c)+1):
        s = c[0:i]
        if s not in Contacts.keys():
            Contacts[s] = []
        Contacts[s].append(c)

if __name__ == '__main__':
    global Contacts
    n = int(input())

    #contacts = []
    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]
        """
        if op == "add":
            contacts.append(contact)
        elif op == "find":
            print(len([k for k in contacts if contact in k]))
        """
        if op == "add":
            addContact(contact)
        elif op == "find":
            print(len(Contacts[contact]) if contact in Contacts.keys() else 0)            
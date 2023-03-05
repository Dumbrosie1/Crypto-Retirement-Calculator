# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:41:04 2023

@author: mail
"""

import requests
import re
def Ether_bal(add):
    url = ("https://api.parsiq.net/balances/eip155-1/v1/addresses/" + add + "/tokens?limit=100")
    #url = ("https://api.parsiq.net/balances/eip155-1/v1/addresses/0x048600E5e11B553121dFdD7a2a3216aFA63ad375/tokens?limit=100")
    # Used for testing specific wallet addresses 

    headers = {
        "accept": "application/json",
        "authorization": "Bearer aAm2zpscrpPo8GOCMNBOnRHgHwuwXmlg"
        }

    response = requests.get(url, headers=headers)
    

        
    bal = response.text[129:140:1]
    #print(response.text) Used to review the Parsiq response
    
    print(bal)
    #bal = "10000" Used for testing specific balance values 
    
    return bal

def Ether_bal(add):
    url = ("https://api.parsiq.net/balances/eip155-1/v1/addresses/" + add + "/tokens?limit=100")
    #url = ("https://api.parsiq.net/balances/eip155-1/v1/addresses/0x048600E5e11B553121dFdD7a2a3216aFA63ad375/tokens?limit=100")
    # Used for testing specific wallet addresses 

    headers = {
        "accept": "application/json",
        "authorization": "Bearer aAm2zpscrpPo8GOCMNBOnRHgHwuwXmlg"
        }

    response = requests.get(url, headers=headers)
    

        
    bal = response.text[129:140:1]
    #print(response.text) Used to review the Parsiq response
    
    print(bal)
    #bal = "10000" Used for testing specific balance values 
    
    return bal
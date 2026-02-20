# program to fill in a letter template given below with name and date 

Letter ='''<|Name|>,
         you are selected 
         <|Date|>'''

print(Letter.replace("<|Name|>","sudeep").replace("<|Date|>", "20 Feb 2026"))
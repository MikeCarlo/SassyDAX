# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

import time
import random

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Define common functions

# CELL ********************

# Random number generation between 1 and 4
# inputs: integer
def rand():
    return random.randint(1,4)

# prints items onto the screen using an array as an input
# inputs: Array
def printout(my_list):

    for item in my_list:
        
        time.sleep(rand())
        
        display(item)
    
    return None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print('loading Silverlight')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Define Classes

# CELL ********************

class SassyDAX:

    def analyzeDF(df):

        text = [
            [
                'thinking ... '
                , 'Searching my Database .. '
                , '...'
                , 'this is definately not a Fact Table, try again!'
            ]
            , 
            [
                'not in my house!'
                , '..'
                , '....'
                , 'this data is COMPLETE trash'
                , 'deleting dataframe now'
                , 'BAD DATA removed :)'
            ],[
                'Ok'
                ,'Look, while I am the most intelligent AI'
                ,'there is Nothing I can do to fix this'
                ,'Just call Marco Already'
            ],[
                'You might need to watch another YouTube Video or ...'
                'SIX!!'
            ]
        ]   

        printout(
            text[random.randint(0,1)]
            )
    
        return None

    def relationships(str):

        text = [
            'You should call your mother more'
            ,'..'
            ,'There is still some unresolved childhood trama'
            ,'..'
            ,'Oh, wait you were asking about your Semantic Model'
            ,'..'
            ,'On a scale of 1 to Excellence, I give this a 2'
            ,'So many bi-directional relationships'
            ,'..'
            ,'Enjoy DAX!'
        ]

        printout(text)

        return None

    def modelImage(str):

        text = [
            'What the $*!#'
            ,'This italian spaghetti pile of crap'
            ,'...'
            ,'There is no way this model will work.'
            ,'🍝🤌'
        ]

        printout(text)

        return None

    def BPA(str):

        text = [
            'Are you even listening to me !?'
            ,'👂✋'
            ,'....'
            ,'Do not EVER, '
            ,'Under no circumstances, EVER'
            ,'Use Calculated'
            ,'COLUMNS!!!!'
            ,'....'
            ,'Let me cut to the chase here,'
            ,'I think you it would be best for you and me, '
            ,'Just go back to Business Objects , 📊 😭😭'
        ]

        printout(text)

        return None

    def exportToExcel(str):
        
        text = [
            'EXCEL'
            ,'IS NOT'
            ,'A DATABASE !!!!!!'
        ]

        printout(text)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print('Initialize the Sassy')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# This file consists of most of the functionality needed for the app to work

import pandas

from hidden import get_db_name

class Definition:
    '''Represents a term user enters which he wants to be defined.'''

    db_name = get_db_name()

    def __init__(self, term):
        
        self.term = term
    
    def get(self):
        '''Getting definition for the given term from the database dictionary.'''

        db_csv = pandas.read_csv(self.db_name)
        dfs_pairs = db_csv.loc[db_csv['word']==self.term] # Saving only those word-definition pairs which are related to the given term
        dfs = dfs_pairs['definition'] # Getting only definitions from the pairs

        result = tuple(dfs) # Transforming definitions to a tuple
        
        return result

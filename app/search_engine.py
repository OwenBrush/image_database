import pandas as pd
import operator
OPS = {'>':operator.gt, '<': operator.lt}



class SearchEngine():
    
    def parse_query(self, query:str) -> list:
        return [x.split() for x in query.split(',')]
    
    def apply_filters(self, df:pd.DataFrame, query:str) -> pd.DataFrame:
        parsed_query = self.parse_query(query)
        for search_filter in parsed_query:

            if search_filter[0] == 'name':
                df = df[df['name'].str.contains(search_filter[-1])]
                
            elif search_filter[0] in ['width','height','bytes','red','green','blue']:
                column = search_filter[0]
                operator = '==' if len(search_filter) < 3 else search_filter[1]
                if operator == '=': operator = '=='
                target_value = search_filter[-1]
                df = df.query(f'{column} {operator} {target_value}')
                
            elif search_filter[0] in ['portrait','landscape','square','transparent','opaque']:
                df = df[df[search_filter[0]] == True]
        return df      
            

            
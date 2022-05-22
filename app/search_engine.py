


class SearchEngine():
    
    def parse_query(query:str) -> list:
        return [x.split() for x in query.split(',')]
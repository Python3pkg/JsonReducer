"""
    Reduce data

    DEPENDENCIES:
        * collections
"""
import collections

def reduce(data):
    merged_array = {}

    if isinstance(data, list):
        for i in data:  
            for k, v in i.iteritems():
                v = reduce(v)
                if k in merged_array:
                    merged_array[k].append(v)
                else:
                    merged_array[k] = [v]
    elif isinstance(data, dict):
        for k, v in data.iteritems():
            v = reduce(v)
            if k in merged_array:
                merged_array[k].append(v)
            else:
                merged_array[k] = [v]
    else:
        return data

    return merged_array

#arr = json.loads('{"data":[{"id":1,"name":"JesusEmanuel","lastname":"LozanoMaltos"},{"id":2,"name":"Gilberto","lastname":"Reyes Barrera","extra":[{"A":1},{"A":2}]}]}')
#arr = [{"id":1,"name":"Rodolfo","username":"rodolfo95"},{"id":2,"name":"Pedro","username":"pedro47","courses":[{"course":"Python","note":90},{"course":"JavaScript","note":85}]}]
#print reduce(arr)

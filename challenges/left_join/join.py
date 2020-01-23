
def join(table1, table2):
    results = []
    for key in table1:
        if key in table2:
            results.append([key,table1[key], table2[key]])
        else:
            results.append([key,table1[key], None])
        
    return results

def join(table1, table2):
    """Write a function that JOINs two hashmaps into a single data structure."""

    results = []
    for key in table1:
        if key in table2:
            results.append([key,table1[key], table2[key]])
        else:
            results.append([key,table1[key], None])
        
    return results
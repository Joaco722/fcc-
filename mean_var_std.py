import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(lst).reshape((3, 3))
    
    mean_columns = matrix.mean(axis=0).tolist()
    mean_rows = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()

    variance_columns = matrix.var(axis=0).tolist()
    variance_rows = matrix.var(axis=1).tolist()
    variance_flattened = matrix.var().tolist()

    std_columns = matrix.std(axis=0).tolist()
    std_rows = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()

    max_columns = matrix.max(axis=0).tolist()
    max_rows = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()

    min_columns = matrix.min(axis=0).tolist()
    min_rows = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()

    sum_columns = matrix.sum(axis=0).tolist()
    sum_rows = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()

    calculations = {
        'mean': [mean_columns, mean_rows, mean_flattened],
        'variance':[variance_columns, variance_rows,variance_flattened],
        'standard deviation':[std_columns,std_rows,std_flattened],
        'max': [max_columns,max_rows,max_flattened],
        'min': [min_columns,min_rows,min_flattened],
        'sum': [sum_columns,sum_rows,sum_flattened]
        }

    return calculations

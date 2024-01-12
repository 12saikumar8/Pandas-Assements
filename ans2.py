import pandas as pd
def get_car_type(value):
    if value <= 15:
        return 'low'
    elif value > 15 and value <= 25:
        return 'medium'
    else:
        return 'high'

def get_type_count(dataset_path):
    df=pd.read_csv(dataset_path)

    df['car_type'] = df['car'].apply(get_car_type)

    count=df['car_type'].value_counts()

    return count

dataset_path='datasets\dataset-1.csv'
result=get_type_count(dataset_path)
print(result)
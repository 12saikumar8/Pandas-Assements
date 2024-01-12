# This answer for 1st question in dataset_1.csv
import pandas as pd 
def generate_car_matrix(dataset_path):

    df=pd.read_csv(dataset_path)


    car_matrix=df.pivot(index='id_1',columns='id_2',values='car').fillna(0)



    car_matrix.values[[range(car_matrix.shape[0])]*2]



    return car_matrix

dataset_path='datasets\dataset-1.csv'
result_matrix=generate_car_matrix(dataset_path)
print(result_matrix)
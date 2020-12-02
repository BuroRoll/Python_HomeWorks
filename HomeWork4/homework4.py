import pandas as pd


def get_group_points(group):
    df = pd.read_csv('Ведомость.csv')
    sorted_df = df.sort_values(by=['Баллы'], ascending=[False])
    row = sorted_df[sorted_df['Команда'] == group]
    print(row[['ФИО', 'Баллы']])


get_group_points('АТ-01')

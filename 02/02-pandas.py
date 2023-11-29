import pandas as pd

data = {'Nume': ['Ana', 'Bogdan', 'Cristina'],
        'Varsta': [25, 30, 22],
        'Salariu': [50000, 60000, 45000]}

df = pd.DataFrame(data)
# print(df)
# nume = df['Nume']
# print(nume)
# salariu_bogdan = df.at[1, 'Salariu']
# print(salariu_bogdan)
#
# df['Experienta'] = [22, 52, 12]
# print(df)
# df.set_index('Nume', inplace=True)
# print(df.loc['Bogdan'])
# df_filtrat_complex = df[(df['Varsta'] >= 22) & (df['Experienta'] >= 22)]
# print(df_filtrat_complex)

data = {'Nume': ['Ana', 'Bogdan', 'Cristina', 'David', 'Elena', 'Florin'],
        'Varsta': [25, 30, 22, 35, 28, 40],
        'Salariu': [50000, 60000, 45000, 70000, 55000, 80000],
        'Departamente': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR']}

df = pd.DataFrame(data)
print(df)
print('==========================================')

grupuri_departamente = df.groupby('Departamente')

# for nume_departament, grup in grupuri_departamente:
#         print(nume_departament)
#         print(grup)

medie_salarii = grupuri_departamente['Salariu'].mean()
print(medie_salarii)

rezultate_agregare = grupuri_departamente.agg({'Varsta': 'mean', 'Salariu': ['sum', 'median'], 'Nume': 'count'})
print(rezultate_agregare)

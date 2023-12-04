import pandas as pd
from json import loads

datas = pd.read_csv("data/in/met_agenda.csv",delimiter=";")
df1 = datas[['Titre','Ville', 'Mots clés', 'Événement physique ou en ligne']]

result = df1.to_json(orient="records")
parsed = loads(result)
for key in range(len(parsed)):
    print(key)
    result_tmp = parsed[key]['Événement physique ou en ligne']
    df1.loc[key].at['Événement physique ou en ligne'] = loads(result_tmp)['label']['fr']

df1.to_csv("data/out/import.py", header=True,index=False)

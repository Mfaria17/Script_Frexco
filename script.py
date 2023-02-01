import csv
import numpy as np
import argparse
from sklearn.linear_model import LinearRegression

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='Nome do arquivo CSV que contém os dados')
args = parser.parse_args()

demand = []

#Lendo o arquivo dados.csv (que contém os dados passados) e colocando-os em um array
with open(args.filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        demand.append(int(row[1].replace('.', '')))

#Calculando a previsão de demanda baseado na regressão linear
model = LinearRegression()
model.fit(np.arange(len(demand)).reshape(-1, 1), demand)
futureDemand = model.predict(np.arange(len(demand), len(demand)+5).reshape(-1, 1))
print(*[int(d) for d in futureDemand], sep=', ')
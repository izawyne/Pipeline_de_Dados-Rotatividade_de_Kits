import pandas as pd
import os

def extract():
    print("Iniciando etapa EXTRACT...")

    caminho = os.path.join("data_sample", "exemplo.csv")

    df = pd.read_csv(caminho)

    print("Dados extraídos com sucesso")
    return df


if __name__ == "__main__":
    extract()

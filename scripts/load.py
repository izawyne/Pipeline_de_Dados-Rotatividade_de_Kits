import os

def load(df):
    print("Iniciando etapa LOAD...")

    # Regra de negócio (exemplo baseado no seu projeto)
    df = df[df["quantidade"] > 5]

    output_path = "output"
    os.makedirs(output_path, exist_ok=True)

    caminho_saida = os.path.join(output_path, "dados_tratados.csv")

    df.to_csv(caminho_saida, index=False, sep=";")

    print("Arquivo salvo com sucesso")
    print(f"Caminho: {caminho_saida}")


if __name__ == "__main__":
    from transform import transform
    from extract import extract

    df = extract()
    df = transform(df)
    load(df)

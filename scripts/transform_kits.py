import pandas as pd

def transform(df):
    print("Iniciando etapa TRANSFORM...")

    # Converter data
    df["data_emissao"] = pd.to_datetime(df["data_emissao"])

    # Padronizar nomes
    df.columns = [col.lower() for col in df.columns]

    # Criar coluna derivada
    df["valor_medio"] = df["valor"] / df["quantidade"]

    print("Transformação concluída")
    return df


if __name__ == "__main__":
    from extract import extract
    df = extract()
    transform(df)

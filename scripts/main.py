from extract import extract
from transform import transform
from load import load

def main():
    print("Executando pipeline completo...")

    df = extract()
    df = transform(df)
    load(df)

    print("Pipeline finalizado com sucesso")


if __name__ == "__main__":
    main()

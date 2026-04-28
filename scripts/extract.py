import pandas as pd
import os

def extract():
    print("Iniciando etapa EXTRACT...")

    # Caminho do SQL
    sql_path = os.path.join("sql", "exemplo_query.sql")

    with open(sql_path, "r") as file:
        query = file.read()

    print("Query carregada:")
    print(query)

    # Simulação de retorno do banco (dados fictícios)
    data = {
        "id_pedido": [1, 2, 3, 4],
        "cod_cliente": [1001, 1002, 1003, 1001],
        "nome_cliente": ["Hospital A", "Hospital B", "Hospital C", "Hospital A"],
        "data_emissao": ["2025-06-01", "2025-06-05", "2025-07-10", "2025-08-15"],
        "quantidade": [10, 5, 8, 12],
        "valor": [1500.50, 800.00, 1200.00, 2000.75]
    }

    df = pd.DataFrame(data)

    print("Dados extraídos com sucesso (simulação)")
    return df


if __name__ == "__main__":
    extract()

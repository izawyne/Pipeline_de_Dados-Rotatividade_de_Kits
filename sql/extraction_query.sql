-- Query de exemplo utilizada para extração de dados
-- Adaptada para fins de portfólio (sem dados reais)

SELECT
    id_pedido,
    cod_cliente,
    nome_cliente,
    data_emissao,
    quantidade,
    valor
FROM pedidos
WHERE data_emissao >= '2025-06-01'

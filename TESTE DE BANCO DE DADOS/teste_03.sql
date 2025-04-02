CREATE TABLE operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    despesa_trimestre DECIMAL(15,2),
    despesa_ano DECIMAL(15,2)
);

LOAD DATA INFILE '/caminho/para/operadoras.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(nome, despesa_trimestre, despesa_ano);

SELECT nome, despesa_trimestre
FROM operadoras
ORDER BY despesa_trimestre DESC
LIMIT 10;

SELECT nome, despesa_ano
FROM operadoras
ORDER BY despesa_ano DESC
LIMIT 10;


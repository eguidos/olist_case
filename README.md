# Modelagem e ingestão de dados

## Table of contents
1. Resumo
2. Solução
    - Proposta de modelo relacional
    - Coleta de dados utilizando Python
    - Normalização de dados utilizando Apache Spark
3. Resultados

* Resumo 

O counteúdo deste repositório tem como objetivo demonstrar um fluxo de dados para realizar a normalização de um banco de 
dados utilizando como base **Apache Spark**. Além disso, será demonstrada a utilização **AWS Schema Conversion Tool**

* Solução

Como destacado anteriormente, o case foi solucionado com base na tecnologia **Spache Spark** e outras tecnologias que 
viabilizaram esta POC:
1. [Apache Spark](https://spark.apache.org/)
2. [Python 3](https://www.python.org/)
3. [Mysql](https://www.mysql.com/)

* Proposta de modelo relacional

O modelo relacional foi implementado sob o banco relacional **MySql Versão 14.14 Distribuição 5.7.30, para Linux** conforme 
o Diagrama de Entidade e Relacionamento abaixo:

![MER](resources/architecture/dw.png)

Logicamente, o modelo foi segmentado em dois principais componentes para a extração de dimensões 
e fatos da base denormalizada inspirado no modelo **Star Schema (Kimball)**:

1. Tabelas dimensionais:
    - Customer
    - Date
    - Reviews 
    - Location
    - Time
    - Seller
    - Products
    - Items
2. Tabela Fato
    - Orders

##Coleta de dados utilizando Python
A estrutura necessária para a coleta dos dados amostrais foi realizada utlizando os trechos de código contidos no módulo `utils.py`.




###Normaliação de dados utilizando **Python / Spark**
A organização do código Pyspark utilizada nesta POC seguiu o padrão semelhante a Arquitetura Orientada a Serviços (SOA) 
evidenciado abaixo. Este padrão contribui para fácil manutenção do código fonte e principalmente para escalabilidade de análises sob o dado coletado.

[!DATA](resources/architecture/normalization.jpg)
:pushpin: **Pyspark** foi a linguagem como base para utilização de ferramentas Big Data.


    
 
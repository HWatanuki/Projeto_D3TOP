# Projeto_D3TOP
Projeto em grupo da disciplina D3TOP - Tópicos em Ciência de Dados do curso de Especialização em Ciência de Dados do IFSP Campinas.

# Membros do grupo: 
- Gabrielly Baratela de Carvalho
- Halisson Gomides
- Hugo Martinelli Watanuki (CP3016692)

# Sistema de recomendação de propriedades para hospedagem
O objetivo deste repositório é fornecer um conjunto de instruções, arquivos de configuração e códigos para a implantação de uma solução de recomendação de propriedades litadas na plataforma Airbnb com base em dados de entrada fornecidos por um usuário sobre suas preferências de hospedagem. 

# a) Descrição e motivação do problema
XXXXXXXXXXXXXXXXX

# b) Objetivo de negócio ou científico associado ao problema.
XXXXXXXXXXXXXXXXX

# c) Descrição da base de dados

A base de dados utilizada no trabalho foi a da Comissão de Taxi e Limousine da cidade de Nova York (https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). 

Essa base contém registros de viagens de passageiros de taxi da cidade de Nova York com os seguintes atributos:
- Local, data e hora da partida e chegada de cada viagem
- Distância, custo, tarifa e número de passageiros de cada viagem

Para as análises foram selecionados 2 datasets:
- 1 dataset contendo as viagens realizadas no mês de Janeiro de 2017 (escolha aleatoria apenas para exemplificar a analise): 9.710.124 registros
- 1 dataset contendo os códigos e descrições das áreas da cidade de Nova York: 265 registros

Os datasets utilizados estão disponíveis aqui: https://github.com/HWatanuki/Trabalho_D2TEC/tree/main/Datasets

O schema do dataset de viagens possui a seguinte estrutura:

    STRING VendorID; // codigo indicando a companhia associada a viagem
    STRING tpep_pickup_datetime; // data e hora do embarque
    STRING tpep_dropoff_datetime; // data e hora do desembarque
    STRING passenger_count; // numero de passageiros
    STRING trip_distance; // distancia da viagem
    STRING RatecodeID; // codigo final de cobranca da viagem
    STRING store_and_fwd_flag; // codigo que indica se os dados da viagem foram gravados no veiculo por falta de conexao
    STRING PULocationID; // codigo do local de embarque
    STRING DOLocationID; // codigo do local de desembarque
    STRING payment_type; // tipo do pagamento (dinheiro,cartao,etc)
    STRING fare_amount; // valor da corrida no taximetro
    STRING extra;  // tarifas extras nos horarios de pico
    STRING mta_tax; // imposto extra em funcao da taxa do taximetro
    STRING tip_amount; // valor da gorjeta
    STRING tolls_amount; // valor dos pedagios
    STRING improvement_surcharge; // taxa compensatoria para viagens curtas
    STRING total_amount; // valor total recebido do passageiro

Visualizacao do dataset de viagens bruto

![image](https://user-images.githubusercontent.com/50485300/200210322-6899b9c8-8b80-4789-822e-d1e9237e0769.png)

O schema do dataset de bairros de NY possui a seguinte estrutura:
  
    STRING LocationID;  // Codigo identificador das zonas de taxi
    STRING Borough; // Bairro da zona
    STRING Zone; // Nome da zona
    STRING service_zone; // Categoria de servico da zona
  
Visualizacao do dataset de bairros de NY bruto

![image](https://user-images.githubusercontent.com/50485300/200210396-e4403d5e-bd37-443e-a7ff-7d8c9c2b1a54.png)


# d) Etapa de limpeza e pré-processamento

O tratamento e análise dos dados objetivou proporcionar a um motorista de taxi da cidade de NY insumos para uma estratégia de trabalho. 
Para isso, uma vez tratados os dados, os mesmos serviram para um entendimento sobre o padrao das viagens ao longo dos dias e horas do mes, bem como as regioes com as viagens e gorjetas mais elevadas. 
Por fim, uma funcao foi elaborada com base nos dados historicos medios para permitir ao motorista estimar o valor, duracao e distancia de uma viagem com base no local de embarque/desembarque, dia e hora de inicio da viagem. 

Os códigos utilizados para tratament e consultas dos dados estão disponíveis aqui: https://github.com/HWatanuki/Trabalho_D2TEC/tree/main/Codigos







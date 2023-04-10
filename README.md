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
A base de dados utilizada no trabalho foi extraída a partir da plataforma Airbnb usando uma ferramenta de web scraping chamada Apify (https://apify.com/dtrungtin/airbnb-scraper). O Airbnb Scraper possibilita processar os anúncios do Airbnb e obter detalhes tais como localidade, preços, reviews, notas, imagens, informações sobre proprietários e hóspedes, etc. A extração pode ser realizada por localidade ou com base em um anúncio específico.

Para o treinamento do modelo foram selecionados 2 datasets:
- 1 dataset contendo os anúncios da cidade de São Paulo: XXXXXX registros
- 1 dataset contendo os anúncios da cidade de Nova York: XXXXXX registros

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


  
Visualizacao do dataset de bairros de NY bruto

![image](https://user-images.githubusercontent.com/50485300/200210396-e4403d5e-bd37-443e-a7ff-7d8c9c2b1a54.png)


# d) Etapa de limpeza e pré-processamento
A etapa de limpeza e pré-processamento dos dados objetivou num primeiro momento tratar adequadamente os dados brutos contidos no arquivo .csv extraído via Apify.

Os códigos utilizados para a limpeza e pré-processamento dos dados estão disponíveis nesse notebook: https://github.com/HWatanuki/Projeto_D3TOP/blob/main/Codigos/Data_preprocessing_v0.ipynb







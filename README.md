# Projeto_D3TOP
Projeto em grupo da disciplina D3TOP - Tópicos em Ciência de Dados do curso de Especialização em Ciência de Dados do IFSP Campinas.

# Membros do grupo: 
- Gabrielly Baratela
- Halisson Souza Gomides (CP3016382)
- Hugo Martinelli Watanuki (CP3016692)

# Sistema de recomendação de propriedades para hospedagem
O objetivo deste repositório é fornecer um conjunto de instruções, arquivos de configuração e códigos para a implantação de uma solução de recomendação de propriedades litadas na plataforma Airbnb com base em dados de entrada fornecidos por um usuário sobre suas preferências de hospedagem. 

# a) Descrição e motivação do problema
XXXXXXXXXXXXXXXXX

# b) Objetivo de negócio ou científico associado ao problema
XXXXXXXXXXXXXXXXX

# c) Descrição da base de dados
A base de dados utilizada no trabalho foi extraída a partir da plataforma Airbnb usando uma ferramenta de web scraping chamada Apify (https://apify.com/dtrungtin/airbnb-scraper). O Airbnb Scraper possibilita processar os anúncios do Airbnb e obter detalhes tais como localidade, preços, reviews, notas, imagens, informações sobre proprietários e hóspedes, etc. A extração pode ser realizada por localidade ou com base em um anúncio específico.

Para o treinamento do modelo foram selecionados 2 datasets:
- 1 dataset contendo os anúncios da cidade de São Paulo: XXXXXX registros
- 1 dataset contendo os anúncios da cidade de Nova York: XXXXXX registros

Os datasets utilizados estão disponíveis aqui: https://github.com/HWatanuki/Projeto_D3TOP/tree/main/Datasets

O schema dos datasets de treinamento possuem a seguinte estrutura:

    url // a url do anúncio
    name // o nome do anúncio
    stars // a nota de avaliação do anúncio
    numberOfGuests // numero de hóspedes permitidos
    address // endereço da propriedade
    roomType // tipo da propriedade
    location // latitude e longitude da propriedade
    reviews // avaliações da propriedade
        author // dados de perfil do autor da avaliação
        comments // texto com o comentário da avaliação
        createdAt // data de criação da avaliação
        id // identificador da avaliação
        collectionTag // tag
        rating // nota dada pelo avaliador
        recipient // destinatário da avaliação
        response // texto com a réplica do proprietário
        localizedDate // data da avaliação
        localizedReview //
    pricing // dados de custo da propriedade
        rate // tarifa de ocupação
        rateType // tipo da tarifa
        rateBreakdown // tarifa por data específica
        nights // quantidade de diárias
        totalPrice // preço total
    photos // fotos do anúncio
        caption // legenda da foto
        pictureUrl // URL da foto
        thumbnailUrl // URL da foto miniatura
    primaryHost // perfil do proprietário
    additionalHosts // perfil dos co-anfitriões
    isHostedBySuperhost // proprietário qualificado

# d) Etapa de limpeza e pré-processamento
A etapa de limpeza e pré-processamento dos dados objetivou num primeiro momento tratar adequadamente os dados brutos contidos no arquivo .csv extraído via Apify.

Os códigos utilizados para a limpeza e pré-processamento dos dados estão disponíveis nesse notebook: https://github.com/HWatanuki/Projeto_D3TOP/blob/main/Codigos/Data_preprocessing_v0.ipynb







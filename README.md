# Projeto_D3TOP
Projeto em grupo da disciplina D3TOP - Tópicos em Ciência de Dados do curso de Especialização em Ciência de Dados do IFSP Campinas.

# Membros do grupo: 
- Gabrielly Baratela (CP3016331)
- Halisson Souza Gomides (CP3016382)
- Hugo Martinelli Watanuki (CP3016692)

# Sistema de análise do mercado de aluguel de curta duração
O objetivo deste repositório é fornecer um conjunto de instruções, arquivos de configuração e códigos para a implantação de uma solução de apoio à tomada de decisão para escolha de imóvel para aluguel de curta temporada com base em dados disponíveis na plataforma Airbnb (https://www.airbnb.com/). 

# a) Descrição e motivação do problema

A decisão de investimento em um imóvel para a finalidade de aluguel de curta temporada deve considerar diversos fatores, como *"Quais os tipos de imóveis mais comuns em um determinada localidade? Qual a característica dos imóveis que apresentam maior taxa de ocupação média? Quais os atributos dos imovéis são mais destacados pelos hóspedes em seus comentários? Qual a proximidade dos pontos turísticos da região? Quais são as regiões mais escolhidas na localidade buscada?"*. Essas respostas costumam surgir provenientes de diversas buscas e análises superficiais dos dados de anúncios feitas pelos próprios locatários, ao exercitarem a comparação visual dos anúncios e suas diferenças. Uma vez que todas esses dados estão disponíveis virtualmente, pode ser muito mais eficiente o uso de estatística e inteligência artificial para análises estruturadas que orientem essa tomada de decisão. 

# b) Objetivo de negócio ou científico associado ao problema

O objetivo deste trabalho é desenvolver um protótipo de sistema de recomendações de anúncios de imóveis para aluguel, de acordo com o interesse e o perfil desejado do locatário, para orientar a melhor tomada de decisão e simplificar sua jornada de busca e comparação de anúncios.

O desafio tem início na própria origem dos dados: desde a captura automatizada à estruturação da base em atributos delimitados; e segue relevante para o sistema de recomendação, uma vez que nem todos os dados estão prontamente consolidados nos anúncios das plataformas. 

Na tentativa de endereçar o primeiro desafio, o uso de ferramentas de web scraping e abordagens de processamento de linguagem natural pode representar uma alternativa viável. Por fim, a solução se apoiará em algoritmos de machine learning para fornecer as recomendações adaptadas às necessidades do locatário.

# c) Descrição da base de dados

Os conjuntos de dados a serem extraídos, processados e analisados consistem nos anúncios de aluguel de curta duração da plataforma Airbnb e seus respectivos atributos. Num primeiro momento, os dados serão extraídos com o auxílio de ferramentas de web scraping. Em seguida, técnicas de processamento de linguagem natural serão aplicadas para limpeza, pré-processamento e estruturação dos dados. 

A base de dados utilizada no trabalho foi extraída a partir da plataforma Airbnb usando uma ferramenta de web scraping disponível no Apify: o Airbnb Scraper (https://apify.com/dtrungtin/airbnb-scraper). 

O Airbnb Scraper possibilita processar os anúncios do Airbnb e obter detalhes tais como localidade, preços, reviews, notas, imagens, informações sobre proprietários e hóspedes, etc. A extração pode ser realizada por localidade ou com base em um anúncio específico.

O conjunto de dados extraídos pelo Airbnb Scraper consiste numa estrutura relacional de anúncios e seus respectivos atributos. A imagem abaixo ilustra uma extração realizada para uma determinadade localidade nos Estados Unidos.

![image](https://user-images.githubusercontent.com/50485300/231626884-dd9a6abd-5527-4720-8a67-bd12b1628037.png)

A lista completa de atributos disponíveis nos anúncios processados pelo Airbnb Scraper é apresentada abaixo:

    additionalHosts // perfil dos co-anfitriões
    address // local da propriedade
    isAvailable // disponibilidade da propriedade
    isHostedBySuperhost // qualificação do anfitrião
    location // latitude e longitude da propriedade
    name // o nome do anúncio
    numberOfGuests // numero de hóspedes permitidos
    photos // fotos do anúncio
        caption // legenda da foto
        pictureUrl // URL da foto
        thumbnailUrl // URL da foto miniatura
    pricing // dados de custo da propriedade
        rate // tarifa de ocupação
        rateType // tipo da tarifa
    primaryHost // perfil do anfitrião
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
        localizedReview // avaliação local   
    roomType // tipo da propriedade 
    stars // a nota de avaliação da propriedade
    url // a url do anúncio
       
 Para auxiliar com o desenvolvimento da solução proposta, inicialmente e apenas para fins exploratórios, foram extraídos dois conjuntos de dados em formato .csv via o Airbnb Scraper:
 
- 1 dataset contendo 547 anúncios da cidade de São Paulo
- 1 dataset contendo 547 anúncios da cidade de Nova York

O objetivo dessa primeira extração foi selecionar anúncios de cidades populosas e localizadas em diferentes países com o intuito de obter uma amostra de anúncios com maior diversidade de imóveis para aluguel de curta temporada, bem como que contivessem comentários em mais do que um idioma.

Os datasets utilizados estão disponíveis aqui: https://github.com/HWatanuki/Projeto_D3TOP/tree/main/Datasets
  

# d) Etapa de limpeza e pré-processamento
A etapa de limpeza e pré-processamento dos dados objetivou num primeiro momento dar uma estruturação mínima e maior qualidade aos dados brutos contidos nos datasets gerados por meio do Airbnb Scraper.

Após a conversão do dataset em um dataframe, as seguintes operações principais foram executadas em sequência:

- Remoção de colunas contendo metadados não críticos 
- Análise e remoção de missing values
- Tratamento dos campos contendo textos em formato natural 
  * Conversão para Minúsculas.
  * Remoção de tags HTML.
  * Remoção de pontuacoes.
  * Remoção de algarismos numericos e numeros de telefone.
  * Remoção de multiplos espacos.
  * Remoção de URLs e E-mails.
  * Substituicao de Emojis.
  * Substituicao de nomes de usuário.
  * Remoção de acentuacao.
  * Remoção caracteres especiais.
  * Remoção de 3 ou mais letras consecutivas.
  * Remoção de palavras curtas.
  * Remoção de Stopwords.
  * Lematização.

Os códigos utilizados para a limpeza e pré-processamento dos dados estão disponíveis nesse notebook: 
https://github.com/HWatanuki/Projeto_D3TOP/blob/main/Codigos/Data_preprocessing_v0.1.ipynb







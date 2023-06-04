# Projeto_D3TOP
Projeto em grupo da disciplina D3TOP - Tópicos em Ciência de Dados do curso de Especialização em Ciência de Dados do IFSP Campinas.

## Membros do grupo: 
- Gabrielly Baratela (CP3016331)
- Halisson Souza Gomides (CP3016382)
- Hugo Martinelli Watanuki (CP3016692)

# Sistema de análise do mercado de aluguel de curta temporada
O objetivo deste repositório é fornecer os documentos para implantação de uma solução de apoio à tomada de decisão para escolha de imóvel para aluguel de curta temporada com base em dados disponíveis na plataforma Airbnb (https://www.airbnb.com/).

## a) Descrição e motivação do problema

A decisão de investimento em um imóvel para a finalidade de aluguel de curta temporada deve considerar diversos fatores, como *"Quais os tipos de imóveis mais comuns em um determinada localidade? Qual a característica dos imóveis que apresentam maior taxa de ocupação média? Quais os atributos dos imovéis são mais destacados pelos hóspedes em seus comentários? Qual a proximidade dos pontos turísticos da região? Quais são as regiões mais escolhidas na localidade buscada?"*. Essas respostas costumam surgir provenientes de diversas buscas e análises superficiais dos dados de anúncios feitas pelos próprios locatários, ao exercitarem a comparação visual dos anúncios e suas diferenças. Uma vez que todas esses dados estão disponíveis virtualmente, pode ser muito mais eficiente o uso de estatística e inteligência artificial para análises estruturadas que orientem essa tomada de decisão. 

## b) Objetivo de negócio ou científico associado ao problema

O objetivo deste trabalho é desenvolver um protótipo de sistema de recomendações de anúncios de imóveis para aluguel, de acordo com o interesse e o perfil desejado do locatário, para orientar a melhor tomada de decisão e simplificar sua jornada de busca e comparação de anúncios. Um sistema de recomendação que variáveis descritivas além dos filtros padrões do aplicativo, torna a experiência de busca do cliente diferenciada na plataforma.

## c) Base de dados

O desafio tem início na própria origem dos dados: desde a captura automatizada à estruturação da base em atributos delimitados; e segue relevante para o sistema de recomendação, uma vez que nem todos os dados estão prontamente consolidados nos anúncios das plataformas. 

Na tentativa de endereçar o primeiro desafio, o uso de ferramentas de web scraping e abordagens de processamento de linguagem natural pode representar uma alternativa viável. Por fim, a solução se apoiará em algoritmos de machine learning para fornecer as recomendações adaptadas às necessidades do locatário.

### Descrição da base de dados
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
  

## d) Etapa de limpeza e pré-processamento
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
 - Conversão das variáveis numéricas

Os códigos utilizados para a limpeza e pré-processamento dos dados estão disponíveis nesse notebook: 
https://github.com/HWatanuki/Projeto_D3TOP/blob/main/Codigos/Data_preprocessing_v0.2.ipynb

## e) Extração de características
O objetivo da etapa de extração de características era resumir todas as reviews de cada anúncio em uma sentença com as palavras-chave mais relevantes no documento. Seguimos com duas abordagens


**1. Teste TF-IDF + Sentence Score: **

Utilizamos o método TF-IDF para coletar as palavras mais relevantes dos reviews e criamos scores para as sentenças de acordo com o resultado do TF-IDF. O resumo escolhia as sentenças de maiores scores que representassem 20% de todos os reviews.

**Decidimos não seguir com essa abordagem** pois era necessário realizar reconhecimento de entidades para remover nomes próprios e outros processamentos para que o resumo com as palavras relevantes fizesse sentido e não ficasse tão grande. 
        
        
**2. LSA Summarizer (Análise Semântica Latente):**

É uma técnica de NLP para analisar relacionamentos entre um conjunto de documentos e os termos que eles contêm, produzindo um conjunto de conceitos relacionados aos documentos e termos. A LSA assume que as palavras com significado próximo ocorrerão em trechos de texto semelhantes (hipótese distributiva), e usa o SVD (decomposição de valor singular) e a similaridade de cosseno para reduzir os textos em uma quantidade de sentenças pré-definida.

**Essa foi a abordagem utilizada no projeto.**


## f) Modelos de Machine Learning 
Para a modelagem, realizamos duas abordagens:


### 1. TF-IDF Vectorizer + SVM:

Decidimos realizar modelagem com o TF-IDF Vectorizer e SVM (support vector machines) para realizar recomendações baseadas em palavras-chave das reviews realizadas pelos usuários. Fizemos um teste e os resultados não estavam aderentes, portanto, **optamos por não seguir com essa abordagem.**
    
    
### 2. BERT pré-treinado com o modelo `bert-base-uncased`:

BERT (Bidirectional Encoder Representations from Transformers) é um modelo de Deep Learning criado por pesquisadores do Google AI Language. A principal vantagem do BERT é a aplicação do treinamento bidirecional do Transformer (um modelo de atenção) ao NLP, isso é, que pode ter um senso mais profundo de contexto e fluxo de linguagem uma vez que entende a sequência de texto da esquerda para a direita e da direita para a esquerda. Além disso, utilizar um modelo pré-treinado evolui significativamente os resultados do modelo após ajuste fino, e com drástica redução de esforço de treinamento. 

Utilizamos os resultados do BERT e a similaridade de cossenos para gerar o produto de similaridade das covariáveis que utilizamos no nosso sistema de recomendação, para finalmente ordenar os anúncios do mais similar para o menos similar e exibir para o usuário.

**Optamos por seguir com essa abordagem.**


## g) Protocolo de experimentos e validação
Como nossa abordagem é não supervisionada, fizemos testes manuais para validar se o resultado retornado como recomendação de acordo com os parâmetros de entrada do sistema estavam fazendo sentido. Fizemos testes alterando o valor de cada covariável, e em todos os casos os retornos fizeram sentido. Foram 30 testes, alterando os inputs de cada covariável, uma de cada vez.

## h) Discussão dos resultados e trabalhos futuros
### Discussão de resultados: 
Os resultados obtidos pelo sistema de recomendação criado são satisfatórios, fazendo sentido no contexto em que está inserido e trazendo inovação para a busca de imóveis para aluguel de temporada. Como é um modelo não supervisionado e não objetivo, não trouxemos métricas para medir seu desempenho, mas em nossos testes os resultados fizeram sentido em 100% dos casos.

### Trabalhos futuros:
- Conectar o sistema com a API do airbnb para conseguir atualizar os dados em tempo real 
- Incluir no sistema a avaliação de datas disponíveis de acordo com o interesse do usuário
- Considerar endereços próximos ao desejado pelo cliente por análise geográfica
- Monitorar tempo de execução dos modelos e outras métricas para acompanhar desempenho do sistema

## i) Deployment da solução em produção

## j) Vídeo de até 10 min explicando o projeto!
<Inserir link>





## IAA016 - Tópicos em IA
## Aluno: Mateus Cichelero da Silva

### Exercício - Caixeiro Viajante com Algoritmos Genéticos
#### Março 2023

# PROGRAMA PARA EXECUÇÃO DO PROBLEMA CAIXEIRO VIAJANTE UTILIZANDO ALGORITMOS GENÉTICOS 


## COMO RODAR:
- Crie e entre em um ambiente python. Exemplo: 
```console
conda create --name caixeiro python=3.10
```

- Instale as bibliotecas necessárias:
    - random
    - matplotlib.pyplot as plt
    - math
    - from random import choices
    - numpy
    - argparse

- Execute o comando: 
```console
python caixeiro_viajante.py
```

- É possível alterar parâmetros do algoritmo e da simulação. Seguem os parâmetros:
    - -n_cidades: Numero de cidades no mapa. Default: 100
    - -n_pop: Numero de percursos na populacao. Default: 100
    - -tx_cruzamento: Taxa de cruzamento. Ex: 60 para 60%. Default: 60
    - -tx_mutacao: Taxa de mutacao. Ex: 5 para 5%. Default: 5
    - -n_geracoes: Numero de geracoes para simulacao. Default: 8000
    - -n_selecao: Numero de individuos selecionados por ranking. Default: 50


- Exemplo de execução alterando-se parâmetros default - escolhendo 1000 gerações na simulação:
```console
python caixeiro_viajante.py -n_geracoes 1000
```

## SAÍDAS DO PROGRAMA:
- Ao executar o script as seguintes informações serão exibidas:
    - Na geração 0 e a cada 1000 gerações uma imagem com o percurso de melhor fitness é exibida e salva na pasta do projeto, Além disso seu valor da função fitness é impresso no console.
    - Ao final da simulação, o percurso (array contendo todas as cidades em ordem de viagem) de melhor fitness da última geração é impresso na tela.

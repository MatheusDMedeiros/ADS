# Simulação de Filas M/M/1 em Tandem usando simulação a Eventos Discretos

> O objetivo da atividade é aplicar simulação a eventos discretos para avaliar o desempenho de uma rede de filas.

## Descrição 

Para elaborar o simulador de filas M/M/1 em tandem, foi necessário se basear no seguinte [código](https://drive.google.com/file/d/1O5UrmUp9KjpCUU49s4hwZK2n9ZPd_y-v/view). Com isso, implementamos duas filas M/M/1 conectadas em Tandem com taxas de chegada e atendimento configuráveis.

- Métricas avaliadas:
  - Vazão de saída da última fila;
  - Número médio de requisições no sistema;
  - Tempo médio de resposta do sistema.

Por fim, o código modificado para filas M/M/1 em Tandem está presente em [simulador.py](./simulador.py) e no [simulador.ipynb] está o notebook para facilitar a execução do simulador. Além disso, ao final é gerado gráficos para apresentar os resultados da simulação.
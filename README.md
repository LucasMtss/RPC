# RPC
RPC de operações matemáticas em python, onde o cliente conecta a um servidor de nomes que informa qual servidor possui a operação matemática requerida, devolvendo o IP e a porta. Dessa forma o cliente faz a requisição para o servidor correto e obtém o resultado da operação.
As operações suportadas são:
<br/>
* Soma
* Produto
* Fatorial
* Números primos
* Conversão de dólar para real
<br/>
O servidor de nome possui um sistema de cache que possibilita para melhorar a performance
<br/>
As conexões cliente/servidor são feitas via socket

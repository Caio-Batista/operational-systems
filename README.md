# operational-systems
Labs of OS classes

--------------------------------------------------------------------

* Lab1 - Questão pratica:
 * Todos os dois ids, de cada relatório, para o open e write são iguais,
  entretanto eles mudam para os diferentes inputs, pois acessam áreas de 
  memórias diferentes no SO.

* Lab1 - Questão teórica:
 * CÓDIGOS DO ESTADO DO PROCESSO | Descrição
   ----------------------------- | ---------------------------------------------------------------------------------
     R                           | executando ou executável (na fila de execução)
     D                           | sono não interrompivel (geralmente IO)
     S                           | sono interrompivel (aguardando a conclusão de um evento)
     Z                           | defunct / zumbi, terminado mas não colhido por seu pai
     T                           | interrompido, seja por um sinal de controle de ou porque ele está sendo rastreado


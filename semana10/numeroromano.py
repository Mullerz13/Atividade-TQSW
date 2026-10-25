def converte(numeroEmRomano):

  tabela = {};
  tabela['I'] = 1;
  tabela['V'] = 5;
  tabela['X'] = 10;
  tabela['L'] = 50;
  tabela['C'] = 100;
  tabela['D'] = 500;
  tabela['M'] = 10000;
  
  acumulador = 0;
  ultimovizinhodireita = 0;

  for i in reversed(range(len(numeroEmRomano))):
    atual = 0;
    numCorrente = numeroEmRomano[i]; 

    if(numCorrente in tabela):      
      atual = tabela[numCorrente];      

    multiplicador = 1;
    if(atual < ultimovizinhodireita):
      multiplicador = -1; # Alteração feita para corrigir a lógica de subtração em números romanos ao invés de adição

    acumulador += atual * multiplicador;       
    ultimovizinhodireita = atual;

  return acumulador;
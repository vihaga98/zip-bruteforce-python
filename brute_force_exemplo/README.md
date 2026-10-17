ZIP Brute Force Extractor
Um script em Python desenvolvido para demonstrar fundamentos de segurança da informação e recuperação de dados locais. O algoritmo utiliza uma abordagem de força bruta para quebrar palavras-passe de ficheiros .zip, gerando e testando dinamicamente milhões de combinações alfanuméricas.

🚀 O que o projeto demonstra
Em vez de recorrer a bibliotecas de terceiros para gerar as combinações, o motor deste projeto foi construído do zero utilizando a lógica base da linguagem Python. O código foca-se em três pilares técnicos:

Lógica de Iteração e Permutação: Utilização de loops aninhados (for) para cruzar exaustivamente um alfabeto completo (números, letras maiúsculas e minúsculas), gerando novas tentativas de palavra-passe em tempo real.

Tratamento de Exceções: Implementação de blocos try...except com a biblioteca nativa zipfile. O sistema captura os erros gerados por palavras-passe incorretas de forma silenciosa, garantindo que o programa continua a testar as restantes combinações sem falhar ou interromper a execução.

Controlo de Fluxo Eficiente: Aplicação rigorosa de condicionais (if) e comandos de interrupção imediata (return) para terminar o processamento de forma limpa no momento exato em que o ficheiro é extraído com sucesso, otimizando o uso do processador.

⚠️ Aviso Legal
Este projeto foi desenvolvido com fins estritamente educacionais e de estudo de algoritmos de iteração matemática. Deve ser utilizado apenas para a recuperação de ficheiros próprios e estudo de criptografia básica.
<h1>Cálculo do Quadrado de um Número</h1>
<p>Este código tem como objetivo solicitar ao usuário que insira um número, calcular o quadrado desse número por meio de uma função e, em seguida, imprimir o resultado.</p>

<ol>

<h2><li>Entrada do Usuário:</li></h2>
<ul>
    <li>Utiliza a função input para permitir que o usuário insira um número.</li>
    <li>Converte a entrada para um número inteiro usando int().</li>
</ul>

    numero = int(input('Digite um número: '))

<h2><li>Definição da Função:</li></h2>
<ul>
    <li>Cria uma função chamada quadrado que aceita um parâmetro numero e retorna o quadrado desse número.</li>
</ul>

    def quadrado(numero):
        return numero * numero

<h2><li>Chamada da Função e Saída de Dados:</li></h2>
<ul>
    <li>Chama a função quadrado com o número inserido pelo usuário como argumento.</li>
    <li>Imprime a saída indicando o número fornecido pelo usuário e o resultado do quadrado.</li>
</ul>

    print(f'O quadrado de {numero} é {quadrado(numero)}.')
</ol>

<h3>Interatividade:</h3>
<p>O código proporciona uma experiência interativa ao permitir que o usuário insira um número e, em seguida, informa o quadrado desse número.</p>

<h3>Conclusão:</h3>
<p>Ao executar este código, o usuário verá o resultado do quadrado do número inserido. Isso destaca o uso de funções para encapsular lógica específica e facilitar a reutilização de código em Python.
</p>
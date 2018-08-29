[(Cavalcante, A. C. A., 2014)]: http://bdm.unb.br/bitstream/10483/9267/1/2014_AndreCruzAlvesCavalcante.pdf
[Arthur Diniz]: https://github.com/arthurbdiniz
[João Carlos]: https://github.com/joao4018
[Gabriel Ziegler]: https://github.com/gabrielziegler3
### Histórico de Revisões

| Data       | Versão | Descrição            |         Autor             |
|:----------:|:------:|:--------------------:|:-------------------------:|
| 22/08/2018 | 0.1 | Criação do Documento com Adição da Argumentação  | [João Carlos] |
| 26/08/2018 | 0.2 | Adição da Introdução e Atualização da Argumentação  |[João Carlos], [Arthur Diniz] |
| 27/08/2018 | 0.3 | Adição de Argumentação da Daily |[Gabriel Ziegler], [João Carlos] |
| 28/08/2018 | 0.4 | Adição de Argumentação do Nome | [João Carlos] |


# Índice

[1. Introdução](#1-introdução)<br/>
[2. Argumentação](#2-argumentação)
- [2.1. (Tema,Linguagem, Framework)](#tema)
- [2.2. (Escolha da daily)](#daily)
- [2.3. (Escolha do nome)](#nome)


# 1. Introdução

A argumentação possui um papel essencial na sociedade. Diariamente diversas
pessoas participam de discussões, negociações, deliberações e várias outras atividades
colaborativas em que o ato de argumentar é constante. A argumentação possibilita às
pessoas ferramentas para que elas possam defender seus interesses e crenças. [(Cavalcante, A. C. A., 2014)]

Para rastrear as argumentações feitas durante o trabalho, em relação à elicitação de requisitos,
e continuidade da rastreabilidade, foi utilizado o framework ACE 4.

O ACE 4
(JURETA; MYLOPOULOS; FAULKNER, 2009. Citado por Cavalcante, A. C. A., 2014) é um framework de argumentação
baseado em proposições que possui origem na engenharia de requisitos. Este
framework oferece maneiras de modelar e raciocinar acerca da validação relativa dos requisitos
discutidos em uma reunião.

O framework é composto de uma linguagem para representar as informações extraídas de uma discussão, uma condição
de aceitabilidade para verificar a existência de consenso entre os participantes e
procedimentos para checar a condição de aceitabilidade automaticamente.[(Cavalcante, A. C. A., 2014)]


Os modelos de argumentação, gerados com base na linguagem contida no ACE,
são grafos direcionados com rótulos. Os vértices são classificados com base em quatro
rótulos: i, It, P e C. Os vértices com rótulo (i) representam vértices de informação que
servem de entrada ou saída para inferências (It). Os vértices com o rótulo (I) representam
a aplicação de inferências a fim de obter determinadas saídas. Os vértices com rótulo (C)
representam regras de conflito envolvendo dois ou mais vértices em um grafo. Finalmente,
os vértices com rótulo (P) representam regras de preferência envolvendo a predileção de
dois ou mais vértices do grafo. [(Cavalcante, A. C. A., 2014)]

# 2. Argumentação

<a name="tema">
</a>

## 2.1 (Tema, Linguagem, Framework)
- **i(P1)** -  É necessário definir um tema, para ser desenvolvido um projeto, onde seja possível aplicar padrões de projeto com facilidade.
- **i(P2)** -  Desenvolver um Web Service focado nos alunos e professores de Engenharia de Software onde eles possam postar trabalhos desenvolvidos nas disciplinas.
- **i(P3)** -  Existem muitas disciplinas onde é possível desenvolver um Web Service, para a equipe aprender algo novo é melhor desenvolver um jogo em python, onde também teremos maior facilidade para aplicar padrões de projeto.
- **P1** - Houve uma votação onde os membros do grupo ganharam de 5x3 para a escolha do desenvolvimento do jogo.
- **i(P4)** -  É necessário buscarmos uma engine para python nem tão robusta e nem tão simples para podermos aplicar padrões de projeto
- **i(P5)** -  Com base em pesquisas não existe uma engine para python que satisfaça nossos requisitos, será melhor desenvolvermos nosso projeto em JS e criarmos um jogo com características do [agar.io](http://agar.io/).
- **P2** -  Os membro com mais conhecimento nos jogos acharam uma boa ideia para ser aplicada no projeto.
- **i(P6)** -  Iniciaremos as pesquisas para saber como desenvolver um jogo utilizando JS.
- **i(P7)** -  Devido ao cenário de incertezas é melhor voltarmos para a ideia do Web Service já que a maioria do time trabalhou com Web em semestres anteriores.
- **P3** -  Como a maioria do grupo não tem experiência com a desenvolvimento dos jogos por maioria foi decidido voltar para a ideia inicial do projeto.
- **i(P8)** -  É necessário a escolha de um Framework para o desenvolvimento do projeto.
- **i(P9)** -  Como alguns membros do grupo tem conhecimento em python e também familiaridade com o Django é sugerido utilizarmos essa Framework para desenvolvimento do projeto.
- **i(P10)** -  É melhor desenvolver em Ruby on Rails, já que a maioria conhece essa linguagem e é fácil para ser trabalhada.
- **P4** -  A maioria do grupo não gostou da ideia de ter a facilidade do Ruby on Rails porque não teriam ganhos de aprendizado além de que aplicar padrões utilizando Django seria mais interessante.

[![Argumentação(Tema, Linguagem, Framework](https://user-images.githubusercontent.com/29952415/44628192-9ee2c500-a911-11e8-8370-14dbdaf29196.jpg)](https://user-images.githubusercontent.com/29952415/44628192-9ee2c500-a911-11e8-8370-14dbdaf29196.jpg)

<a name="daily">
</a>

## 2.2 (Escolha da daily)

- **i(P1)** - Daily do sábado teve apenas um membro presente, deve-se rever a metologia.
- **i(P2)** - Cancelamento de dailies nos fins de semana.
- **i(P3)** - Dailies em desenho de software é overhead.
- **i(P4)** - Dailies devem ser de segunda à quinta, fica tranquilo para todos os membros participarem.
- **C1(i(P2), i(P4))** - Sexta-feira também é um dia com baixa adesão da daily meeting, deve-se retirar também.
- **i(P5)** - Dailies com timebox aumentado para 1 hora, de segunda a quinta.
- **i(P6)** - Já que as dailies terão 1 hora de timebox da para os membros participarem das dailies de segunda a sexta na parte da manhã.

[![Argumentação(Escolha da daily)](https://user-images.githubusercontent.com/18370133/44695572-33504300-aa4a-11e8-84bb-a3c6e55cb11a.jpg)](https://user-images.githubusercontent.com/18370133/44695572-33504300-aa4a-11e8-84bb-a3c6e55cb11a.jpg)


<a name="nome">
</a>

## 2.2 (Escolha do nome)

- **i(P1)** - Deve-se entrar na [issue](../../issues/23) decisão de nome e ver a mais votada.
- **i(P2)** - Quase nem um membro votou, não dá para escolher desta forma.
- **P1** -  O grupo não entrou em acordo para escolher nomes colocados nas issues por aprensetar pouca quantidade de votos e nomes para escolha.
- **i(P3)** - Deve-se fazer um brainstorm para facilitar a decisão do nome.
- **i(P4)** - O nome em latim é uma boa opção, basta escolher um nome que faça sentido para o projeto e passar para latim como Recon abreviação de Reconditorium de repositório.
- **i(P5)** - Deve as siglas da Faculdade do Gama(FGA), já que nosso projeto é focado para pessoas da faculdade.
- **i(P6)** - Não é necessário utilizar FGA, já que podemos expandir esse projeto no futuro.
- **P2** - O time concordou que não é necessário utilizar FGA no nome.
- **i(P7)** - Boa sugestão em utilizar latim existem outra opções como Spatium de espaço, Ipsum de muito.
- **i(P8)** - Não tem o porque de se prender a escolha de nome em latim, é bem melhor que nós escolhamos algo relacionado a nossa proposta, é opção nossa utilizarmos um nome como boteco, já que as pessoas se reúnem nesses estabelecimentos para conversar, trocar ideias e opiniões, como nosso projeto envolve em trocas de conhecimento em projetos faz muito sentido.
- **P3** - O time preferiu o argumento sobre o nome de boteco já que todos concordam com tais afirmações.
- **i(P9)** - Vamos fazer uma analogia ao git que tem a presença de uma característica nossa que é o compartilhamento de projetos e vamos usar o signifcado do boteco porém em outra língua, e utilizarmos o nome GitPub.

[![definicaonome](https://user-images.githubusercontent.com/29952415/44757591-4de7f200-ab06-11e8-9f92-4352293bf9a1.jpg)](https://user-images.githubusercontent.com/29952415/44757591-4de7f200-ab06-11e8-9f92-4352293bf9a1.jpg)

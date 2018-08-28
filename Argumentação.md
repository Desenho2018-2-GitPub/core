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

# Índice

[1. Introdução](#1-introdução)<br/>
[2. Argumentação](#2-argumentação)

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

## 2.2 (Escolha da daily)

- **i(P1)** - Daily do sábado teve apenas um membro presente.
- **i(P2)** - Cancelamento de dailies nos fins de semana.
- **i(P3)** - Dailies em desenho de software é overhead.
- **i(P4)** - Dailies devem ser de segunda à quinta.
- **C1(i(P2), i(P4))** - Sexta-feira também é um dia com baixa adesão da daily meeting.
- **i(P5)** - Dailies com timebox aumentado para 1 hora, de segunda a quinta.
- **i(P6)** - Dailies de segunda a sexta na parte da manhã.

[![Argumentação(Escolha da daily)](https://user-images.githubusercontent.com/18370133/44695572-33504300-aa4a-11e8-84bb-a3c6e55cb11a.jpg)](https://user-images.githubusercontent.com/18370133/44695572-33504300-aa4a-11e8-84bb-a3c6e55cb11a.jpg)

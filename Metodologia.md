# Histórico de Versionamento
Data|Versão|Descrição|Autor
-|-|-|-
29/08/2018|1.0.0|Adição dos artefatos da metodologia aplicada | Arthur Diniz


## Scrum

O Scrum é uma estrutura na qual as pessoas podem abordar problemas adaptativos complexos, entregando, de forma produtiva e criativa, produtos do mais alto valor possível.

O próprio Scrum é um framework simples para colaboração efetiva de equipes em produtos complexos. Os co-criadores do Scrum [Ken Schwaber]() e [Jeff Sutherland]() escreveram o [The Scrum Guide]() para explicar o Scrum de forma clara e sucinta. Este guia contém a definição de Scrum. Essa definição consiste nos papéis, eventos, artefatos e regras do Scrum que os unem.

## O Framework

Scrum é simples. É o oposto de uma grande coleção de componentes obrigatórios interligados. Scrum não é uma metodologia. Scrum implementa o método científico do empirismo. O Scrum substitui uma abordagem algorítmica programada por uma heurística, com respeito pelas pessoas e auto-organização, para lidar com a imprevisibilidade e resolver problemas complexos. O gráfico abaixo representa Scrum como descrito por [Ken Schwaber]() e [Jeff Sutherland]() em seu livro [Software in 30 Days], que nos leva desde o planejamento até a entrega do software.

![scrumframework](https://user-images.githubusercontent.com/18387694/44786444-87524900-ab6a-11e8-92f3-6a2df532e5d3.png)

## Valores
Esses valores incluem Coragem, Foco, Compromisso, Respeito e Abertura. Leia o [Guia do Scrum]() para saber mais sobre esses valores, como eles se aplicam ao Scrum.

![scrumvalues](https://user-images.githubusercontent.com/18387694/44786604-08114500-ab6b-11e8-93de-897a64953dc6.png)

## Papéis do Time

O Time Scrum consiste em um Dono do Produto (Product Owner ou PO), a Equipe de Desenvolvimento (Devs) e um Scrum Master (SM). As equipes do Scrum são auto-organizadas e interfuncionais. Equipes auto-organizadas escolhem a melhor forma de realizar seu trabalho, em vez de serem dirigidas por outras pessoas fora da equipe. Equipes multifuncionais têm todas as competências necessárias para realizar o trabalho sem depender de outros que não fazem parte da equipe. O modelo de equipe no Scrum foi desenvolvido para otimizar a flexibilidade, a criatividade e a produtividade.

## Eventos

Eventos são usados ​​no Scrum para criar regularidade e minimizar a necessidade de reuniões não definidas no Scrum. Todos os eventos são armazenados em **time-box**. Quando a Sprint começa, sua duração é fixa e não pode ser reduzida ou aumentada. Os eventos restantes podem terminar sempre que o objetivo do evento for alcançado, garantindo que uma quantidade apropriada de tempo seja gasta sem permitir desperdício no processo. Os Eventos Scrum são:

- Sprint
- Planejamento de sprint
- Daily
- Revisão de Sprint
- Retrospectiva da Sprint


## Artefatos

Os artefatos do Scrum representam **trabalho** ou **valor** para fornecer transparência e oportunidades de inspeção e adaptação. Os artefatos definidos pelo Scrum são projetados especificamente para maximizar a transparência das principais informações, para que todos tenham o mesmo entendimento do artefato.

Os artefatos do Scrum são:

- Backlog do produto
- Backlog do Sprint
- Incremento

## Nossas Modificações

Durante a primeira semana de projeto tivemos tempo para analisar o cotidiano de cada integrante da equipe e chegar a algumas conclusões sobre como poderíamos modificar o **SCRUM** para aumentar a produtividade do time.

##### - Sprint (7 dias)
Percebemos que um bom período da sprint seria de 7 dias e que um tempo maior que isso acabaria trazendo falta de comunicação e erros no andamento do projeto.

#### - Daily seg a quinta 21:00 até 21:30 não presencial via Issue
Durante a primeira semana as dailys foram corretamente preenchidas de segunda a quinta porém no fim de semana percebemos que a maioria dos integrantes do time não tiveram tempo nem disponibilidade de responder a daily.

#### - Planejamento das 21:30 até 22:30 domingo via hangouts
Vimos que seria necessário fazer reuniões para definir o planejamento da semana e essa reunião acontece todo domingo das 21:30 até 22:30

#### - Burndown
Utilizaremos o burndown gerado pelo plugin ZenHub para ver o andamento do que planejamos.

#### - Velocity
Ainda utilizando o plugin do ZenHub vai ser útil para comparar o andamento do time durante as sprints

#### - Pair programming flexível
Como a maioria dos integrantes do time já fizeram projetos em python acreditamos que o Pair programming vai ser utilizado quando tiverem tasks mais complexas, sendo assim decidimos por deixar flexível para o próprio time decidir se vai ser necessário.

#### - Integração contínua e Deploy Contínuo
Para evitar possíveis erros na branch de produção e para melhorar o fluxo de entrega contínua vamos aplicar o conceito de **integração contínua** e **deploy contínuo** que será utilizado um fluxo de build, testes e deploy.

#### - Teste de Regressão

#### - Definição de Pronto
Vamos definir que alguma feature ou bug está concluído quando ele possuir 3 coisas
```
Código -> Teste -> Review
```
#### - Análise estática de código
Para analisar o nível do código sendo produzido vamos utilizar ferramentas de análise estática.

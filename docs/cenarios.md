| Data       | Versão | Descrição               | Autor             |
|:----------:|:------:|:-----------------------:|:-----------------:|
| 31/08/2018 | 1.0    | Criação do documento        | Romeu Antunes     |


## Cenários Geral.
Aqui estão listados e descritos os cenários que não necessitam de especificação de Ator.

###### Acessar o GitPub pelo navegador

| Título    	| Acessar o GitPub pelo navegador|
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Acessar a plataforma GitPub pelo navegador |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pós condição 1 - Acesso com sucesso |
| Atores | Visitante, Estudante, Professor ou Administrador |
| Recursos | 1 - Acesso à Internet; <br/> 2 - Computador; |
| Episódios | Usuário inicia seu computador; <br/> Usuário inicia seu navegador; <br/> Usuário digita o endereço eletrônico do GitPub; <br/> Usuário acessa com sucesso o site do GitPub; |
| Restrição | 1 - Falta de conexão com a internet; |
| Exceção | 1 - Queda/Falta de conexão tanto pelo GitPub ou pelo usuário; <br/> 2 - Endereço eletrônico inválido; |

<br/>

###### Visualizar projetos de uma disciplina

| Título    	| Visualizar projetos de uma disciplina|
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Visualizar um projeto em uma determinada disciplina |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - [Acessar o GitPub no navegador](#Acessar-o-GitPu-pelo-navegador) <br/> Pós condição 1 - Visualizar projeto <br/>|
| Atores | Visitante, Estudante, Professor ou Administrador |
| Recursos | 1 - Acesso à Internet; <br/> 2 - Computador; |
| Episódios | Usuário acessa o GitPub; <br/> Usuário busca uma disciplina; <br/> Usuário seleciona a disciplina; <br/> Usuário visualiza projeto da disciplina; |
| Restrição | 1 - Disciplina não encontrada; <br/> 2 - disciplina sem projetos;|
| Exceção | 1 - Queda/Falta de conexão tanto pelo GitPub ou pelo usuário; <br/> 2 - Usuário pesquisar disciplina inexistente; |

<br/>

###### Buscar conteúdo por meio de filtros

| Título    	| Buscar conteúdo por meio de filtros|
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Selecionar filtros para buscar um conteúdo |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - [Acessar o GitPub no navegador](#Acessar-o-GitPu-pelo-navegador) <br/> Pós condição 1 - Visualizar conteúdo pesquisado <br/>|
| Atores | Visitante, Estudante, Professor ou Administrador |
| Recursos | 1 - Acesso à Internet; <br/> 2 - Computador; |
| Episódios | Usuário acessa o GitPub; <br/> Usuário seleciona filtro(s) para a pesquisa; <br/> Usuário busca um conteúdo; <br/> Usuário visualiza conteúdo buscado; |
| Restrição | 1 - conteúdo não encontrada;|
| Exceção | 1 - Queda/Falta de conexão tanto pelo GitPub ou pelo usuário; <br/> 2 - Usuário pesquisar conteúdo inexistente; |

<br/>

## Cenários de Visitante
Aqui estão listados e descritos os cenários que o Ator Visitante pode realizar.

###### Cadastrar-se na plataforma GitPub

| Título    	| Cadastrar-se na plataforma GitPub |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar cadastro de forma efetiva na plataforma GitPub |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pós condição 1 - Cadastro efetuado com sucesso na plataforma |
| Atores | Visitante |
| Recursos | 1 - Acesso à internet <br/> 2 - Email válido |
| Episódios | Visitante [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Visitante clica no botão "Iniciar sessão" <br/> Visitante clica no botão "Cadastrar-se" <br/> Visitante preenche os dados necessários <br/> Visitante recebe um email de confirmação <br/> Visitante confirma o cadastro pelo email recebido <br/> Visitante é cadastrado com sucesso|
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Visitante sem email  |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Email já registrado |

<br/>

## Cenários de não Visitante
Aqui estão listados e descritos os cenários que o Ator necessita de autenticação.

###### Comentar em um projeto

| Título    	| Comentar em um projeto |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar um comentário em um determinado projeto |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub <br/> Pós condição 1 - Comentário enviado com sucesso |
| Atores | Estudante, Professor ou Administrador |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Usuário busca por um projeto <br/> Usuário clica em um projeto <br/> Usuário escreve um comentário na caixa de comentários <br/> Usuário clica em "evnviar" para registrar comentário|
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado  |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente <br/> 3 - Envio da caixa de comentários vazia |

<br/>

###### Se inscrever em uma disciplina

| Título    	| Se inscrever em uma disciplina |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar uma inscrição em disciplinas |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub <br/> Pós condiçao - Aluno inscrito na disciplna|
| Atores | Estudante |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Usuário busca por uma disciplina <br/> Usuário clica em se inscrever na disciplina <br/> Usuário se aceito é inscrito na disciplina |
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado <br/> |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente <br/> 3 - Disciplina não cadastrada no sistema |

<br/>

###### Gerenciar disciplinas no sistema

| Título    	| Gerenciar disciplinas no sistema |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar o gerenciamento de disciplinas no GitPub |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub |
| Atores | Professor e Administrador |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Usuário clica em "disciplinas" <br/> Usuário seleciona a opção de adicionar uma nova disciplina ou alterar uma disciplina existente <br/> Usuário confirma as alterções feitas |
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado <br/> |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente |

<br/>

###### Gerenciar projetos no sistema

| Título    	| Gerenciar projetos no sistema |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar o gerenciamento de projetos em uma disciplina no GitPub |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub |
| Atores | Professor e Administrador |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Usuário clica em "disciplinas" <br/> Usuário seleciona uma disciplina <br/> visualiza os projetos da disciplinas <br/> Usuário seleciona a opção de modificar um projeto existente ou criar um novo projeto |
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado <br/> 3 - Disciplina não possue projetos|
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente <br/> 3 - Disciplinas inexistentes |

<br/>

###### Gerenciar comentários no sistema

| Título    	| Gerenciar comentários no sistema |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar o gerenciamento de comentários em um projeto no GitPub |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub |
| Atores | Professor e Administrador |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Usuário clica em "disciplinas" <br/> Usuário seleciona uma disciplina <br/> visualiza os projetos da disciplinas <br/> Usuário seleciona um projeto <br/> Usuário seleciona comentários <br/> Usuário visualiza os comentários feitos <br/> Usuário escolhe aceitar o comentário ou excluir o comentário |
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado <br/> 3 - Disciplina não possue projetos <br/> 4 - Projeto não possui comentários |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente <br/> 3 - Disciplinas inexistentes |

<br/>

###### Linkar arquivos do git em um projeto

| Título    	| Linkar arquivos do git em um projeto |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar a referência de arquivos no Git em um projeto no GitPub |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub <br/> Pré condição 2 - Possuir arquivos em um repositório Git |
| Atores | Estudante, Professor e Administrador |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Busca a disciplina <br/> Usuário seleciona uma disciplina <br/> visualiza os projetos da disciplina <br/> Usuário cria um projeto <br/> usuário seleciona em "linkar com Git" <br/> Usuário escolhe a plataforma GitHub ou GitLab <br/> Usuário se autentica na plataforma escolhida <br/> Usuário seleciona os reposiório <br/> Usuário confirma a referência |
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado <br/> 3 - Disciplina não possue projetos <br/> 4 - Linkar com projeto já existente |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente |

<br/>

###### Linkar arquivos via upload em um projeto

| Título    	| Linkar arquivos via upload em um projeto |
| -------- | ----------------------------------------------------------------------------- |
| Objetivo | Realizar o upload de arquivos locais em um projeto no GitPub |
| Contexto | Local - Qualquer local <br/> Tempo - A qualquer horário  <br/> Pré condição 1 - Autenticar-se no GitPub |
| Atores | Estudante, Professor e Administrador |
| Recursos | 1 - Acesso à internet <br/> 2 - Cadastro válido |
| Episódios | Usuário [acessa o site do GitPub](#Acessar-o-GitPub-pelo-navegador) <br/> Usuário acessa a plataforma GitPub <br/> Usuário se atentica na plataforma <br/> Busca a disciplina <br/> Usuário seleciona uma disciplina <br/> visualiza os projetos da disciplina <br/> Usuário cria um projeto <br/> usuário seleciona em "Upload de projeto" <br/> Usuário escolhe os arquivos <br/> O usuário confirma o upload <br/> Usuário visualiza o projeto com os arquivos enviados no projeto |
| Restrição | 1 - Falta de conexão com a internet  <br/> 2 - Usuário não atenticado <br/> 3 - Disciplina não possue projetos <br/> 4 - Linkar com projeto que já possui arquivos |
| Exceção | 1 - Queda/Falta de conexão por parte do Usuário e do GitPub <br/> 2 - Cadastro inexistente |

<br/>
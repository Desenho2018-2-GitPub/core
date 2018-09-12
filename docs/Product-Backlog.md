### Histórico de Revisões

| Data       | Versão | Descrição            |         Autor             |
|:----------:|:------:|:--------------------:|:-------------------------:|
| 19/08/2018 | 0.1 | Criação do Documento com tema, épico, funcionalidades e user story  | [Arthur Diniz](https://github.com/arthurbdiniz) |
| 12/09/2018 | 0.2 | Revisão dos termos utilizados  | [Victor Moura](https://github.com/victorcmoura) |
| 13/09/2018 | 0.3 | Generalização de termos  | [Victor Moura](https://github.com/victorcmoura) |

# Versão 2

## Tema
| ID | DESCRIÇÃO |
|----|-----------|
|TM01| Repositório de projetos|

## Épicos
| ID | DESCRIÇÃO | ID RELACIONADO (TEMA) |
|----|-----------|----------------|
| EP01 | Como um usuário, eu desejo acessar e utilizar uma plataforma de centralização de projetos | TM01 |
| EP03 | Como um usuário, eu desejo me cadastrar na plataforma de centralização de projetos | TM01 |
| EP04 | Como um usuário, eu desejo interagir com outros usuários | TM01 |
| EP05 | Como um usuário, eu desejo personalizar dados da plataforma | TM01 |
| EP06 | Como um usuário, eu desejo ter ajuda no uso do sistema | TM01 |

## Funcionalidades (Features)
| ID | DESCRIÇÃO | ID RELACIONADO (ÉPICOS) |
|----|-----------|----------------|
| FT01 | Publicar projetos | EP01, EP03 |
| FT02 | Pesquisar projetos | EP01, EP03, EP04 |
| FT03 | Sugerir noticias, disciplinas e projetos  para o usuário | EP02 |
| FT04 | Chat entre usuários | EP01 |
| FT05 | Explorar conteúdos | EP01 |
| FT06 | Sistema de contas | EP01, EP05 |
| FT07 | Alterar dados pessoais | EP01, EP05 |
| FT08 | Alterar layout da aplicação | EP01, EP05 |
| FT09 | Compartilhamento de projetos em redes sociais | EP01 |
| FT10 | Organizar _feed_ de conteúdo | EP01 |
| FT11 | Recomendar projetos | EP03, EP04 |
| FT12 | Pagina de ajuda | EP06 |

## User Story

|    ID   |      Tipo     |     Eu como    |      Desejo       | De modo que | Prioridade | Status    | ID RELACIONADO (FEATURES) |
|:-------:|:-------------:|:--------------:|:-----------------:|:-----------:|:----------:|:---------:|:-------------------------------:|
|    US01    |   Funcional   | Usuário        | cadastrar no site | possa logar no site | Alta | To Do | FT06 |
|    US02    |   Funcional   | Usuário        | logar no site | tenha acesso a todas funcionalidades do Repositório | Alta | To Do | FT06 |
|    US03    |   Funcional   | Usuário        | navegar pelo feed de repositórios |    consiga ver todos os repositórios em um só lugar | Alta | To Do | FT02, FT03, FT10 |
|    US04    |   Funcional   | Usuário        | realizar publicação de arquivos contendo codigo e documentação | - | Alta | To Do | FT01 |
|    US05    |   Funcional   | Usuário        | seguir outros usuários ou repositórios | consiga visualizar os projetos publicados pelos usuários seguidos | Alta | To Do | FT02, FT03 |
|    US06    |   Funcional   | Usuário        | atribuir tags aos meus projetos | a partir da busca realizada pelos usuários, o projeto possa ser filtrado | Alta | To Do | FT05 |
|    US07    |   Funcional   | Usuário        | ter um chat | permita uma interação mais direta entre os usuários | Baixa | To Do | FT04 |
|    US08    |   Funcional   | Usuário        | curtir posts | - | Media | To Do | FT02 |
|    US09    |   Funcional   | Usuário        | realizar busca de projetos e usuários | a busca filtre o conteúdo desejado e mostre ao usuário | Alta | To Do | FT05 |
|    US10    |   Funcional   | Usuário        | acessar o perfil | consiga visualizar as informações de meu perfil, podendo fazer alterações nele  | Média | To Do | FT07 |
|    US11    |   Funcional   | Usuário        | compartilhar projetos e disciplinas | o conteúdo compartilhado fique disponível para que outros usuários consigam ver minha atividade | Média | To Do | FT09 |
|    US12    |   Funcional   | Usuário        | configurar minha conta | consiga trocar informações e preferências | Média |To Do | FT08 |
|    US13    |   Funcional   | Usuário        | editar a aparência site | consiga trazer um auto contraste | Baixa| To Do | FT08 |
|    US14    | Não Funcional | Usuário        | ver as atividades recentes do usuário | me atualize de minhas ultimas novidades | Baixa | To Do |  FT10 |
|    US15    | Não Funcional | Desenvolvedor  | criar uma pagina de ajuda | auxilie os usuários a terem uma melhor interação com o site | Média | To Do | FT12
|    US16    |   Não Funcional   | Desenvolvedor  | criar um algoritmo de recomendação | os usuários possam visualizar projetos do seu gosto, em seu feed de conteúdo, projetos de seu gosto | Alta| To Do | FT11
|    US17    |   Não Funcional   | Desenvolvedor  | resgatar do banco os posts e informações necessárias | os usuários possam visualizar seus projetos e disciplanas que já participou | Alta | To Do| FT05
|    US18    |   Não Funcional   | Desenvolvedor  | salvar no banco os posts de um usuário | seja mantido os dados de forma persistente | Alta | To Do | FT05
|    US19    | Não Funcional | Desenvolvedor  | realizar testes na API  | para garantir uma melhor qualidade do código e evitar erros|  Média | To Do | -
|    US20    | Não Funcional | Usuário        | dar upload de uma imagems com tamanho maior que 50Mb | consiga postar imagens com uma melhor qualidade | Média | To Do | FT01
|    US21    | Não Funciona  | Desenvolvedor  | limitar tamanho de upload de imagens para 100MB | evite latência no servidor e recupere os dados mais rapidamente | Alta | To Do | FT01
|    US22    |   Funcional   | Usuário        | poder editar meu projeto | consiga realizar alterações nos textos nele contido | Alta | To Do | FT10 |

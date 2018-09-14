### Histórico de Revisões

| Data       | Versão | Descrição            |         Autor             |
|:----------:|:------:|:--------------------:|:-------------------------:|
| 02/09/2018 | 1.0 | Criação do ME-R e DE-R  | [Vitor Falcão](https://github.com/vitorfhc) |
| 03/09/2018 | 2.0 | Alteração do ME-R e DE-R  | [Vitor Falcão](https://github.com/vitorfhc) |

---

## Versão 1

### ME-R

**Entidades**

|Nome|Atributos|
|:--:|:--:|
|Aluno|nome, sobrenome, **matricula**, usuario, senha|
|Professor|nome, sobrenome, **matriculaProf**, usuario, senha|
|Administrador|nome, sobrenome, **id**, usuario, senha|
|Disciplina|nome, sigla, **codigo**, visibilidade|
|Projeto|nome, visibilidade, **idProj**|

**Relacionamentos**

|Entidades|Relação|Descrição|Cardinalidade|
|:---:|:---:|:---:|:---:|
|Aluno - Disciplina|Alunos _participam_ de disciplinas|Um ou vários alunos participam de uma ou mais disciplinas|N para N|
|Aluno - Projeto|Aluno _participa de_ projeto|Um aluno pode ter um ou mais projetos, um projeto pode ser de um ou mais alunos|N para N|
|Disciplina - Projeto|Disciplina _possui_ projetos|Uma disciplina possui um ou vários projetos|1 para N|
|Professor - Disciplina|Professor _possui_ disciplinas|Um professor possui uma ou várias disciplinas|1 para N|

### DE-R
![de-r](https://github.com/Desenho2018-2/GitPub/blob/master/docs/images/de-r-v2.png?raw=true)

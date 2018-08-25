|Data|Versão|Alteração|Autor|
|:------:|:------:|:-----:|:-----:|
|23/08/2018|0.1|Criação do documento|Gabriel Ziegler|
|23/08/2018|0.2|Adição do conteúdo do estilo|Gabriel Ziegler|

# Folha de estilo do Django

## Python Style

A folha de estilo da linguagem segue as especificações da [PEP 8](https://www.python.org/dev/peps/pep-0008/)

* snake_case, não camelCase

Use:
```Python
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
```

Não use:
```Python
class Person(models.Model):
    FirstName = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=40)
```

* Identação com 4 espaços

* Identação com 4 espaços para argumentos em mais de uma linha:

Use:
```Python
raise AttributeError(
    'Here is a multine error message '
    'shortened for clarity.'
)
```

Não use:
```Python
raise AttributeError('Here is a multine error message '
                     'shortened for clarity.')
```

* Aspas simples para strings 

* Docstrings de funções seguem a [PEP 257](https://www.python.org/dev/peps/pep-0257/)

```Python
def test_foo():
    """
    A test docstring looks like this (#123456).
    """
    ...
```

* A **classe Meta** deve aparecer sempre depois da definição dos atributos da classe separado por **apenas UMA linha**.

```Python
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'people'
```

* Template: no Django, o código da template deve ser separado por **um espaço** separando das chaves.

Use:
```Python
{{ foo }}
```

Não use:
```Python
{{foo}}
```

* View: o primeiro parâmetro de uma`View` deve ser chamado **request**
```Python
def my_view(request, foo):
    # ...
```

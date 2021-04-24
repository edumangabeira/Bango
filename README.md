# Bango
## Aplicação web para acompanhamento de fluxo de caixa para uso pessoal.

- [Instruções de uso](#instruções-de-uso)
  * [O aplicativo web](#o-aplicativo-web)
  * [Clonando](#clonando)
- [Histórico de versões](#histórico-de-versões)
- [Configurações](#configurações)


### Instruções de uso

#### O aplicativo web

Após realizar login, basta inserir um rótulo para o gasto e a quantia associada no formulário principal, a aplicação atualiza uma planilha no Google Sheets com esses dados e outros campos úteis.


_tela de login_

![Tela de login](https://user-images.githubusercontent.com/26633114/115966675-17f0ab00-a505-11eb-80f7-4318d40f3aa8.PNG)

_tela com formulário_

![bango_form](https://user-images.githubusercontent.com/26633114/115966760-6d2cbc80-a505-11eb-982f-0cdc0d949f7d.png)

_planilha_

![bango_sheets](https://user-images.githubusercontent.com/26633114/115966773-79187e80-a505-11eb-8626-e08b5b9441b4.PNG)


#### Clonando

Caso queira clonar o repositório e usar o aplicativo, é preciso seguir [alguns passos](#configurações) antes de começar. Bango foi criado com base no [tutorial Flask do Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), por isso vale a pena checar esse material em caso de problemas.

### Histórico de versões

```[v.1.1]``` - Por enquanto o acesso é limitado a duas pessoas que possuem login e senha.

```[v.1.0]``` - Apenas a funcionalidade básica de atualizar a tabela de gastos, sem controle de acesso


## Configurações


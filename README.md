# Automação de Preenchimento de Formulário

Este projeto utiliza Python para automatizar o preenchimento de um formulário web usando a biblioteca `pyautogui`. O script lê dados de um arquivo CSV e insere esses dados em um formulário online.

### Funcionalidades

- Abre o Google Chrome.
- Navega até a página de login.
- Preenche as credenciais de login.
- Lê dados de um arquivo CSV.
- Preenche o formulário com os dados lidos.
- Cadastrar os produtos

### Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pyautogui`
  - `pandas`

### Prepare o arquivo produtos.csv com os seguintes cabeçalhos:

* `codigo`
* `marca`
* `tipo`
* `preco_unitario`
* `custo`
* `obs`

### Execute o script:

bash
```
python script.py
```


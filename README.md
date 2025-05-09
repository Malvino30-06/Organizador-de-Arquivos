## Organizador de Arquivos - Script em Python

Este projeto é um script em Python desenvolvido com o objetivo de organizar automaticamente arquivos em pastas nomeadas conforme suas extensões. Foi criado com foco no aprendizado de boas práticas com Python, organização de código em módulos, uso de argparse e estruturação para testes automatizados.

---

## 🚀 Funcionalidades

- ✅ Organiza arquivos com base em extensão
- ✅ Cria pastas automaticamente conforme os tipos encontrados
- ✅ Opção de simulação sem alterar os arquivos reais
- ✅ Execução por linha de comando com argumentos customizados

---

# 🛠 Tecnologias Utilizadas

- Python 3.13.3
- argparse (biblioteca padrão para argumentos via terminal)
- unittest (para testes automatizados)

---

## ⚙️ Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/Malvino30-06/Organizador-de-Arquivos.git
```

2. Acesse a pasta do projeto:

```bash
cd organizador-de-arquivos
```


3. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate   # Windows
```

4. Execute o script passando o caminho da pasta que deseja organizar:
```bash
python organizador.py /caminho/para/sua/pasta
```

5. ⚠️ Extra - Modo Simulação (sem mover arquivos):
```bash
python organizador.py /caminho/pasta --simular
```

---

## 🌍 Exemplos de Uso

python organizador.py ~/Downloads
python organizador.py C:\\Users\\User\\Desktop --simular

---

## 📁 Estrutura de Pastas

```
organizador-de-arquivos/
├── organizador.py           # Script principal com a lógica de organização
├── README.md                # Documentação do projeto
├── requirements.txt         # Lista de dependências
└── tests/
    └── test_organizador.py  # Testes automatizados com unittest
```

---

## 🚀 Possíveis Melhorias Futuras

- Interface gráfica (GUI) com Tkinter ou PyQt
- Modo "desfazer"
- Organização por data de criação ou tamanho
- Ignorar arquivos ocultos ou pastas específicas
- Suporte a logs em arquivo externo

---

## 📄 Licença

Este projeto está sob a licença MIT.

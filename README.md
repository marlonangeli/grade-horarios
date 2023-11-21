# Grade de Horários

## Descrição do Projeto

O projeto consiste na implementação de um algoritmo genético para montar a grade horários
do curso de Ciência da Computação do campus Medianeria do 1º ao 8º período.
O algoritmo gera uma distribuição de disciplinas onde não existam conflitos entre os
horários de disciplinas que são pré-requisito e suas correspondentes e nem de horários
dos professores, onde um professor não pode ministrar diferentes disciplinas no mesmo
dia e horário.

## Como executar

Para executar o projeto é necessário ter o Python 3 instalado na máquina.

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório

```bash
git clone https://github.com/marlonangeli/grade-horarios.git
```

2. Entre na pasta do projeto

```bash
cd grade-horarios
```

3. Crie um ambiente virtual

**Linux**
```bash
python3 -m venv venv
```

ou

**Windows**
```ps
python -m venv venv
```

4. Ative o ambiente virtual

**Linux**
```bash
source venv/bin/activate
```

ou

**Windows**
```ps
.\venv\Scripts\activate
```

5. Instale as dependências

```bash
pip install -r requirements.txt
```

6. Execute o projeto

**Linux**
```bash
python3 main.py
```

ou

**Windows**
```bash
python main.py
```

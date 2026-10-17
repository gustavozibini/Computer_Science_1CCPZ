# Computer Science - 1CCPZ

Exercícios, checkpoints e projetos da faculdade (Ciência da Computação, turma 1CCPZ, 2026),
organizados por tema.

## Estrutura

| Pasta | O que tem |
|---|---|
| `01_python_basico/` | Primeiras aulas de Python: input, condicionais, funções, módulos, laços, listas e matrizes. Inclui o CP1. |
| `02_algoritmos_e_estruturas/` | Busca binária, algoritmos de ordenação (bubble, selection, insertion), recursão e teste de desempenho com NumPy. |
| `03_arquitetura_de_computadores/` | ASCII e binário, simulador de CPU (fetch/decode/execute) e o projeto SpaceGuard em Arduino (`.ino`). |
| `04_projetos_e_trabalhos/` | CPs e projetos: triagem de contêineres, consumo de energia residencial, SpaceGuard (menu e versão com IA) e o controle de recarga de veículos elétricos (Raspberry Pi Pico). |
| `05_estatistica/` | Teste de hipótese com Z-score. |
| `06_javascript/` | Lista encadeada (playlist), fila e pilha em JavaScript. |
| `07_documentos/` | PDFs de Product Backlog e Sprint Backlog. |

## Como rodar

- **Python**: `python3 caminho/do/arquivo.py`
- **Bibliotecas usadas em alguns arquivos**: `numpy`, `scipy` e `ollama` (`pip install numpy scipy ollama`).
  O `spaceguard_com_ia_ollama.py` também precisa do [Ollama](https://ollama.com) instalado e do modelo: `ollama pull llama3.2:1b`.
- **Arduino**: abra `03_arquitetura_de_computadores/gs_spaceguard_arduino/gs_spaceguard_arduino.ino` no Arduino IDE.
- **Raspberry Pi Pico (MicroPython)**: o código está em `04_projetos_e_trabalhos/recarga_veiculos_eletricos_pico/`
  (`diagram.json` é o circuito para simular no [Wokwi](https://wokwi.com)).
- **JavaScript**: abra os arquivos `.html` no navegador.

## Observação

Boa parte dos arquivos de aula tem trechos comentados (`#`): são exemplos da aula guardados como anotação.
Para testá-los, remova o `#` das linhas (no PyCharm: selecione e use `Ctrl + /` ou `Cmd + /`).

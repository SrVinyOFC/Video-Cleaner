# Video Cleaner 🎥🧹

Um utilitário profissional em **Python** para limpeza e organização automática de coleções de vídeos.
O script detecta vídeos corrompidos, duplicados ou incompletos e os move para subpastas dedicadas, mantendo sua pasta de origem organizada.

---

## 🧩 Descrição

**Video Cleaner** foi desenvolvido para simplificar a manutenção de grandes bibliotecas de vídeos.
Ele utiliza o `ffprobe` (parte do pacote **FFmpeg**) para verificar a integridade e duração dos arquivos, e faz o gerenciamento automatizado das pastas com base no tipo de problema encontrado.

Além disso, acompanha um script de instalação (`setup.sh`) que cria o ambiente Python isolado, instala as dependências necessárias e executa o programa automaticamente.

---

## ⚙️ Funcionalidades principais

| Função                            | Descrição                                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Mover vídeos corrompidos**      | Detecta arquivos que não podem ser abertos pelo `ffprobe` e os move para a pasta `Corrupted`.    |
| **Mover vídeos duplicados**       | Compara o hash SHA1 de cada arquivo e move cópias duplicadas para a pasta `Duplicates`.          |
| **Mover vídeos incompletos**      | Verifica vídeos com duração muito curta (ex: < 5 segundos) e os move para a pasta `Incomplete`.  |
| **Interface de seleção de pasta** | Usa `tkinter` para abrir um explorador gráfico e permitir ao usuário escolher a pasta de origem. |
| **Organização automática**        | Cria as subpastas necessárias (`Corrupted`, `Incomplete`, `Duplicates`) automaticamente.         |

---

## 🧰 Requisitos

* **Python 3.8+**
* **FFmpeg** (instalado automaticamente via `setup.sh`)
* Módulos padrão: `os`, `shutil`, `subprocess`, `hashlib`, `tkinter`

---

## 🚀 Instalação e uso automático

O projeto vem com um script `setup.sh` que faz todo o processo de configuração automaticamente:

```bash
chmod +x setup.sh
./setup.sh
```

Esse comando irá:

1. Criar e ativar um ambiente virtual Python (`venv`)
2. Verificar e instalar o `FFmpeg`, caso necessário
3. Instalar as dependências do `requirements.txt`
4. Executar o programa principal (`main.py`)

---

## 🖥️ Execução manual (opcional)

Se preferir rodar manualmente:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 🧭 Menu principal

Ao executar o programa, será exibido um menu no terminal:

```
==== Video Cleaner ====
1 - Mover vídeos corrompidos
2 - Mover vídeos duplicados
3 - Mover vídeos incompletos
```

Após escolher a opção, basta selecionar a pasta desejada na janela gráfica que será aberta.

---

## 📂 Estrutura de pastas

```
📁 projeto/
├── main.py
├── requirements.txt
├── setup.sh
└── README.md
```

Durante a execução, o programa criará automaticamente as pastas:

```
Corrupted/
Incomplete/
Duplicates/
```

---

## 🧑‍💻 Autor

Desenvolvido por **Vinícius**, técnico e programador especializado em automação e sistemas de análise de arquivos.

---

## 🪪 Licença

Este projeto é de uso livre para fins pessoais e educacionais.


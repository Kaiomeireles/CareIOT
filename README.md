# 👤 Detecção Facial Local – Integração com o Jogo CareHero

Este projeto faz parte da Sprint de IoT & IOB e tem como objetivo desenvolver uma aplicação local de **detecção facial** utilizando **MediaPipe** e **OpenCV**.  
A solução funciona como uma etapa inicial do jogo mobile **CareHero**, permitindo verificar a presença do usuário antes de liberar o acesso ao app.

---

## 🎥 Vídeo Explicativo (YouTube)

▶️ **Assista ao vídeo da apresentação:**  
https://youtu.be/1h6KeD5LXYk

---

## 💻 Código no Repositório

🔗 **Link do código completo:**  
*([CODIGUIN](https://github.com/Kaiomeireles/CareIOT/blob/main/main.py))*

---

## 🎯 Objetivo do Projeto

Criar uma aplicação local capaz de:

- Detectar o rosto do usuário usando a câmera;
- Exibir informações da detecção em tempo real;
- Demonstrar o impacto dos parâmetros configuráveis do modelo;
- Servir como base para integração com o **CareHero**, garantindo que o jogador está presente antes de iniciar o jogo.

---

## 🧩 Relação com o CareHero

O **CareHero** é um jogo mobile gamificado com foco na evolução de um personagem.  
A detecção facial funciona como uma etapa inicial — o jogo só deve continuar quando o usuário estiver realmente na frente da câmera, tornando a experiência mais imersiva e moderna.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **OpenCV**
- **MediaPipe Face Detection**
- Bibliotecas padrão (time, os)

Tudo funciona localmente, sem envio de imagens para servidores externos.

---

## 📦 Instalação

### 1. Criar ambiente virtual
```bash
python3 -m venv venv
````

### 2. Ativar ambiente virtual

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install mediapipe opencv-python
```

---

## ▶️ Como Executar

Com o ambiente ativado:

```bash
python camera_mediapipe.py
```

A aplicação irá abrir a câmera e mostrar:

* Rosto detectado ou não;
* Confiança da detecção;
* FPS;
* Parâmetros usados.

Para sair:

```
q
```

---

## 📄 Arquivo Principal

### **camera_mediapipe.py**

Contém:

* Configuração dos parâmetros:

  * `min_detection_confidence`
  * `model_selection`
* Captura e exibição da câmera com OpenCV;
* Processamento de detecção facial com MediaPipe;
* Renderização da interface em tempo real.

---

## 🎚️ Parâmetros Ajustáveis

### 🔹 min_detection_confidence

Controla a exigência da detecção:

* Baixo → detecta mais fácil, menos preciso
* Alto → mais preciso, pode falhar em luz ruim

### 🔹 model_selection

* **0** → rosto próximo (uso normal de celular)
* **1** → rosto distante

---

## 🧪 Funcionamento Prático

A aplicação:

* Abre a câmera;
* Analisa cada frame em tempo real;
* Detecta o rosto e desenha o retângulo;
* Exibe informações úteis (FPS, número de rostos, confiança);
* Serve como camada inicial de presença no **CareHero**.

---

## ⚠️ Limitações

* Precisa de boa iluminação;
* Falha com rosto muito lateral ou coberto;
* Detecta presença, não identifica quem é o usuário;
* Depende da qualidade da câmera do dispositivo.

---

## 🚀 Próximos Passos

* Integrar diretamente na tela inicial do **CareHero**;
* Ajustar parâmetros para maior estabilidade;
* Melhorar desempenho em cenários de baixa luz;
* Evoluir para identificação real caso necessário.

---

## 📚 Integrantes do Grupo

- Kaio Vinicius Meireles Alves - RM553282

 - Lucas Alves de Souza -  RM553956

 - Lucas de Freitas Pagung -  RM553242

 - Guilherme Fernandes de Freitas - RM554323

 - João Pedro Chizzolini de Freitas - RM553172
---

## ✔️ Status

* Vídeo explicativo: **OK**
* Código funcional: **OK**
* README completo: **OK**

```

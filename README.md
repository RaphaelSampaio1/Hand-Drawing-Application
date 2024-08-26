# Hand-Drawing-Application
Lousa digital criada com visão computacional

Este é um projeto simples de uma aplicação de desenho que utiliza a biblioteca OpenCV e o `HandTrackingModule` da `cvzone` para detectar e rastrear a mão através da webcam, permitindo desenhar na tela usando os dedos.

## Funcionalidades

- **Desenhar na tela**: Desenhe na tela usando o dedo indicador.
- **Limpar a tela**: Limpe o desenho atual quando três dedos estiverem levantados.
- **Pausar o desenho**: Pause o desenho ao levantar mais ou menos de um dedo.

## Como funciona

- **Um dedo levantado**: Começa a desenhar na tela usando a ponta do dedo indicador.
- **Três dedos levantados**: Limpa todo o desenho atual.
- **Qualquer outro número de dedos**: Pausa o desenho.

## Requisitos

- Python 3.x
- OpenCV (`cv2`)
- cvzone (`HandTrackingModule`)

### Instalação das dependências

Use o pip para instalar as dependências necessárias:

```bash
pip install opencv-python cvzone

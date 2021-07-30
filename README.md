# Objetivo:
Criar um aplicativo com interface gráfica para download de vídeos (mp4) e músicas (mp3) do YouTube, apenas com a inserção do endereço (URL).

# Como foi feito:
1) Criar a interface gráfica (frame.ui) com o QTDesing da plataforma QTCreator.
2) Transformar o frame.ui em frame.py: No prompt de comando, ir até a pasta onde está
o frame.ui e digitar: pyuic5 'nome do frame'.ui -o 'nome do frame'.py -x
3) Imagem de fundo do app foi convertida de imagem.qrc para imagem.py:  No prompt de comando, ir até a pasta onde está
a imagem.qrc e digitar: pyrcc5 'nome da imagem'.qrc -o 'nome da imagem'.py
4) No arquivo frame.py: Foi utilizado a função yt_download do módulo mhyt, disponível em https://pypi.org/project/mhyt/.
Foram necessários alguns ajustes na função para correção de erros.
6) Conversão do arquivo frame.py para frame.exe: No prompt de comando, ir até a pasta onde está
frame.py e digitar: pyinstaller --onefile --noconsole 'nome do arquivo que será convertido'.py

# Observações:
1) O arquivo baixado vai estar na mesma pasta onde está o arquivo executável.
2) Caso a execução do arquivo gere algum erro, é necessário executar como administrador e/ou desabilitar o antivírus no momento do download.
 
# Images do app:

![1](https://user-images.githubusercontent.com/79408563/127662919-50cd11e0-d41c-4eb6-9337-490e6911b64f.PNG)

![2](https://user-images.githubusercontent.com/79408563/127662969-fc4abf90-4679-40d3-abc3-77d14096180c.PNG)

![3](https://user-images.githubusercontent.com/79408563/127662990-edd345aa-b535-406c-b350-c5155b615de5.PNG)


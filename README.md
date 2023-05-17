![Habla con ChatGPT](https://i.postimg.cc/j5pYpVsZ/Captura-de-pantalla-de-2023-05-01-15-34-20.png)

## Habla con ChatGPT

Este software emplea el micrófono de la laptop para reconocer cuando se habla. 

Mientras no se pronuncien las palabras "Hola" o "chatGPT" el programa no se ejecutará.

### ejemplo:

    usuario -- "Hola"
    chatGPT -- "Te escucho"
    usuario -- "¿de que color era el caballo blanco del general San martín?
    chatGPT -- "...."


En esta etapa beta, el usuario no podrá mantener un hilo conversacional ni modificar las configuraciones que se le han hecho a chatGPT modelo gpt-3.5-turbo, por lo tanto esta AI dará respuestas con humor, algo irónicas y sarcásticas de forma tal que no parezca que un HAL9000 cualquiera.


--------------------------------------------------------------------------------

# La idea de esta aplicacíon de PC es para que una persona con conocimientos básicos de informática pueda mantener una conversación oral con chatGPT y que sea de la forma más sencilla posible. 


## requisitos:

Este programa utiliza:
* openai para conectarse con chatGPT, por lo que el usuario deberá registrarse en la página web de openai.com y obtener una api key 
* Para el reconocimiento de voz se emplea SpeechRecognition con Google Speech Recognition. 

Nota: para evitar complicaciones se recomienda ejecutar este programa en una laptop y no en una PC de escritorio ya que las primeras traen incorporado un micrófono que es necesario para que el programa pueda reconocer el audio. 

Gracias Google Speech Recognition este programa se puede correr en computadoras medianamente antiguas y / o de bajos recursos


        * Conexión a Internet: si
        * Micrófono activado y configurado: si
        * Tener un API Key para poder conectarse con chatGPT: si 

--------------------------------------------------------------------------------

## aclaraciones:
* Debido a que chatGPT está limitado a expresarse en forma oral, solicitudes tales como que haga un script en python para hacer X cosa puede que tengan un resultado poco satisfactorio.
* El tiempo que tarde chatGPT puede variar dependiendo de la velocidad de conexión, la saturación de pedidos que tenga que atender en ese momento la AI
* Puede que la efectividad del reconocimiento de las palabras no sea del 100% ya que depende factores tales como: calidad del micrófono, el alcance del mismo, el ruido ambiente, como así también de la pronunciación del emisor, etc. 
* Así mismo la primera vez que se ejecute puede que tarde un poco más de tiempo en reconocerla.

--------------------------------------------------------------------------------

## información técnica:

Este programa está en fase beta y fue realizado íntegramente en el lenguaje de programación python3

## Librerías necesarias
        aiohttp==3.8.4
        aiosignal==1.3.1
        async-timeout==4.0.2
        attrs==23.1.0
        certifi==2023.5.7
        cffi==1.15.1
        charset-normalizer==3.1.0
        click==8.1.3
        cryptography==40.0.2
        frozenlist==1.3.3
        gTTS==2.3.2
        idna==3.4
        multidict==6.0.4
        openai==0.27.6
        PyAudio==0.2.13
        pycparser==2.21
        pygame==2.4.0
        pyttsx3==2.90
        requests==2.30.0
        SpeechRecognition==3.10.0
        tqdm==4.65.0
        urllib3==2.0.2
        yarl==1.9.2
# Instalación:
1. clonar el repositorio.

        git clone https://github.com/rocky-roll/speak_to_the_chatGPT
        
2. Instalar las librerias necesarias para ejecutar el programa.

        cd speak_to_the_chatGPT
        python -m pip freeze install -r requirements.txt
--------------------------------------------------------------------------------

# ¿cómo obtener la API Key para chatGPT?
1. Realizar el proceso de registración en la página web de https://platform.openai.com/overview
2. En el menú de usuario hacer clic en la opción"View API keys" https://platform.openai.com/account/api-keys
3. Elegir la opción "+ Create new secret key" completar los pasos y crear la clave. Una vez creada esta dese ser copiada ya que luego el programa no dejará volver a consultarla.

--------------------------------------------------------------------------------

# Agregar la clave generada al programa 

1. ejecute el archivo assistant.py.

        python assistant.py
1. Una vez abierto el programa ir a la barra de menú y hacer clic "Archivo/chatGPT key"
2. En la caja de texto pegar (CTRL + v) la API key previamente creada en openai y hacer clic en el botón "Enviar"
3. Luego se abrirá una caja de mensaje informándonos que si se desea aplicar los cambios habrá que cerrar la aplicación y volver a abrirla

Al reiniciar la aplicación ya se podrá conectar con chatGPT

## garantía:

No se ofrece ningún tipo de garantía

## licencia:

Este programa se publica bajo la licencia de software libre GPLv3 (https://www.gnu.org/licenses/gpl-3.0.txt)

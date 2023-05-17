![Habla con ChatGPT](https://i.postimg.cc/j5pYpVsZ/Captura-de-pantalla-de-2023-05-01-15-34-20.png)

## Habla con ChatGPT

Este software emplea el micrófono de la laptop para reconocer cuando se habla. 

Mientras no se pronuncien las palabras "Hola" o "chatGPT" el programa no se ejecutará.

### ejemplo:

    usuario -- "Hola"
    chatGPT -- "Te escucho"
    usuario -- "¿de que color era el caballo blanco del general San martín?
    chatGPT -- "...."
    usuario -- "Hola"
    chatGPT -- "Te escucho"
    usuario -- "¿Qué simboliza su sable?"
    chatGPT -- "...."


Sí se quiere iniciar un nuevo tema de conversación basta con pronunciar la palabra "Nuevo"

    usuario -- "Nuevo"
    chatGPT -- "Nueva conversación creada. Te escucho "
    usuario -- "¿existen los imanes unipolares?"
    chatGPT -- "...."

En esta etapa beta, el usuario no podrá modificar las configuraciones que se le han hecho a chatGPT. Se lo configuró para que de respuestas con humor, irónicas y sarcásticas de forma tal que no parezca que un HAL9000 cualquiera.


--------------------------------------------------------------------------------

# La idea es que una persona con  conocimientos básicos de informática pueda mantener una conversación propia con la AI de la que todos hablan y que sea de la forma más sencilla posible. 


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

# ¿cómo obtener la API Key para chatGPT?
1. Realizar el proceso de registración en la página web de https://platform.openai.com/overview
2. En el menú de usuario hacer clic en la opción"View API keys" https://platform.openai.com/account/api-keys
3. Elegir la opción "+ Create new secret key" completar los pasos y crear la clave. Una vez creada esta dese ser copiada ya que luego el programa no dejará volver a consultarla.

--------------------------------------------------------------------------------

# Agregar la clave generada al programa 
#### Windows 10
* Descomprima el archivo asistenteWin10.zip y ejecute el archivo asistente.exe
#### Gnu/Linux 64bits
* Descomprima el archivo asistenteLinux.zip y ejecute el archivo binario asistente
#### Lo mismo para ambos SO.
1. Una vez abierto el programa ir a la barra de menú y hacer clic "Archivo/chatGPT key"
2. En la caja de texto pegar la API key previamente creada en openai y hacer clic en el botón "Enviar"
3. Luego se abrirá una caja de mensaje informándonos que si se desea aplicar los cambios habrá que cerrar la aplicación y volver a abrirla

Al reiniciar la aplicación ya se podrá conectar con chatGPT

## información técnica:

Este programa está en fase beta y fue realizado íntegramente en el lenguaje de programación python3

## garantía:

No se ofrece ningún tipo de garantía

## licencia:

Este programa se publica bajo la licencia de software libre GPLv3 (https://www.gnu.org/licenses/gpl-3.0.txt)

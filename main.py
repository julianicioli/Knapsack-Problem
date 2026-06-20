import eel
from controller.mochila_controller import MochilaController

def iniciar_sistema():
    # Informa ao Eel que a pasta contendo a interface gráfica (View) chama-se 'web'
    eel.init('web/html')
    
    # Instancia o controlador para registrar as funções expostas do Python
    controller = MochilaController()
    
    print("Sistema Iniciado. Abrindo a interface gráfica...")
    
    # Abre o seu arquivo index.html em uma janela nativa do sistema
    eel.start('index.html', mode='default', size=(1100, 780))

if __name__ == "__main__":
    iniciar_sistema()
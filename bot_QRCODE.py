import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
##Updater é algo que utiliza para saber as solicitações que recebe do usuário
## qnd o usuário manda mensagem, manda algum comando....




INPUT_TEXT = 0



def start(update, context):
#add handler (manipulador do comando)

    update.message.reply_text('Olá, o que devo fazer? \n\n Usa /qr para gerar um codigo qr.')




def qr_command_handler(update, context):

    update.message.reply_text('Envia o texto para gerar o codigo QR')

    return INPUT_TEXT



def generate_qr(text):
#gerar arquivo do qrcode .jpg  

    filename = text + '.jpg'

    img = qrcode.make(text)
    img.save(filename)

    return filename


def send_qr(filename, chat):
    #primiero enviar uma acao para o telegrame a vai mostrar pro usuario o que telegram ta fazendo (digitando, gravando auido, gavadno video)
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    #sobe a foto pro usuario(mostra a foto no chat)
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    #apaga o arquivo do codigo qr
    os.unlink(filename)

def input_text(update,context):
#pega o texto que o usuario enviou e transforma no qrcode
    text = update.message.text

    filename = generate_qr(text)

    #possui informacoes do usuario (nome e ultimo nome do teleg) o id da conversa e o tipo dela(privado ou grupo...)
    chat = update.message.chat

    send_qr(filename, chat)

    return ConversationHandler.END


if __name__ == '__main__':

    updater = Updater(token='SEU_TOKEN_DO_BOTFATHER', use_context=True)
    
    dp = updater.dispatcher #dispatcher é encarregado de lidar com os comandos que entra no updater

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(
        
            entry_points = [ 
                CommandHandler('qr', qr_command_handler)
            ], 

             states={
                INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
            },

                

            fallbacks = []
            

    ))
    

    #Permite que o bot se ative, cria um ciclo infinito para permitir esses comandos
    updater.start_polling()
    updater.idle()


#ObsÇ caso queira listar para o usuario os comandos que o bot possui, tem que entrar no botfather
#mybots...
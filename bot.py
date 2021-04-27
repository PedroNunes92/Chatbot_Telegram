from telegram.ext import Updater, CommandHandler
##Updater é algo que utiliza para saber as solicitações que recebe do usuário
## qnd o usuário manda mensagem, manda algum comando....

def start(update, context):
#add handler (manipulador do comando)
    update.message.reply_text('Olá, estou aqui para responder suas dúvidas em relação as plantacões.')



if __name__ == '__main__':

    updater = Updater(token='TOKEN_FROM_BOTFATHER', use_context=True)
    
    dp = updater.dispatcher #dispatcher é encarregado de lidar com os comandos que entra no updater

    dp.add_handler(CommandHandler('start', start))
    

    #Permite que o bot se ative, cria um ciclo infinito para permitir esses comandos
    updater.start_polling()
    updater.idle()
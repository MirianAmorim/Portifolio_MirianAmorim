# Criei um gmail novo.

#Configurei os acessos:
   # Permitir aplicativos menos seguros (Ativar): https://myaccount.google.com/lesssecureapps
   # Desbloquear acesso os gmail: https://accounts.google.com/b/2/DisplayUnlockCaptcha
   # Ativar o acesso via IMAP: https://mail.google.com/mail/#settings/fwdandpop
   
# Instalei o flask_mail no terminal

from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail_settings = {
   "MAIL_SERVER": 'smtp.gmail.com',
   "MAIL_PORT": 465,
   "MAIL_USE_TLS": False,
   "MAIL_USE_SSL": True,
   "MAIL_USERNAME": 'mi.amorim.work@gmail.com',
   "MAIL_PASSWORD": 'udzssq120664'
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
   def __init__ (self, nome, email, mensagem):
      self.nome = nome
      self.email = email
      self.mensagem = mensagem

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
   if request.method == 'POST':
      formContato = Contato(
         request.form['nome'],
         request.form['email'],
         request.form['mensagem']
      )

      msg = Message(
         subject= 'Contato do seu Portfólio', 
         sender=app.config.get("MAIL_USERNAME"), 
         recipients=[app.config.get("MAIL_USERNAME")], 
         body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
         
               {formContato.mensagem}''' 
         )
      mail.send(msg)
   return render_template('send.html', formContato=formContato)

if __name__ == '__main__':
   app.run(debug=True)
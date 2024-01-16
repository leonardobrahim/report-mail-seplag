import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ast import literal_eval

from .constants import ENV, FOOTER_IMG, HEADER_IMG

SERVER = ENV['SERVER']
PW = ENV['PASSWORD']
REMETENTE = ENV['REMETENTE']
DESTINATARIOS = literal_eval(ENV['DESTINATARIOS'])
PORTA = ENV['PORTA']


def sender(subject, message):
    msg = MIMEMultipart('related')
    msg['From'] = REMETENTE
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = subject

    html_parte = MIMEText(message, 'html')
    msg.attach(html_parte)

    # header image
    image_path = HEADER_IMG
    with open(image_path, 'rb') as image_file:
        image_header = MIMEImage(image_file.read(), name='header.png')
        image_header.add_header('Content-ID', '<header_image>')
        msg.attach(image_header)

    # footer image
    image_footer = FOOTER_IMG
    with open(image_footer, 'rb') as image_file_footer:
        image_footer = MIMEImage(image_file_footer.read(), name='footer.png')
        image_footer.add_header('Content-ID', '<footer_image>')
        msg.attach(image_footer)

    # send the email
    with smtplib.SMTP(SERVER, PORTA) as server:
        server.starttls()
        server.login(REMETENTE, PW)
        server.sendmail(REMETENTE, DESTINATARIOS, msg.as_string())

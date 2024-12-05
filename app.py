from email.mime.image import MIMEImage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv('SERVER')
PW = os.getenv('PASSWORD')
REMETENTE = os.getenv('REMETENTE')
DESTINATARIOS = os.getenv('DESTINATARIOS').split(',')
PORTA = os.getenv('PORTA')


def apply_warning_highlight(log):
    if 'warning' in log.lower():
        return f'<li style="list-style: none; margin-top: 15px; border: 1px solid red; padding: 15px; border-radius: 15px; text-align: center;">{log}</li>'
    else:
        return f'<li style="list-style: none; margin-top: 15px; border: 1px solid #C8C8C8; padding: 15px; border-radius: 15px; text-align: center;">{log}</li>'


def send_mail(assunto, corpo, tabela):
    msg = MIMEMultipart('related')
    msg['From'] = REMETENTE
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = assunto
    
    html_parte = MIMEText(
       f'<html><head></head>'
        + '<body style="border-radius: 15px; width: 50vw; min-width: 330px; padding: 20px; border: solid #C8C8C8 1px; text-align: center;">'
        + '<div style="border-radius: 10px; width: 250px; font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande", "Lucida Sans Unicode", Geneva, Verdana, sans-serif; margin: 0 auto;" >'
        + f'<img src="cid:header_image" style="border-radius: 10px; width: 100%; height: 100%;" alt="Header_png"> {corpo}{tabela}</div>'
        + f'<img src="cid:footer_image" style="border-radius: 10px; width: 100%; height: 100%;" alt="Footer_png"></body></html>',
        'html',
    )
    msg.attach(html_parte)

    # Attach the image
    image_path = './header.png'
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name='header.png')
        image.add_header('Content-ID', '<header_image>')
        msg.attach(image)

    # Attach the image
    image_footer = './footer.png'
    with open(image_footer, 'rb') as image_file_footer:
        imageFooter = MIMEImage(image_file_footer.read(), name='footer.png')
        imageFooter.add_header('Content-ID', '<footer_image>')
        msg.attach(imageFooter)

    # Send the email
    with smtplib.SMTP(SERVER, PORTA) as server:
        server.starttls()
        server.login(REMETENTE, PW)
        server.sendmail(REMETENTE, DESTINATARIOS, msg.as_string())


if __name__ == '__main__':
    today_date = datetime.now().strftime('%Y-%m-%d')
    with open('logfile.txt', 'r', encoding='utf-8') as txt_file:
        all_logs = txt_file.readlines()
        dateNowLog = [log for log in all_logs if log.startswith(today_date)]

    lista = f'<ul style="font-size: 15px;text-align: center; gap: 10px; list-style-type: none; margin-block: 50px;  padding-left: 20px; padding-right: 20px;">' + ''.join([
        apply_warning_highlight(log) for log in dateNowLog
    ]) + '</ul>'

    send_mail(
        f'EMAIL DE TESTE: {today_date}',
        f'<h1 style=" border-bottom: 1px solid #C8C8C8; font-size: 40px; text-align: center; color: #1e43a2; font-weight: bold;">Email de teste - {today_date}</h1>',
        lista
    )

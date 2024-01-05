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
        return f'<li style="list-style: none; margin-top: 15px; border: 1px solid red; padding: 15px; border-radius: 15px;">{log}</li>'
    else:
        return f'<li style="list-style: none; margin-top: 15px; border: 1px solid gray; padding: 15px; border-radius: 15px;">{log}</li>'


def send_mail(assunto, corpo, tabela):
    msg = MIMEMultipart('related')  # Use 'related' for images
    msg['From'] = REMETENTE
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = assunto

    html_parte = MIMEText(
        f'<html><head></head>'
        + '<body style="border-radius: 15px ;width: 50vw; padding: 20px; border: solid black 1px; text-align: center;">'
        + '<div style=" border-radius: 10px; width: 250px; font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande", "Lucida Sans Unicode", Geneva, Verdana, sans-serif;" >'
        + f'<img src="cid:header_image" style="border-radius: 10px; width: 100%; height: 100%;" alt="">{corpo}{tabela}</div></body></html>',
        'html',
    )
    msg.attach(html_parte)

    # Attach the image
    image_path = './header.png'
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name='header.png')
        image.add_header('Content-ID', '<header_image>')
        msg.attach(image)

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

    lista = f'<ul style=" align-items: center; border-top: 1px solid gray; gap: 10px;">' + ''.join([
        apply_warning_highlight(log) for log in dateNowLog
    ]) + '</ul>'

    send_mail(
        f'BI INTEGRADO - LOG: {today_date}',
        f'<h1 style="text-align: center; color: #1e43a2; font-weight: bold;">Relatorio Diario - {today_date}</h1>',
        lista
    )

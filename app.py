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
        return f'<li><font color="red">{log}</font></li>'
    else:
        return f'<li>{log}</li>'

def send_mail(assunto, corpo, tabela):
    msg = MIMEMultipart('alternative')
    msg['From'] = REMETENTE
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = assunto

    html_parte = MIMEText(
        '<html><head></head>'
        + '<body>'
        + corpo
        + '<br />'
        + tabela
        + '</body></html>',
        'html',
    )
    msg.attach(html_parte)

    with smtplib.SMTP(SERVER, PORTA) as server:
        server.starttls()
        server.login(REMETENTE, PW)
        server.sendmail(REMETENTE, DESTINATARIOS, msg.as_string())

if __name__ == '__main__':
    today_date = datetime.now().strftime('%Y-%m-%d')
    with open('logfile.txt', 'r', encoding='utf-8') as txt_file:
        all_logs = txt_file.readlines()
        dateNowLog = [log for log in all_logs if log.startswith(today_date)]
    
    lista = '<ul style="list-style-type: square; padding: 10px; background-color: #C8D6E4; border-radius: 5px; margin-top: 10px; margin-bottom: 10px;">' + ''.join([
        f'<li style="margin-bottom: 5px; color: #fff; font-size: 14px; { "border-bottom: 1px solid black;" if i != len(dateNowLog) - 1 else "" } list-style: none;">{apply_warning_highlight(log)}</li>' for i, log in enumerate(dateNowLog)
    ]) + '</ul>'

    send_mail(
        f'BI INTEGRADO - log do dia {today_date}',
        '<h2 style="text-align:center;">BOM DIA, LOGS DE HOJE</h2>',
        lista
    )
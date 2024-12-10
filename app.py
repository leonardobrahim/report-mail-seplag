from email.mime.image import MIMEImage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
import os
from gerartabela import html_table
load_dotenv()

SERVER = os.getenv('SERVER')
PW = os.getenv('PASSWORD')
REMETENTE = os.getenv('REMETENTE')
DESTINATARIOS = os.getenv('DESTINATARIOS').split(',')
PORTA = os.getenv('PORTA')


def read_html(df_html):
    with open(df_html, 'r', encoding='utf-8') as file:
        return file.read()


def send_mail(assunto, titulo, table):
    msg = MIMEMultipart('related')
    msg['From'] = REMETENTE
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = assunto
    
    html_parte = MIMEText(
       f'<html><head></head>'
        + '<body style="border-radius: 15px; width: 50vw; min-width: 330px; padding: 20px; border: solid #C8C8C8 1px; text-align: center;">'
        + '<div style="border-radius: 10px; width: 250px; font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande", "Lucida Sans Unicode", Geneva, Verdana, sans-serif; margin: 0 auto;" >'
        + f'<img src="cid:header_image" style="border-radius: 10px; width: 100%; height: 100%;" alt="Header_png"> {titulo}{table}</div>'
        + f'<img src="cid:footer_image" style="border-radius: 10px; width: 100%; height: 100%; margin-top: 25px;" alt="Footer_png"></body></html>',
        'html',
    )
    msg.attach(html_parte)

    image_path = './header.png'
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name='header.png')
        image.add_header('Content-ID', '<header_image>')
        msg.attach(image)

    image_footer = './footer.png'
    with open(image_footer, 'rb') as image_file_footer:
        imageFooter = MIMEImage(image_file_footer.read(), name='footer.png')
        imageFooter.add_header('Content-ID', '<footer_image>')
        msg.attach(imageFooter)

    with smtplib.SMTP(SERVER, PORTA) as server:
        server.starttls()
        server.login(REMETENTE, PW)
        server.sendmail(REMETENTE, DESTINATARIOS, msg.as_string())


if __name__ == '__main__':
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    table = f"""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin: 20px;
                    }}
                    .styled-table {{
                        margin: 0 auto;
                        border-collapse: collapse;
                        width: 90%;
                    }}
                    .styled-table th, .styled-table td {{
                        border: 1px solid #dddddd;
                        padding: 8px;
                        text-align: center;
                    }}
                    .styled-table th {{
                        background-color: #f4f4f4;
                    }}
                </style>
            </head>
            <body>
                {html_table}
            </body>
            </html>
            """
                
    
    send_mail(
        f'Posição da execução orçamentária por UO 2024: {today_date}',
        f'<h1 style=" border-bottom: 1px solid #C8C8C8; font-size: 25px; text-align: center; color: #1e43a2; font-weight: bold;">Posição da execução orçamentária por UO 2024<br>{today_date}</h1>',
        table
    )

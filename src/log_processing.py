from datetime import datetime
from .constants import TODAY_DATE


def subject_title(project_name):
    return f'{project_name}: logs do dia {TODAY_DATE}'


def body_title():
    return \
        f'<h1 style="' \
        + ' text-align: center;' \
        + ' color: #1e43a2;' \
        + ' font-weight: bold;' \
        + f' ">Relatório Diário - {TODAY_DATE}</h1>'


def all_logs(log_file):
    with open(log_file, 'r', encoding='utf-8') as txt_file:
        all_logs = txt_file.readlines()

    logs_with_date = [
        (datetime.strptime(log_[:10], '%Y-%m-%d'), log_[24:].replace('\n', '')) 
        for log_ in all_logs]
        
    return logs_with_date


def last_logs(log_file):
    all_logs_ = all_logs(log_file)
    return [
        (date_, log_) for date_, log_ in all_logs_ if date_ == all_logs_[-1][0]
    ]


def body_content(log_file):
    last_logs_  = last_logs(log_file)
    return log_content_styled(last_logs_)
    

def log_content_styled(log):
    highlight_log = ''.join(
        [apply_warning_highlight(log_) for _, log_ in log]
        )
    
    return \
        '<ul style="font-size: 15px;' \
        +' text-align: center; gap: 10px;' \
        + ' list-style-type: none;' \
        + ' margin-block: 50px;' \
        + ' padding-left: 20px;' \
        + ' padding-right: 20px;">' \
        +  f'{highlight_log}' \
        + '</ul>'


def apply_warning_highlight(log):
    if 'warning' in log.lower():
        return \
            '<li'  \
                + ' style="list-style: none;' \
                + ' margin-top: 15px;' \
                + ' border: 1px solid red;' \
                + ' padding: 15px;' \
                + ' border-radius: 15px;' \
                + ' text-align:' \
                + f' center;">{log}' \
            + '</li>'
    else:
        return \
            '<li' \
                + ' style="list-style: none;' \
                + ' margin-top: 15px;' \
                + ' border: 1px solid #C8C8C8;' \
                + ' padding: 15px;' \
                + ' border-radius: 15px;' \
                + f' text-align: center;">{log}' \
            + '</li>'


def mime_text(body_title, body_content):
    font_family = \
        'Geneva,' \
        + ' Verdana,' \
        + ' sans-serif;'
    
    return \
        '<html>' \
        + '<head></head>' \
        + '<body' \
            + ' style="border-radius: 10px;' \
            + ' padding: 20px;' \
            + ' border: solid #C8C8C8 1px;' \
            + ' width: 50vw;' \
            + f' font-family: {font_family} " >' \
            + ' <img src="cid:header_image" style="border-radius: 10px;' \
            + ' width: 100%; height: 100%;" alt="Header_png">' \
            + f' {body_title}{body_content}<img src="cid:footer_image"' \
            + ' style="border-radius: 10px; width: 100%; height: 100%;"' \
            + ' alt="Footer_png"></body></html>'

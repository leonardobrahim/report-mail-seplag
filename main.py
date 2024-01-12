from src import send_mail
from src import subject_title, mime_text, body_content, body_title


subject_ = subject_title('BI Integrado')
body_title_ = body_title()
body_content_ = body_content('logfile.txt')
body_ = mime_text(body_title_, body_content_)

send_mail(subject_, body_)

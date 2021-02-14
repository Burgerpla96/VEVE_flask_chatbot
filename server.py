from waitress import serve
from app import app #app.py에서 변수 app

serve(app,host='0.0.0.0',port=8383)


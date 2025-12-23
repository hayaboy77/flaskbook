from flask import Flask, request



print(f'__name__ : {__name__}' )

app=Flask(__name__)

@app.route('/')
def index():
    return "<p>안녕</p>"


@app.route('/trans')
def trans():
    return "<p>교통현황 대시보드</p>"


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Christmas')
    return f"<p>안녕 {name}</p>"
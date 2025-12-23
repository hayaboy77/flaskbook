from flask import Flask, request, render_template



print(f'__name__ : {__name__}' )

app=Flask(__name__)

@app.route('/',  endpoint='root')
def index():
    return "<p>안녕</p>"


@app.route('/tomorrow/<menu>')
def tomorrow(menu):
    return render_template('index.html', menu=menu)


# @app.route('/trans1')
@app.get('/trans')
def transGet():
    return "<p>교통현황 대시보드-GET방식</p>"


@app.post('/trans')
def transPost():
    return "<p>교통현황 대시보드-POST방식</p>"


@app.route('/hello')
def hello():
    name = request.args.get('name2', 'Christmas')
    return f"<p>안녕 {name}</p>"


# @app.route 데코레이터의 Rule에 변수를 지정할 수 있다. 변수는 <변수명>
@app.route('/hello2/<height>')
def hello2(height):    
    height=int(height)
    result=height+7
    return f"<p>안녕 {result}</p>"
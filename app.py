from bottle import Bottle, run
from database import engine

app = Bottle()

@app.route('/', method='GET')
def home():
    # acceso a db
    conn = engine.connect()
    stmt = text(("SELECT * FROM artists").format())
    rows = conn.execute(stmt)
    for r in rows:
        print(r)
    # respuesta
    return "Hello World!"

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
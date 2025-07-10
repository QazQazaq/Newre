from flask import Flask
from flask_cors import CORS
from utils.db import init_mongo, mongo  # <- make sure `init_mongo` is imported
from overlays import overlays_bp

app = Flask(__name__)
CORS(app)

init_mongo(app)

app.register_blueprint(overlays_bp)

@app.route('/api/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(port=3001)

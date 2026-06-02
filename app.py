from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = os.getenv('HOSTNAME', ' MO Alaa ')
    return render_template('index.html', 
                         current_time=current_time,
                         hostname=' MO Alaa ')

@app.route('/health')
def health():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
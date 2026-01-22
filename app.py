from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Simple Flask Server',
        'version': '1.0.0',
        'endpoints': ['/', '/health', '/api/info']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
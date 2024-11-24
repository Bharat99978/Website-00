from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Your Python app is running."

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code')
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return {"result": exec_globals}, 200
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

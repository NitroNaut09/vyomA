import logging
from flask import Flask, render_template, request, make_response, escape

app = Flask(__name__, template_folder='templates', static_folder='static')
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET'])
def index():
    try:
        user_input = request.args.get('input')
        sanitized_input = escape(user_input)
        response = make_response(render_template('index.html', input=sanitized_input))
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        return response
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')

if __name__=='__main__':
    app.run(debug=True)

from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def index():
    # ambil header dari objeck request
    headers = request.headers
    response = ['%s = %s' % (key, value) \
            for key, value in sorted(headers.items())
        ]
    response = '<br/>'.join(response)
    return response

@application.route('/browser')
def browser():
    browseragent = request.headers.get('User-Agent')
    return '<h2>Menggunakan : %s </h2>' % browseragent 

if __name__=='__main__':
    application.run(debug=True)
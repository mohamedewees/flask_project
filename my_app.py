from flask import Flask, request, render_template

app = Flask(__name__,template_folder=r"D:\programming\python\web_app\web_design",static_folder=r"D:\programming\python\web_app\web_design\static")

@app.route('/')
# def home():
#     return "Hello, World!"
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
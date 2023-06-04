from flask import Flask, render_template
import subprocess
import os

app_root = os.path.dirname(os.path.abspath(__file__))
main_script_path = os.path.join(app_root, 'pose_tracking', 'main.py')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-main')
def run_main():
    subprocess.Popen(['python', main_script_path])
    return 'Running main.py'

if __name__ == '__main__':
    app.run()

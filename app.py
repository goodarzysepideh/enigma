from flask import Flask, request, render_template
from flask_api import status

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('page1.html');

@app.route('/page2')
def retrun_page2():
    return render_template('page2.html')

@app.route('/page3')
def retrun_page3():
    return render_template('page3.html')    

@app.route('/page1', methods=['POST'])
def mpars():
    #count = get_hit_count()
    print("look here:" , request.form['result'])
    if request.form['result'] == 'No beginning! No ending!':
        return 'page2', status.HTTP_200_OK
    else:
        return 'alaki', status.HTTP_400_BAD_REQUEST

if __name__ == "__main__":
    app.run(host="localhost", port=5000 , debug=True)

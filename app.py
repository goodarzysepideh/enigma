from flask import Flask, request, render_template
from flask_api import status

app = Flask(__name__)

@app.route('/')
def start_page():
    return render_template('start.html');

@app.route('/page1')
def first_page():
    return render_template('page1.html');

@app.route('/page1sp', methods=['POST'])
def mpars():
    #count = get_hit_count()
    print("look here:" , request.form['result'])
    if request.form['result'] == 'No beginning! No ending!':
        return 'family', status.HTTP_200_OK
    else:
        return 'alaki', status.HTTP_400_BAD_REQUEST

@app.route('/family')
def retrun_page2():
    return render_template('page2.html')

@app.route('/detective')
def retrun_page3():
    return render_template('page3.html')

@app.route('/rooma')
def retrun_page4():
    return render_template('page4.html')

@app.route('/page4p1', methods=['POST'])
def parsdecripted():
    print("look here:" , request.form['result'])
    if request.form['result'] == 'the rooms are linked':
        return 'grandpa', status.HTTP_200_OK
    else:
        return 'alaki', status.HTTP_400_BAD_REQUEST

@app.route('/grandpa')
def retrun_page5():
    return render_template('page5.html')

@app.route('/page4p2', methods=['POST'])
def parsHash():
    print("look here:" , request.form['result'])
    if request.form['result'] == '3C14D7C01FFB526638B434E4FD0E13AF':
        return 'nightstand', status.HTTP_200_OK
    else:
        return 'alaki', status.HTTP_400_BAD_REQUEST

@app.route('/page4p3', methods=['POST'])
def parsHash3():
    print("look here:" , request.form['result'])
    if request.form['result'] == 'pfpZ4Xayj7fNwIu2bDTL4UbwAewk1datIwLU9wZ/aH6yIMsuf4/WohWisPGBseWJzohDDCAjpQRUbYtQwjAzZ0W1w9AN21A2aKcks6p7uT8kafysKQM+I4fkL3/N6d1U03wYD6xROcdEZE9So9i0JRv8KncgN98xEAbai3CjZNQ=':
        return 'bed', status.HTTP_200_OK
    else:
        return 'alaki', status.HTTP_400_BAD_REQUEST

@app.route('/nightstand')
def retrun_page6():
    return render_template('page6.html')

@app.route('/bed')
def retrun_page7():
    return render_template('page7.html')

@app.route('/page7p', methods=['POST'])
def sendpacket():
    print("look here!")
    return 'We are with you, right here, not right now!', status.HTTP_200_OK

@app.route('/page7ans', methods=['POST'])
def parsans():
    print("look here:" , request.form['result'])
    if request.form['result'] == 'We are with you, right here, not right now!':
        return 'continue', status.HTTP_200_OK
    else:
        return 'alaki', status.HTTP_400_BAD_REQUEST

@app.route('/continue')
def retrun_page8():
    return render_template('continue.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000 , debug=True)

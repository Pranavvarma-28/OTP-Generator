from flask import Flask, render_template, request
import random

app = Flask(__name__)

otp = ""  # Global OTP

@app.route('/')
def home():
    global otp
    otp = str(random.randint(100000, 999999))  # ✅ Generate fresh OTP only on direct visit
    return render_template('main.html', otp=otp)

@app.route('/login', methods=['POST'])
def login():
    global otp
    username = request.form['username']
    entered_otp = request.form['otp_input']

    # ✅ Compare entered OTP with current one
    if entered_otp == otp:
        result = f"✅ Hello {username}, login successful!"
    else:
        result = f"❌ Hello {username}, login failed!"

    # ✅ Show result and keep OTP stable
    return render_template('main.html', otp=otp, result=result, username=username)

if __name__ == '__main__':
    app.run(debug=True)
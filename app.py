from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unlock_wallet', methods=['POST'])
def unlock_wallet():
    passphrase = request.form.get('passphrase')
    
    if passphrase:
        print(f"Unlocking wallet with passphrase: {passphrase}")
        return f"Wallet unlocked with passphrase: {passphrase}"
    else:
        return "Passphrase is required. Please try again."

if __name__ == '__main__':
    app.run(debug=True)

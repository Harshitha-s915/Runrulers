from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret'  # Use any random string

# Simple hardcoded user database
USERS = {'admin': 'password123', 'ngo': 'ngo123'}

# Data storage
surplus_food = []
donation_logs = []

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/add_food', methods=['POST'])
def add_food():
    if 'username' not in session:
        return jsonify({"error": "Login required"}), 401
    data = request.json
    data['id'] = len(surplus_food) + 1
    data['status'] = 'available'
    surplus_food.append(data)
    return jsonify({"message": "Food registered!", "food": data})

@app.route('/list_food', methods=['GET'])
def list_food():
    if 'username' not in session:
        return jsonify([])
    return jsonify(surplus_food)

@app.route('/update_status', methods=['POST'])
def update_status():
    if 'username' not in session:
        return jsonify({"error": "Login required"}), 401
    data = request.json
    for item in surplus_food:
        if item['id'] == data['id']:
            item['status'] = data['status']
            donation_logs.append({
                "id": item['id'],
                "status": item['status'],
                "timestamp": datetime.now().isoformat()
            })
            return jsonify({"message": "Status updated!", "item": item})
    return jsonify({"error": "Food not found"}), 404

@app.route('/safety_check', methods=['POST'])
def safety_check():
    if 'username' not in session:
        return jsonify({"error": "Login required"}), 401
    data = request.json
    for item in surplus_food:
        if item['id'] == data['id']:
            item['safety_check'] = data['check']
            return jsonify({"message": "Safety check updated!", "item": item})
    return jsonify({"error": "Food not found"}), 404

@app.route('/donation_logs', methods=['GET'])
def view_logs():
    if 'username' not in session:
        return jsonify([])
    return jsonify(donation_logs)

if __name__ == '__main__':
    app.run(debug=True)

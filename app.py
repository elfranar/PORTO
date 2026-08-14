import os
import sqlite3
import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')

def init_db():
    """Initializes the SQLite database and creates the messages table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app loads
init_db()

@app.route('/')
def home():
    """Renders the main portfolio page."""
    return render_template('index.html')

@app.route('/project/co2-to-methanol')
def co2_methanol_project():
    """Renders the CO2 to Methanol Reactor Project details page."""
    return render_template('project_co2_methanol.html')

@app.route('/project/biochemistry')
def biochemistry_project():
    """Renders the Biochemistry Papain Enzyme Isolation Project details page."""
    return render_template('project_biochemistry.html')

@app.route('/project/computational-chemistry')
def computational_chemistry_project():
    """Renders the Computational Chemistry Kinetic Simulation Project details page."""
    return render_template('project_computational_chemistry.html')

@app.route('/project/otp')
def otp_project():
    """Renders the OTP Verification System Project details page."""
    return render_template('project_otp.html')

@app.route('/project/notify')
def notify_project():
    """Renders the NotifyX System Console Project details page."""
    return render_template('project_notify.html')



@app.route('/api/contact', methods=['POST'])
def contact():
    """Handles async contact form submissions."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'No data provided'}), 400

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        # Simple backend validation
        if not name or not email or not subject or not message:
            return jsonify({'success': False, 'message': 'All fields are required.'}), 400

        # Basic email regex validation
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            return jsonify({'success': False, 'message': 'Please enter a valid email address.'}), 400

        # Save to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO messages (name, email, subject, message) VALUES (?, ?, ?, ?)',
            (name, email, subject, message)
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Thank you! Your message has been sent successfully.'})

    except Exception as e:
        app.logger.error(f"Error saving contact message: {str(e)}")
        return jsonify({'success': False, 'message': 'An internal error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    # Run the application locally
    app.run(debug=True, port=5000)

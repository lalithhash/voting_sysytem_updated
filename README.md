<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voting System - README</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
        h1, h2, h3 { color: #333; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        code { font-family: monospace; color: #d63384; }
    </style>
</head>
<body>
    <h1 align="center">Voting System</h1>
    <p align="center">
        <img src="https://raw.githubusercontent.com/github/explore/main/topics/flask/flask.png" align="center" width="15%">
    </p>
    
    <h2>Overview</h2>
    <p>This is a Flask-based voting system designed for elections in a medical institution. The system allows users to register, log in, and cast their votes securely. It also provides an admin dashboard to manage election data.</p>
    
    <h2>Features</h2>
    <ul>
        <li><b>User Authentication:</b> Secure login and signup system.</li>
        <li><b>Candidate Display:</b> Shows available candidates for each position.</li>
        <li><b>Voting Mechanism:</b> Allows users to vote once per position.</li>
        <li><b>Admin Dashboard:</b> Manage candidates and view voting results.</li>
    </ul>
    
    <h2>Project Structure</h2>
    <pre>
├── app.py             # Main Flask application
├── instance/          # Configuration and database files (if any)
├── static/            # CSS, JavaScript, and image files
├── templates/         # HTML templates for UI rendering
    </pre>
    
    <h2>Installation</h2>
    <h3>Prerequisites</h3>
    <p>Ensure you have the following installed:</p>
    <ul>
        <li><b>Python (3.x)</b></li>
        <li><b>Flask</b></li>
        <li><b>pip (Python package manager)</b></li>
    </ul>
    
    <h3>Setup Instructions</h3>
    <ol>
        <li><b>Clone the Repository</b>
            <pre><code>git clone https://github.com/lalithhash/sign-language-recognition.git
cd voting_sysytem_updated-main</code></pre>
        </li>
        <li><b>Create a Virtual Environment</b>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
        </li>
        <li><b>Install Dependencies</b>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><b>Run the Application</b>
            <pre><code>python app.py</code></pre>
        </li>
        <li><b>Access the Web Interface</b>
            <p>Open your browser and go to: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></p>
        </li>
    </ol>
    
    <h2>Usage</h2>
    <ol>
        <li><b>Register/Login</b> as a user.</li>
        <li><b>View the available candidates</b> for different positions.</li>
        <li><b>Cast your vote</b> securely.</li>
        <li><b>Admins</b> can log in to manage candidates and view results.</li>
    </ol>
    
    <h2>Contributing</h2>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
        <li>Commit your changes (<code>git commit -m "Added new feature"</code>).</li>
        <li>Push to GitHub (<code>git push origin feature-branch</code>).</li>
        <li>Submit a Pull Request.</li>
    </ol>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
    
    <hr>
    <p align="center">Feel free to contribute and improve this voting system! 🚀</p>
</body>
</html>


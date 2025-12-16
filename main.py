import sys
import os
from flask import Flask

# Keep the project root as the path
project_root = r"C:\Users\matth\personalProjects\ForageStudy"
sys.path.append(project_root)

# CHANGE THIS LINE: Add 'backend.' to the front
from backend.api.account import account_bp 

app = Flask(__name__)

app.register_blueprint(account_bp, url_prefix='/api/accounts')

if __name__ == '__main__':
    print("🚀 Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)
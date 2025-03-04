from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key-123'  # Change this for production
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    voting_type = db.Column(db.String(10), nullable=False, default='single')  # 'single' or 'multiple'
    candidates = db.relationship('Candidate', backref='post', lazy=True, cascade='all, delete-orphan')

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    votes = db.Column(db.Integer, default=0)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

# Create tables and admin user
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username="SUBHASH@GS").first():
        admin_user = User(
            username="SUBHASH@GS",
            password_hash=generate_password_hash("subhash")
        )
        db.session.add(admin_user)
        db.session.commit()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    posts = Post.query.all()
    return render_template('dashboard.html', posts=posts)

@app.route('/create-post', methods=['POST'])
def create_post():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    post_title = request.form.get('post_title')
    voting_type = request.form.get('voting_type')  # 'single' or 'multiple'
    candidates = request.form.get('candidates').split('\n')
    
    new_post = Post(title=post_title, voting_type=voting_type)
    db.session.add(new_post)
    db.session.commit()
    
    for name in candidates:
        name = name.strip()
        if name:
            new_candidate = Candidate(name=name, post=new_post)
            db.session.add(new_candidate)
    
    # Add NOTA option
    nota_candidate = Candidate(name="NOTA (None of the Above)", post=new_post)
    db.session.add(nota_candidate)
    
    db.session.commit()
    flash('Post created successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/delete-post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        for post in Post.query.all():
            if post.voting_type == 'single':
                candidate_id = request.form.get(f'post_{post.id}')
                if candidate_id:
                    candidate = Candidate.query.get(candidate_id)
                    candidate.votes += 1
            else:  # Multiple voting
                candidate_ids = request.form.getlist(f'post_{post.id}')
                for candidate_id in candidate_ids:
                    candidate = Candidate.query.get(candidate_id)
                    candidate.votes += 1
        db.session.commit()
        flash('Vote submitted successfully!', 'success')
        return redirect(url_for('home'))
    
    posts = Post.query.all()
    return render_template('vote.html', posts=posts)

@app.route('/results')
def results():
    if not session.get('logged_in'):
        flash('You must be logged in to view results.', 'danger')
        return redirect(url_for('login'))
    
    posts = Post.query.all()
    return render_template('results.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
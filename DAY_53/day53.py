from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['UPLOAD_FOLDER'] = 'DAY_53/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# مدل پایگاه داده برای عکس‌ها
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    caption = db.Column(db.String(200))

# ایجاد دیتابیس (فقط یک بار اجرا شود)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    photos = Photo.query.all()
    return render_template('index.html', photos=photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        caption = request.form['caption']
        
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            new_photo = Photo(filename=filename, caption=caption)
            db.session.add(new_photo)
            db.session.commit()
            
            flash('عکس با موفقیت آپلود شد!', 'success')
            return redirect(url_for('home'))
    
    return render_template('upload.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
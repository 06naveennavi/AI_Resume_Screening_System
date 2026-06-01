import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from resume_parser import parse_resume_text
from skill_extractor import extract_skills
from recommender import recommend_jobs

# Define allowed upload types and configure the upload folder
ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

# Create Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Limit upload size to 10MB
app.secret_key = 'replace-this-with-a-secure-random-key'


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render the home page with the resume upload form."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    """Handle the resume upload and redirect to analysis page."""
    if 'resume' not in request.files:
        flash('No file part in the request. Please select a PDF resume.')
        return redirect(request.url)

    file = request.files['resume']

    if file.filename == '':
        flash('No selected file. Choose a resume PDF to upload.')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return redirect(url_for('analyze', filename=filename))

    flash('Unsupported file type. Please upload a PDF file.')
    return redirect(request.url)


@app.route('/analyze')
def analyze():
    """Analyze the uploaded resume and show recommendations."""
    filename = request.args.get('filename')
    if not filename:
        flash('No file was provided for analysis.')
        return redirect(url_for('index'))

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))

    if not os.path.exists(file_path):
        flash('Uploaded resume not found. Please upload again.')
        return redirect(url_for('index'))

    # Parse the resume into clean text
    resume_text = parse_resume_text(file_path)
    # Extract skills from the resume text
    extracted_skills = extract_skills(resume_text)
    # Recommend best matching jobs based on skills
    recommendations = recommend_jobs(extracted_skills)

    return render_template(
        'result.html',
        extracted_skills=extracted_skills,
        recommendations=recommendations,
        resume_text=resume_text[:1500]  # limit preview length for display
    )


if __name__ == '__main__':
    # Ensure the upload directory exists before starting the server
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)

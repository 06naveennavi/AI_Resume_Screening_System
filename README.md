# AI Resume Screening & Job Recommendation System

## Project Overview
This project provides a production-ready AI-powered resume screening and job recommendation platform. Users upload a PDF resume, the system extracts text and skills from the resume, compares the candidate's skills against job descriptions, computes match percentages, and recommends the top 3 most suitable jobs.

## Features
- Upload a PDF resume via a responsive web UI
- Extract clean resume text using `pdfplumber`
- Detect professional skills using keyword matching
- Compare extracted skills with job requirements
- Compute job match scores using `TfidfVectorizer` and cosine similarity
- Recommend the top 3 most relevant job roles
- Display results with extracted skills, missing skills, and match percentage

## Tech Stack
- Backend: Python, Flask
- Machine Learning / NLP: Pandas, NumPy, Scikit-learn, NLTK, PDFPlumber
- Frontend: HTML, CSS, Bootstrap

## Folder Structure
```
AI_Resume_Screening_System/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── recommender.py
├── resumes.csv
├── jobs.csv
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── uploads/
│
└── model/
```

## Installation Steps
1. Clone or download the repository.
2. Navigate to the project directory:
   ```bash
   cd AI_Resume_Screening_System
   ```
3. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS / Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open a browser and go to:
   ```text
   http://127.0.0.1:5000/
   ```
3. Upload a PDF resume and click **Analyze Resume**.

## Expected Outputs
- Home page with a professional resume upload form
- Resume upload should lead to a results page
- Results page will show:
  - Extracted skills from the resume
  - Top 3 recommended jobs
  - Job match percentage for each recommendation
  - Missing skills for each recommended job
  - Parsed resume text preview

## Sample Datasets
- `jobs.csv` contains 20 job roles and required skills
- `resumes.csv` contains 50 sample candidate records

## Deployment Instructions for Render
1. Create a new Web Service in Render.
2. Connect your GitHub repository containing this project.
3. Set the build command:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the start command:
   ```bash
   gunicorn app:app
   ```
5. Ensure the web service is configured to use Python and the correct root directory.
6. Deploy the service.

## Future Scope
- Add OCR support for scanned resumes
- Expand skill extraction with NLP entity recognition
- Add user authentication and resume history
- Enable company-specific job recommendations
- Add a dashboard for analytics and candidate comparison

## Resume Bullet Points
- Built an AI resume screening system using Flask and NLP to extract candidate skills from PDFs.
- Developed a recommendation engine using TF-IDF and cosine similarity to match skills with job requirements.
- Designed a polished Bootstrap web UI for resume upload and candidate-job recommendation display.
- Created sample datasets with 20 job roles and 50 candidate resumes for testing and validation.

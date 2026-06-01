# AI Resume Screening & Job Recommendation System

## Project Overview
This project provides an AI-powered resume screening and job recommendation platform. Users upload a PDF resume, the system extracts text and skills from the resume, compares the candidate's skills against job descriptions, computes match percentages, and recommends the top 3 most suitable jobs.

## Features
- Upload a PDF resume via a responsive web UI
- Extract resume text using pdfplumber
- Detect professional skills using keyword matching
- Compare extracted skills with job requirements
- Compute job match scores using TF-IDF and cosine similarity
- Recommend the top 3 most relevant job roles
- Display extracted skills, missing skills, and match percentages

## Tech Stack
- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- NLTK
- PDFPlumber
- HTML
- CSS
- Bootstrap

## Folder Structure

AI_Resume_Screening_System/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── recommender.py
├── resumes.csv
├── jobs.csv
├── requirements.txt
├── README.md
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── style.css
├── uploads/
└── model/

## Installation

1. Clone the repository

```bash
git clone https://github.com/06naveennavi/AI_Resume_Screening_System.git
```

2. Navigate to the project folder

```bash
cd AI_Resume_Screening_System
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Expected Output

- Resume upload page
- Skill extraction from PDF resumes
- Top 3 recommended jobs
- Match percentage for each job
- Missing skills analysis

## Deployment on Render

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn app:app
```

## Future Enhancements

- OCR support for scanned resumes
- Advanced NLP-based skill extraction
- User authentication
- Resume history tracking
- Recruiter dashboard

## Resume Highlights

- Developed an AI-based resume screening system using Flask and NLP.
- Implemented TF-IDF and cosine similarity for job recommendations.
- Built a responsive web interface for resume analysis.
- Created datasets for testing candidate-job matching accuracy.

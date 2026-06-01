import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_data(job_csv_path='jobs.csv'):
    """Load job roles and skills from the jobs CSV file."""
    return pd.read_csv(job_csv_path)


def build_skill_corpus(resume_skills, job_skills_list):
    """Create the text corpus for TF-IDF vectorization."""
    resume_text = ' '.join(resume_skills)
    return [resume_text] + job_skills_list


def calculate_missing_skills(resume_skills, required_skills):
    """Return skills that are required for a job but missing from the resume."""
    resume_set = set([skill.lower() for skill in resume_skills])
    required_set = set([skill.strip().lower() for skill in required_skills.split(',') if skill.strip()])
    return [skill.title() for skill in required_set.difference(resume_set)]


def recommend_jobs(resume_skills, job_csv_path='jobs.csv', top_n=3):
    """Recommend the top N jobs based on resume skills and job required skills."""
    job_df = load_job_data(job_csv_path)
    job_df['Required Skills'] = job_df['Required Skills'].fillna('')

    # Build corpus for the resume and all job descriptions
    job_skills_list = job_df['Required Skills'].tolist()
    corpus = build_skill_corpus(resume_skills, job_skills_list)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Calculate cosine similarity between resume vector and each job vector
    resume_vector = tfidf_matrix[0:1]
    job_vectors = tfidf_matrix[1:]
    similarity_scores = cosine_similarity(resume_vector, job_vectors).flatten()

    recommendations = []
    for idx, score in enumerate(similarity_scores):
        missing = calculate_missing_skills(resume_skills, job_df.at[idx, 'Required Skills'])
        recommendations.append({
            'job_role': job_df.at[idx, 'Job Role'],
            'match_score': round(float(score) * 100, 2),
            'missing_skills': missing,
            'required_skills': job_df.at[idx, 'Required Skills']
        })

    # Sort jobs by descending similarity score and return the top N
    recommendations = sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
    return recommendations[:top_n]

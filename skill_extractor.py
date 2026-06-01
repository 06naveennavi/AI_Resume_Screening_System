import re
import nltk

# Skill reference list used for matching resumes
SKILL_DATABASE = [
    'Python', 'Java', 'C++', 'SQL', 'Machine Learning', 'Deep Learning',
    'TensorFlow', 'PyTorch', 'Flask', 'Django', 'Power BI', 'Excel',
    'Pandas', 'NumPy', 'NLP', 'Computer Vision', 'Data Science',
    'Statistics', 'Scikit-Learn', 'Git', 'Docker'
]

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def extract_skills(text):
    """Identify skills in resume text using keyword matching."""
    # Tokenize text into words using NLTK for robust NLP processing
    tokens = nltk.word_tokenize(text)
    normalized_text = ' '.join([token.lower() for token in tokens])
    found_skills = set()

    for skill in SKILL_DATABASE:
        # Use a regex with word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, normalized_text):
            found_skills.add(skill)

    return sorted(found_skills)

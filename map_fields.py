"""Map fields from their string to integer representations."""

# Put the abbreviated form of the field and its question number in the Google
# Form here. Will automatically account for the timestamp and email address
# fields in the Google Sheet.
FIELDS = {
    "name": 1,
    "id": 2,
    "grad-year": 3,
    "resume": 4,
    "cover-letter": 5,
    "twitter": 6,
    "linkedin": 7,
    "website": 8,
    "major": 9,
    "second-major": 10,
    "minor": 11,
    "second-minor": 12,
    "academic-update": 13,
    "fav-major-classes": 14,
    "fav-nonmajor-classes": 15,
    "career": 16,
    "academic-interests": 17,
    "personal-interests": 18,
    "strengths": 19,
    "weaknesses": 20,
    "life-update": 21,
    "advisor-questions": 22
}

QUESTIONS = {
    "Timestamp": "latest-timestamp",
    "Email Address": "email",
    "1. What name would you like to be called by?": "name",
    "2. What is your Student ID?": "id",
    "3. What is your Graduation Year?": "grad-year",
    "4. Do you have a resume?": "resume",
    "5. Do you have a cover letter?": "cover-letter",
    "6. Do you have a Professional Twitter? ": "twitter",
    "7. Do you have a LinkedIn URL? ": "linkedin",
    "8. Do you have a professional website?": "website",
    "9. Major": "major",
    "10. Second Major (If Applicable)": "second-major",
    "11. Minor": "minor",
    "12. Second Minor (If Applicable)": "second-minor",
    "13. How are you doing in classes?": "academic-update",
    "14. What are you favorite classes in your major?": "fav-major-classes",
    "15. What are your favorite classes not in your major?": "fav-nonmajor-classes",
    "16. What are some of your career plans or goals?": "career",
    "17. What academic topics are you interested in?": "academic-interests",
    "18. What are some of your personal, non-academic, and extracurricular acitivites? ": "personal-interests",
    "19. What are some of your strengths?": "strengths",
    "20. What are some of your weaknesses?": "weaknesses",
    "21. How's life?": "life-update",
    "22. Any questions for your advisor?": "advisor-questions"
}

REVERSED_FIELDS = {v: k for k, v in FIELDS.items()}


def get_field_int(field_string):
    """Return integer that corresponds to the string for a field."""
    # setting offset to account for first two columns of Google Sheet
    # also considers that first column has an index of 0
    TIMESTAMP_AND_EMAIL_OFFSET = 1
    return FIELDS[field_string] + TIMESTAMP_AND_EMAIL_OFFSET


def get_field_string(field_int):
    """Return string that corresponds to the int for a field."""
    return REVERSED_FIELDS[field_int - 1]


def get_abbreviated_field(question):
    """Return abbreviated field that corresponds to a question."""
    return QUESTIONS[question]

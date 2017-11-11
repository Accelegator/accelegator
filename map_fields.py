"""Map fields from their string to integer representations."""

# Put the abbreviated form of the field and its question number in the Google
# Form here. Will automatically account for the timestamp and email address
# fields in the Google Sheet.
fields = {
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


def get_field_int(field_string):
    """Return integer that corresponds to the string for a field."""
    # setting offset to account for first two columns of Google Sheet
    # also considers that first column has an index of 0
    TIMESTAMP_AND_EMAIL_OFFSET = 1
    return fields[field_string] + TIMESTAMP_AND_EMAIL_OFFSET

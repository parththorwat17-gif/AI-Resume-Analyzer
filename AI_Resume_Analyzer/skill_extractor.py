from job_roles import JOB_ROLES


def extract_skills(text):
    """
    Extract skills from resume text by matching
    against all skills present in JOB_ROLES.
    """

    if not text:
        return []

    text = text.lower()

    # Collect all unique skills
    all_skills = set()

    for skills in JOB_ROLES.values():
        all_skills.update(skills)

    # Find matching skills
    found_skills = []

    for skill in all_skills:
        if skill.lower() in text:
            found_skills.append(skill)

    # Remove duplicates and sort
    found_skills = sorted(list(set(found_skills)))

    return found_skills
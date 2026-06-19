from job_roles import JOB_ROLES

def calculate_score(resume_text, role):

    required_skills = JOB_ROLES.get(role, [])

    matched = []

    for skill in required_skills:

        if skill.lower() in resume_text.lower():
            matched.append(skill)

    score = int(
        (len(matched) / len(required_skills)) * 100
    ) if required_skills else 0

    missing = list(
        set(required_skills) - set(matched)
    )

    return score, matched, missing
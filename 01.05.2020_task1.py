known_answers = {0:0, 1:1, 2:2, 3:4}

def stepPerms(n):
    if n in known_answers.keys():
        return known_answers.get(n)
    result = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
    known_answers[n] = result
    return result
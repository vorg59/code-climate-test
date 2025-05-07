def complex_logic():
    cond_1 = True
    cond_2 = True
    cond_3 = True
    cond_4 = True
    cond_5 = False
    cond_6 = False
    if cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6:
        return 0
    return 1 

def evaluate_student(score1, score2, score3, score4, score5, attendance, behavior, extra_credit):
    if score1 > 50:
        if score2 > 50:
            if score3 > 50:
                if score4 > 50:
                    if score5 > 50:
                        if attendance > 75:
                            if behavior == "good":
                                if extra_credit:
                                    return "Excellent"
                                else:
                                    return "Good"
                            else:
                                return "Needs Improvement"
                        else:
                            return "Low Attendance"
                    else:
                        return "Low Score in Subject 5"
                else:
                    return "Low Score in Subject 4"
            else:
                return "Low Score in Subject 3"
        else:
            return "Low Score in Subject 2"
    else:
        return "Low Score in Subject 1"
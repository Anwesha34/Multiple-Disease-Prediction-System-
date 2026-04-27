def get_heart_suggestions(result):
    if result == 1:
        return [
            "Reduce oily and fatty foods",
            "Walk 30 minutes daily",
            "Avoid smoking and alcohol",
            "Check BP regularly",
            "Consult a doctor immediately"
        ]
    else:
        return [
            "Maintain healthy diet",
            "Exercise regularly",
            "Avoid junk food",
            "Keep monitoring heart health"
        ]


def get_diabetes_suggestions(result):
    if result == 1:
        return [
            "Reduce sugar intake",
            "Eat high-fiber foods",
            "Exercise daily",
            "Monitor blood sugar",
            "Consult doctor for medication"
        ]
    else:
        return [
            "Avoid excess sugar",
            "Maintain healthy weight",
            "Do regular checkups"
        ]
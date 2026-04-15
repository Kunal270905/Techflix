def calculate_score(crime, lighting, traffic, time, is_night):
    safety = (10 - crime) + lighting

    if is_night:
        safety -= crime * 2

    score = (2.5 * safety) - (1.5 * time) - (1.2 * traffic)
    return round(score, 2)


def generate_advice(score, is_night):
    if score > 25:
        return "✅ Highly recommended: safest and efficient route"
    elif score > 10:
        return "⚠️ Balanced route: moderate safety and time"
    else:
        if is_night:
            return "❌ Avoid: unsafe at night"
        return "⚠️ Not recommended under current conditions"
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import calculate_score, generate_advice

app = Flask(__name__)
CORS(app)

def generate_routes():
    return [
        {"name": "Fastest Route", "time": 15, "traffic": 8, "crime": 7, "lighting": 4},
        {"name": "Balanced Route", "time": 20, "traffic": 5, "crime": 5, "lighting": 6},
        {"name": "Safest Route", "time": 25, "traffic": 3, "crime": 2, "lighting": 9}
    ]

@app.route("/api/routes", methods=["POST"])
def get_routes():
    try:
        data = request.json
        source = data.get("source", "")
        destination = data.get("destination", "")
        time_of_day = data.get("time", "day")

        is_night = time_of_day == "night"

        routes = generate_routes()
        results = []

        for r in routes:
            score = calculate_score(
                r["crime"], r["lighting"], r["traffic"], r["time"], is_night
            )

            advice = generate_advice(score, is_night)

            results.append({
                "route": r["name"],
                "time": r["time"],
                "traffic": r["traffic"],
                "safety_score": (10 - r["crime"]) + r["lighting"],
                "final_score": score,
                "advice": advice
            })

        results.sort(key=lambda x: x["final_score"], reverse=True)

        return jsonify({
            "status": "success",
            "best_route": results[0],
            "all_routes": results
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(debug=True)
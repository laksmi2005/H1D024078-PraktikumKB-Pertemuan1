from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ==========================================
# FUZZY LOGIC MANUAL (Pure Python, no scikit-fuzzy)
# ==========================================

def trimf(x, a, b, c):
    """Triangular membership function"""
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

def get_membership(val):
    """Get rendah/sedang/tinggi membership for a 0-100 value"""
    rendah = max(trimf(val, 0, 0, 50), 0)
    sedang = max(trimf(val, 25, 50, 75), 0)
    tinggi = max(trimf(val, 50, 100, 100), 0)
    # Fix edges
    if val <= 0:
        rendah = 1.0
    if val >= 100:
        tinggi = 1.0
    return rendah, sedang, tinggi

def calculate_physical_anxiety(palpitation, insomnia, muscle_tension, digestive):
    p_r, p_s, p_t = get_membership(palpitation)
    i_r, i_s, i_t = get_membership(insomnia)
    m_r, m_s, m_t = get_membership(muscle_tension)
    d_r, d_s, d_t = get_membership(digestive)

    # Fuzzy Rules -> output: aman=15, waspada=50, kritis=85
    rules = [
        # AMAN
        (min(p_r, i_r, m_r, d_r), 15),
        # WASPADA
        (min(max(p_s, i_s), m_r), 50),
        (min(m_s, d_s), 50),
        (min(max(m_t, d_t), 1 - p_t), 50),
        # KRITIS
        (min(max(p_t, i_t), max(m_s, d_s)), 85),
        (min(p_t, i_t, m_t), 85),
        (min(max(p_t, m_t), d_t), 85),
    ]

    # Defuzzification (weighted average)
    numerator = sum(strength * output for strength, output in rules)
    denominator = sum(strength for strength, _ in rules)

    if denominator == 0:
        result_score = 50.0
    else:
        result_score = numerator / denominator

    if result_score < 30:
        status = "Normal / Aman"
        color = "green"
        desc = "Gejala fisik masih dalam batas wajar. Tetap jaga pola hidup sehat."
    elif result_score < 70:
        status = "Waspada (Gejala Sedang)"
        color = "yellow"
        desc = "Tubuh mulai menunjukkan tanda stres berlebih. Disarankan latihan relaksasi pernapasan."
    else:
        status = "Kritis (Gejala Parah)"
        color = "red"
        desc = "Gejala fisik sangat nyata (Psikosomatis). Sangat disarankan berkonsultasi dengan tenaga profesional."

    return {
        "score": round(result_score, 1),
        "status": status,
        "color": color,
        "description": desc
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fuzzy', methods=['POST'])
def api_fuzzy():
    data = request.json
    try:
        res = calculate_physical_anxiety(
            float(data['palpitation']),
            float(data['insomnia']),
            float(data['muscle_tension']),
            float(data['digestive'])
        )
        return jsonify(res)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

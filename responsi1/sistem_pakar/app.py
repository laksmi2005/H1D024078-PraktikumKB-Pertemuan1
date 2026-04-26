from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ==========================================
# 🔍 EXPERT SYSTEM: DIAGNOSA PSIKOLOGIS (CF)
# ==========================================
# Gejala Anxiety dan Bobot Pakarnya (MB - MD disederhanakan ke Weight)
ANXIETY_RULES = {
    "Generalized Anxiety Disorder (GAD)": [
        {"q": "q1", "weight": 0.8}, # Overthinking
        {"q": "q2", "weight": 0.7}, # Gelisah
        {"q": "q3", "weight": 0.6}, # Lelah terus menerus
        {"q": "q4", "weight": 0.8}, # Sulit konsentrasi / pikiran kosong
        {"q": "q5", "weight": 0.6}  # Mudah marah / tersinggung
    ],
    "Panic Disorder": [
        {"q": "q6", "weight": 0.9}, # Sesak/Gemetar tiba-tiba
        {"q": "q7", "weight": 0.8}, # Takut kehilangan kendali
        {"q": "q8", "weight": 0.7}  # Merasa ada bahaya mengancam
    ],
    "Social Anxiety": [
        {"q": "q9", "weight": 0.9}, # Menghindari interaksi sosial
        {"q": "q10", "weight": 0.8} # Takut dihakimi orang
    ]
}

def calculate_psychological_cf(responses):
    final_diagnoses = []
    
    for disorder, symptoms in ANXIETY_RULES.items():
        cf_combine = 0
        is_first = True
        
        for s in symptoms:
            # User input from 0 (Tidak Pernah) to 1 (Sangat Sering)
            cf_user = float(responses.get(s["q"], 0)) 
            cf_rule = cf_user * s["weight"]
            
            if is_first:
                cf_combine = cf_rule
                is_first = False
            else:
                cf_combine = cf_combine + cf_rule * (1 - cf_combine)
        
        if cf_combine > 0.1: # Minimal threshold
            final_diagnoses.append({
                "disorder": disorder,
                "confidence": round(cf_combine * 100, 1),
                "severity": "Tinggi" if cf_combine > 0.7 else "Sedang" if cf_combine > 0.4 else "Rendah"
            })
            
    return sorted(final_diagnoses, key=lambda x: x['confidence'], reverse=True)

# --- FLASK ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/audit', methods=['POST'])
def api_audit():
    data = request.json
    try:
        res = calculate_psychological_cf(data.get('responses', {}))
        return jsonify(res)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)

import re
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def format_million(value):
    return f"{value / 1_000_000:.2f}M"  # Keeps two decimal places

def process_data(data):
    values = {}
    total = 0
    
    # Extract key-value pairs using regex
    matches = re.findall(r'(\w+)=([0-9]+)', data)
    for key, value in matches:
        value = int(value)
        values[key] = value
        if key in ["IMSIs", "DNs", "IMEIs"]:
            total += value
    
    # Format individual values
    imsi_million = format_million(values.get("IMSIs", 0))
    dn_million = format_million(values.get("DNs", 0))
    imei_million = format_million(values.get("IMEIs", 0))
    total_million = format_million(total)
    
    # Output result
    output = {
        "IMSI": imsi_million,
        "DN": dn_million,
        "IMEI": imei_million,
        "Total": total_million,
        "Calculation": f"{values.get('IMSIs', 0)} + {values.get('DNs', 0)} + {values.get('IMEIs', 0)} = {total} = {total_million}"
    }
    
    return output

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_request():
    data = request.json.get("data", "")
    result = process_data(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

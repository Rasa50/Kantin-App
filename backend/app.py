import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ambil dari Environment Variable (Identity Injection)
nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Nama Mahasiswa')
nim_owner = os.environ.get('NIM_PRAKTIKAN', '0000000')

kantin_data = {
    "nama_kantin": f"Kantin milik {nama_owner}",
    "pemilik": nama_owner,
    "nim": nim_owner,
    "menu": ["Nasi Goreng", "Es Teh", "Gorengan"]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(kantin_data)

@app.route('/api/add-menu', methods=['POST'])
def add_menu():
    new_item = request.json.get('item')
    if new_item:
        kantin_data["menu"].append(new_item)
        return jsonify({"message": "Menu berhasil ditambah!"}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
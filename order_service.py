from flask import Flask, jsonify, request  #[cite: 1]
import requests  #[cite: 1]

app = Flask(__name__)  #[cite: 1]
orders = []  #[cite: 1]
BOOK_SERVICE_URL = 'http://localhost:5001'  # Alamat Book Service[cite: 1]


# BUAT PESANAN (POST) - EDIT & MANIPULASI DI POSTMAN[cite: 1]
@app.route('/orders', methods=['POST'])  #[cite: 1]
def create_order():
  data = request.get_json()  #[cite: 1]
  book_id = data.get('book_id')  #[cite: 1]

  try:
    # Order Service menembak HTTP Request ke Book Service (Port 5001)[cite: 1]
    response = requests.get(f'{BOOK_SERVICE_URL}/books/{book_id}')  #[cite: 1]

    if response.status_code == 200:  #[cite: 1]
      book_data = response.json()  #[cite: 1]
      if book_data['stock'] > 0:  #[cite: 1]
        order = {  #[cite: 1]
            'id': len(orders) + 1,  #[cite: 1]
            'book_id': book_id,  #[cite: 1]
            'status': 'berhasil',  #[cite: 1]
        }  #[cite: 1]
        orders.append(order)  #[cite: 1]
        return jsonify(order), 201  #[cite: 1]

    return jsonify({'error': 'Buku tidak tersedia'}), 400  #[cite: 1]

  # Menangani jika Book Service di Port 5001 Mati[cite: 1]
  except requests.exceptions.ConnectionError:  #[cite: 1]
    return (
        jsonify({'error': 'Book Service sedang down!'}),
        500,
    )  #[cite: 1]


if __name__ == '__main__':
  # Berjalan di Port 5002[cite: 1]
  app.run(port=5002, debug=True)  #[cite: 1]
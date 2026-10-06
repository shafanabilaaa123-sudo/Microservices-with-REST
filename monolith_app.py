from flask import Flask, jsonify, request  #[cite: 1]

app = Flask(__name__)  #[cite: 1]

# Database simulasi (In-memory)[cite: 1]
books = [{"id": 1, "title": "Belajar Flask", "stock": 5}]  #[cite: 1]
orders = []  #[cite: 1]


# 1. LIHAT SEMUA BUKU (GET) - BISA DI BROWSER / POSTMAN[cite: 1]
@app.route('/books', methods=['GET'])  #[cite: 1]
def get_books():
  return jsonify(books)  #[cite: 1]


# 2. TAMBAH BUKU BARU (POST) - EDIT & MANIPULASI DI POSTMAN
@app.route('/books', methods=['POST'])
def add_book():
  data = request.get_json()  # Ambil data JSON dari Postman

  # Validasi sederhana
  if not data or 'title' not in data or 'stock' not in data:
    return jsonify({'error': 'Judul (title) dan stok (stock) harus diisi!'}), 400

  new_book = {
      'id': len(books) + 1,
      'title': data.get('title'),
      'stock': int(data.get('stock')),
  }

  books.append(new_book)  # Masukkan buku baru ke array 'books'
  return jsonify(new_book), 201  # HTTP 201 Created


# 3. BUAT PESANAN (POST) - EDIT & MANIPULASI DI POSTMAN[cite: 1]
@app.route('/orders', methods=['POST'])  #[cite: 1]
def create_order():
  data = request.get_json()  #[cite: 1]
  book_id = data.get('book_id')  #[cite: 1]

  for b in books:  #[cite: 1]
    if b['id'] == book_id and b['stock'] > 0:  #[cite: 1]
      b['stock'] -= 1  # Kurangi stok[cite: 1]
      order = {  #[cite: 1]
          'id': len(orders) + 1,  #[cite: 1]
          'book_id': book_id,  #[cite: 1]
          'status': 'berhasil',  #[cite: 1]
      }  #[cite: 1]
      orders.append(order)  #[cite: 1]
      return jsonify(order), 201  #[cite: 1]

  return jsonify({'error': 'Buku tidak ditemukan atau stok habis'}), 400  #[cite: 1]


if __name__ == '__main__':
  # Berjalan di Port 5000[cite: 1]
  app.run(port=5000, debug=True)  #[cite: 1]
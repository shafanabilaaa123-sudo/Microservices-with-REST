from flask import Flask, jsonify, request  #[cite: 1]

app = Flask(__name__)  #[cite: 1]

# Database khusus Book Service[cite: 1]
books = [{"id": 1, "title": "Belajar Flask", "stock": 5}]  #[cite: 1]


# 1. LIHAT SEMUA BUKU (GET) - BISA DI BROWSER / POSTMAN[cite: 1]
@app.route('/books', methods=['GET'])  #[cite: 1]
def get_books():
  return jsonify(books)  #[cite: 1]


# 2. LIHAT SATU BUKU SPESIFIK BERDASARKAN ID (GET)[cite: 1]
@app.route('/books/<int:book_id>', methods=['GET'])  #[cite: 1]
def get_book(book_id):
  for b in books:  #[cite: 1]
    if b['id'] == book_id:  #[cite: 1]
      return jsonify(b)  #[cite: 1]
  return jsonify({'error': 'Not found'}), 404  #[cite: 1]


# 3. TAMBAH BUKU BARU (POST) - EDIT & MANIPULASI DI POSTMAN
@app.route('/books', methods=['POST'])
def add_book():
  data = request.get_json()

  if not data or 'title' not in data or 'stock' not in data:
    return jsonify({'error': 'Judul (title) dan stok (stock) harus diisi!'}), 400

  new_book = {
      'id': len(books) + 1,
      'title': data.get('title'),
      'stock': int(data.get('stock')),
  }

  books.append(new_book)
  return jsonify(new_book), 201


if __name__ == '__main__':
  # Berjalan di Port 5001[cite: 1]
  app.run(port=5001, debug=True)  #[cite: 1]
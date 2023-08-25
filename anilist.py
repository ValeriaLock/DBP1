from flask import Flask, request, jsonify

app = Flask(__name__)

animes = [
    {"id": 1, 
     "titulo": "One Piece",
     "puntaje": 8,
     "tipo": "Serie",
     "season": "Fall 1999",
     "generos": ["Action", "Adventure", "Comedy", "Drama", "Fantasy"]},

    {"id": 2,
     "titulo": "Seija Musou",
     "puntaje": 6,
     "tipo": "Serie",
     "season": "Summer 2023",
     "generos": ["Adventure", "Comedy", "Fantasy"]},

     {"id": 3,
     "titulo": "Watashi no Shiawase na Kekkon",
     "puntaje": 8,
     "tipo": "Serie",
     "season": "Summer 2023",
     "generos": ["Drama", "Romance", "Supernatural"]},

    {"id": 4,
     "titulo": "Hanma Baki",
     "puntaje": 7,
     "tipo": "Serie",
     "season": "Summer 2023",
     "generos": ["Action", "Sports"]},

     {"id": 5,
     "titulo": "Rurouni Kenshin",
     "puntaje": 7,
     "tipo": "Serie",
     "season": "Summer 2023",
     "generos": ["Action", "Adventure", "Drama", "Romance"]}
]

# Ruta para obtener todos los animes
@app.route('/animes', methods=['GET'])
def get_animes():
    return jsonify(animes)

# Ruta para obtener un anime por su ID
@app.route('/animes/<int:id>', methods=['GET'])
def get_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime is None:
        return jsonify({"error": "Anime not found"}), 404
    return jsonify(anime)

# Ruta para agregar un nuevo anime
@app.route('/animes', methods=['POST'])
def add_anime():
    new_anime = request.json
    new_anime['id'] = len(animes) + 1
    animes.append(new_anime)
    return jsonify({"message": "Anime added successfully", "anime": new_anime}), 201

# Ruta para actualizar un anime por su ID
@app.route('/animes/<int:id>', methods=['PUT'])
def update_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime is None:
        return jsonify({"error": "Anime not found"}), 404
    updated_data = request.json
    anime.update(updated_data)
    return jsonify({"message": "Anime updated successfully", "anime": anime})

# Ruta para actualizar parcialmente un anime por su ID
@app.route('/animes/<int:id>', methods=['PATCH'])
def patch_anime(id):
    anime = next((anime for anime in animes if anime['id'] == id), None)
    if anime is None:
        return jsonify({"error": "Anime not found"}), 404
    updated_data = request.json
    anime.update(updated_data)
    return jsonify({"message": "Anime updated successfully", "anime": anime})

# Ruta para eliminar un anime por su ID
@app.route('/animes/<int:id>', methods=['DELETE'])
def delete_anime(id):
    global animes
    animes = [anime for anime in animes if anime['id'] != id]
    return jsonify({"message": "Anime deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, send_file, render_template, session
#dev
#from app.repository.repository_streaming import UsuarioRepository, ContentRepository, SuscripcionRepository

#prod
from repository.repository_streaming import UsuarioRepository, ContentRepository, SuscripcionRepository
import os
import socket


class StreamingService:
    ALLOWED_EXTENSIONS = {'mp3', 'mp4', 'txt', 'jpg', 'png'}
    UPLOAD_FOLDER = 'archivos'

    @staticmethod
    def obtener_mensaje():
        return f"Container ID: {socket.gethostname()}"

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in StreamingService.ALLOWED_EXTENSIONS

    @staticmethod
    def subir_archivo_al_servidor():
        
        print(request.files)
        if 'file' not in request.files:
            return jsonify({"error": "No file part"})
        
        archivo = request.files['file']
        print("here?")
        print("archivo?" + str(archivo))
        if archivo.filename == '':
            print(archivo.filename)
            return jsonify({"error": "No selected file"})

        if archivo and StreamingService.allowed_file(archivo.filename):
            filename = os.path.join(StreamingService.UPLOAD_FOLDER, archivo.filename)
            print(filename)

            # Separar el archivo en chunks y simular la carga
            chunk_size = 1024*500  # Tamaño del chunk en bytes
            total_chunks = (len(archivo.read()) + chunk_size - 1) // chunk_size
            print(total_chunks)
            archivo.seek(0)  # Reiniciar el puntero del archivo

            with open(filename, 'wb') as dest_file:
                for i in range(total_chunks):
                     
                    chunk_data = archivo.read(chunk_size)
                    dest_file.write(chunk_data) 
                    progress_percentage = (i + 1) / total_chunks * 100
                    print(progress_percentage)
       
            return jsonify({'mensaje': 'Archivo subido exitosamente', 'filename': filename})
        else:
            return jsonify({"error": "Invalid file format. Allowed formats: mp3, mp4, txt, png"})

    @staticmethod
    def obtener_archivos():
        archivos = [arch for arch in os.listdir(StreamingService.UPLOAD_FOLDER) if
                    os.path.isfile(os.path.join(StreamingService.UPLOAD_FOLDER, arch)) and
                    StreamingService.allowed_file(arch)]
        return jsonify({'archivos': archivos})

    @staticmethod
    def obtener_archivo(nombre_archivo):
        archivo_path = os.path.join(StreamingService.UPLOAD_FOLDER, nombre_archivo)
        if StreamingService.allowed_file(nombre_archivo) and os.path.isfile(archivo_path):
            return send_file(archivo_path)
        else:
            return jsonify({"error": "Invalid file format or file not found. Allowed formats: mp3, mp4, txt"})

    @staticmethod
    def subir_archivo_al_servidor_get():
        catalogo = ContentRepository.obtener_catalogo()

        return render_template('subir_archivo_al_servidor.html', catalogo=catalogo)

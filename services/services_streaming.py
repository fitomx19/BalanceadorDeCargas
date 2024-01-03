from flask import Flask, request, jsonify, send_file, render_template, session,send_from_directory
from google.cloud import storage

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
            if 'file' not in request.files:
                return jsonify({"error": "No se ha enviado ningún archivo"})

            archivo = request.files['file']

            if archivo.filename == '':
                return jsonify({"error": "No se ha seleccionado ningún archivo"})

            if archivo and StreamingService.allowed_file(archivo.filename):
                filename = os.path.join(StreamingService.UPLOAD_FOLDER, archivo.filename)

                tipo_subida = request.form.get('tipoSubida')  # Obtener el tipo de subida desde el formulario
                if tipo_subida == '1':
                    # Subir archivo localmente
                    archivo.save(filename)
                elif tipo_subida == '2':
                    # Subir archivo a Google Cloud Storage
                    client = storage.Client()
                    bucket_name = "nombre_de_tu_bucket"
                    bucket = client.get_bucket(bucket_name)
                    blob = bucket.blob(archivo.filename)
                    blob.upload_from_file(archivo)
                else:
                    return jsonify({"error": "Opción de subida no válida"})

                file_to_modify = request.form.get('fileToModify')
                print(f"Nombre de la película: {file_to_modify}")

                return jsonify({'mensaje': 'Archivo subido exitosamente', 'filename': filename})
            else:
                return jsonify({"error": "Formato de archivo no válido. Formatos permitidos: mp3, mp4, txt, png"})


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

 
    @staticmethod
    def download(filename):
        file_path = os.path.join('static/peliculas/', filename)

        # Verificar si hay un encabezado de rango en la solicitud
        range_header = request.headers.get('Range', None)

        if range_header:
            # Devolver la porción del archivo según el rango
            return send_file(file_path, mimetype='video/mp4', as_attachment=True, download_name=filename, conditional=True)

        # Si no hay encabezado de rango, simplemente devolver el archivo completo
        return send_file(file_path, mimetype='video/mp4', as_attachment=True, download_name=filename, conditional=True)

from app import app
import base64
from flask import flash, json, render_template, request, Response, send_from_directory
import os
from werkzeug.utils import secure_filename

# Directory-related variables
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, "tmp_json")

TEMP_JSON_NAME = "json_encoded.json"
TEMP_JSON_FILE = os.path.join(DATA_FOLDER, TEMP_JSON_NAME)

# If Data folder doesn't exist, mkdir it.
if not os.path.isdir(DATA_FOLDER):
    os.mkdir(DATA_FOLDER)

# if Data folder has old temporary json files, remove it
if os.listdir(DATA_FOLDER):
    for entry in os.listdir(DATA_FOLDER):
        if entry != "__init__.py":
            os.remove(os.path.join(DATA_FOLDER, entry))


def encode_this_file(file):
    encoded_pdf = base64.b64encode(file.read())
    return encoded_pdf


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("upload_file.html")
    elif request.method == "POST":
        if request.form["main"] == "Submit":
            if "files[]" not in request.files:
                flash("No file part")
                return redirect(request.url)
            files = request.files.getlist("files[]")
            encoded_files = {}
            for file in files:
                filename = secure_filename(file.filename)
                filename = "." in filename and filename.rsplit(".", 1)[0]
                encoded_file = encode_this_file(file)
                encoded_files[filename] = str(encoded_file.decode("ascii"))

        with open(TEMP_JSON_FILE, "w") as output_json:
            json.dump(encoded_files, output_json)

        file_download = send_from_directory(
            DATA_FOLDER, TEMP_JSON_NAME, as_attachment=True
        )
        return file_download


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

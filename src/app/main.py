from app import app
import base64
from flask import jsonify, render_template, request
from werkzeug.utils import secure_filename


def encode_pdf(file):
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
            for file in files:
                filename = secure_filename(file.filename)
                encoded_file = encode_pdf(file)
                json_file = jsonify({filename: encode_pdf})
        flash("Encoded file")
        print(json_file)
        return render_template("upload_file.html")
        # return Response(
        #     json_file,
        #     mimetype="application/json",
        #     headers={"Content-Disposition": "attachment;filename=zones.geojson"},
        # )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

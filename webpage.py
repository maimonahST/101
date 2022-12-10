from flask import Flask, render_template,request
from PIL import Image
import os
import base64
import io
from Preduct import preduct

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Display_IMG", methods = ['GET', 'POST'])
def Display_IMG():
    if request.method == 'GET':
        name = request.args.get('uploaded-file')
        Flask_Img = os.path.join("templates/Test", str(name))

        im = Image.open(Flask_Img).resize((300,300))
        data = io.BytesIO()
        im.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        

        cls , score = preduct(Flask_Img)
        return render_template("results-1.html", img_data=encoded_img_data.decode('utf-8'), score = score , cls = cls )


if __name__=='__main__':
    app.run(debug=True)
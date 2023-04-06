from flask import Flask, request, make_response, render_template
from PyPDF2 import PdfReader, PdfMerger
import io
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    pdf_files = request.files.getlist('pdf')
    merger = PdfMerger()
    for pdf in pdf_files:
        if pdf and allowed_file(pdf.filename):
            merger.append(PdfReader(pdf))
        else:
            return "Invalid file type. Only PDF files are allowed."
    output = io.BytesIO()
    merger.write(output)
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=merged.pdf'
    response.mimetype = 'application/pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
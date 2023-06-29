from flask import render_template, request, Blueprint
from flaskblog.config import Config



main = Blueprint('main', __name__)


@main.route("/")
def landing():
    return render_template('home.html')

@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/concepts")
def concepts():
    return render_template('concepts.html', title='Concepts')

@main.route("/disclaimer")
def disclaimer():
    return render_template('disclaimer.html', title='Disclaimer')

@main.route("/tools/")
def tools():
    return render_template('tools.html', title='Tools')

@main.route("/ideafactory/")
def ideafactory():
    return render_template('ideafactory.html', title='Ideafactory')

@main.route("/portfolios")
def portfolios():
    return render_template('portfolios.html', title='Portfolios')

@main.route("/dashboard")
#@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
    

@main.route("/concepts/keepitreal")
def keepitreal():
    return render_template('keepitreal.html', title='Keep it real!')





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

# @main.route('/upload', methods=['GET', 'POST'])
# @login_required
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         # if 'files[]' not in request.files:
#         #     flash('No file part')
#         #     return redirect(request.url)
#         files = request.files.getlist('files[]')
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         for file in files:
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(Config.UPLOAD_FOLDER, filename))

#         flash('File(s) successfully uploaded')
#         return redirect('/')
#     return '''
#     <!doctype html>
#     <title>Upload new Files</title>
#     <h2>Upload new Files</h2>
#     <form method=post enctype=multipart/form-data >
#       <input type="file" multiple name="files[]" />
#       <input type=submit value=Upload>
#     </form>
#     '''

# from flask import send_from_directory

# @main.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(Config.UPLOAD_FOLDER,
#                                filename)
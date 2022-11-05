from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from script import process_file
import os

ALLOWED_EXTENSIONS={'pdf'}
def allowed_file(filename):
    #function to extract the file extension and check if its pdf
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app=Flask(__name__)

    @app.route('/',methods=['GET'])
    def home():
        if request.method=='GET':
            return render_template('hello.html')
    
    @app.route('/upload',methods=['GET','POST'])
    def upload():
        if request.method=='POST':
            file=request.files['file']
            if(file and allowed_file(file.filename)):
                #if the provided file is pdf
                #secre_filename will format the filename properly,i.e removing paths or /s
                filename=secure_filename(file.filename)
                #saving the uploaded file
                save_file=os.path.join('uploads',filename)
                file.save(save_file)
    
                #processing the uploaded file
                angle=request.form['angle']
                page_no=request.form['page_no']
                if(angle and page_no):
                    process_file(filename,angle,page_no)
                    processed_filename=filename[:-4]+'_modified'
                    return render_template('download.html')
                
                #incase rotation angle and page number is not provided
                return 'Pdf Uploaded Successfully'

        return render_template('upload.html')
        
    return app
from flask import Flask, render_template, Response,request, send_from_directory, send_file
import sqlite3
from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import textwrap
import fpdf
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import io
import os
from docx import Document
import textract
import pdfplumber
import sqlite3
from fpdf import FPDF
import PyPDF2
import random


nltk.download('stopwords')
nltk.download('punkt')


app=Flask(__name__)

database="class.db"

def createtable():
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("create table if not exists studentreg(id integer primary key autoincrement,regno text, section text, studentname text,password text)")
    cursor.execute("create table if not exists query(id integer primary key autoincrement,regno text, section text, studentname text,student text,staff text,status int)")

    cursor.execute("create table if not exists feedback(id integer primary key autoincrement,regno text, section text, studentname text,feedback text)")
    cursor.execute("create table if not exists staff(id integer primary key autoincrement, StaffId text, Section text, StaffName text, password text)")
    cursor.execute("create table if not exists assignment(id integer primary key autoincrement,regno text,section ,name text, assignment blob)")
    conn.commit()
    conn.close()
createtable()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
a=[]
@app.route('/register', methods=["GET","POST"])
def register():
    
    if request.method=="POST":
        regno=request.form['regno']
        sec=request.form['sec']
        studentname=request.form['studentname']
        password=request.form['password']
        conn=sqlite3.connect(database)
        cursor=conn.cursor()
        cursor.execute(" SELECT regno FROM studentreg WHERE regno=?",(regno,))
        registered=cursor.fetchall()
        if registered:
            return render_template('index.html',show_alert1=True)
        else:
            cursor.execute("insert into studentreg(regno,section, studentname,password) values(?,?,?,?)",(regno,sec,studentname,password))
            conn.commit()
            return render_template('index.html', show_alert2=True)
    return render_template('index.html')
a=[]
sname=[]
Sid=[]
sec=[]
@app.route('/login', methods=["GET","POST"])
def login():
    global regno
    if request.method == "POST":
        regno=request.form['regno']
        password=request.form['password']
        conn=sqlite3.connect(database)
        cursor=conn.cursor()
        cursor.execute("select * from studentreg where regno=? AND password=?",(regno,password))
        data=cursor.fetchone()
        
        print(a)
        if data is None:
            return render_template('index.html', show_alert4=True)
        else:
            a.append(data[2])
            sname.append(data[3])
            Sid.append(data[1])
            sec.append(data[2])
            conn=sqlite3.connect(database)
            cursor=conn.cursor()
            cursor.execute("select * from studentreg where regno=?",(regno,))
            results=cursor.fetchone()
            conn.commit()
            return render_template('upload_ass.html')
    return render_template('login.html')





@app.route('/convert', methods=["GET","POST"])
def convert():
    if request.method == "POST":
        msg=request.form['msg']
        print(msg)
        lang=int(request.form['lang'])
        print(lang)
        if lang == 0 :
           translator = Translator()
           output = translator.translate(msg, dest='ta').text
        elif lang == 1:
            translator = Translator()
            output = translator.translate(msg, dest='en').text
        elif lang == 2:
            translator = Translator()
            output = translator.translate(msg, dest='te').text
        elif lang == 3:
            translator = Translator()
            output = translator.translate(msg, dest='kn').text
        elif lang == 4:
            translator = Translator()
            output = translator.translate(msg, dest='ml').text
        elif lang == 5:
            translator = Translator()
            output = translator.translate(msg, dest='hi').text
        elif lang == 6:
            translator = Translator()
            output = translator.translate(msg, dest='af').text
        elif lang == 7:
            translator = Translator()
            output = translator.translate(msg, dest='sq').text
        elif lang == 8:
            translator = Translator()
            output = translator.translate(msg, dest='ar').text
        elif lang == 9:
            translator = Translator()
            output = translator.translate(msg, dest='hy').text
        elif lang == 10:
            translator = Translator()
            output = translator.translate(msg, dest='az').text
        elif lang == 11:
            translator = Translator()
            output = translator.translate(msg, dest='eu').text
        elif lang == 12:
            translator = Translator()
            output = translator.translate(msg, dest='be').text
        elif lang == 13:
            translator = Translator()
            output = translator.translate(msg, dest='bn').text
        elif lang == 14:
            translator = Translator()
            output = translator.translate(msg, dest='bs').text
        elif lang == 15:
            translator = Translator()
            output = translator.translate(msg, dest='bg').text
        elif lang == 16:
            translator = Translator()
            output = translator.translate(msg, dest='ca').text
        elif lang == 17:
            translator = Translator()
            output = translator.translate(msg, dest='ceb').text
        elif lang == 18:
            translator = Translator()
            output = translator.translate(msg, dest='zh-CN').text
        elif lang == 19:
            translator = Translator()
            output = translator.translate(msg, dest='co').text
        elif lang == 20:
            translator = Translator()
            output = translator.translate(msg, dest='hr').text
        elif lang == 21:
            translator = Translator()
            output = translator.translate(msg, dest='cs').text
        elif lang == 22:
            translator = Translator()
            output = translator.translate(msg, dest='da').text
        elif lang == 23:
            translator = Translator()
            output = translator.translate(msg, dest='nl').text
        elif lang == 24:
            translator = Translator()
            output = translator.translate(msg, dest='eo').text
            
        elif lang == 25:
            translator = Translator()
            output = translator.translate(msg, dest='et').text
        elif lang == 26:
            translator = Translator()
            output = translator.translate(msg, dest='fi').text
        elif lang == 27:
            translator = Translator()
            output = translator.translate(msg, dest='fr').text
        elif lang == 28:
            translator = Translator()
            output = translator.translate(msg, dest='fy').text
        elif lang == 29:
            translator = Translator()
            hindi = translator.translate(msg, dest='gl').text
        elif lang == 30:
            translator = Translator()
            output = translator.translate(msg, dest='ka').text
        elif lang == 31:
            translator = Translator()
            output = translator.translate(msg, dest='de').text
        elif lang == 32:
            translator = Translator()
            output = translator.translate(msg, dest='el').text
        elif lang == 33:
            translator = Translator()
            output = translator.translate(msg, dest='gu').text
        elif lang == 34:
            translator = Translator()
            output = translator.translate(msg, dest='ht').text
        elif lang == 35:
            translator = Translator()
            output = translator.translate(msg, dest='ha').text
        elif lang == 36:
            translator = Translator()
            hindi = translator.translate(msg, dest='haw').text
        elif lang == 37:
            translator = Translator()
            output = translator.translate(msg, dest='he').text
        elif lang == 38:
            translator = Translator()
            output = translator.translate(msg, dest='hmn').text
        elif lang == 39:
            translator = Translator()
            output = translator.translate(msg, dest='hu').text
        elif lang == 40:
            translator = Translator()
            output = translator.translate(msg, dest='is').text
        #print(output)
        return render_template('upload_ass.html' , output=output)



        
        
    return render_template('studentview.html')

@app.route('/assignment', methods=["GET","POST"])
def assignment():
    return render_template('assignment.html')




@app.route('/studentview', methods=["GET","POST"])
def studentview():
    return render_template('studentview.html')


@app.route('/upload_ass', methods=["GET","POST"])
def upload_ass():
    return render_template('upload_ass.html')

@app.route('/staffview', methods=["GET","POST"])
def staffview():
    return render_template('staffview.html')

def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return render_template('studentview.html',show_alert3=True)
    else:
        return None


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)

@app.route('/result', methods=["GET","POST"])
def result():
   if request.method == 'POST':
            file = request.files['text']
            if file.filename == '':
                return 'No selected file'

            file_path = 'static/videos/' + file.filename
            file.save(file_path)

            # Check the file extension
            file_ext = os.path.splitext(file_path)[1].lower()

            if file_ext == '.pdf':
                with open(file_path, 'rb') as pdf_file:
                    pdf_content = pdf_file.read()
                    text = extract_text_from_pdf(pdf_content)
               
            elif file_ext == '.txt':
                # Read text directly from text file
                with open(file_path, 'r') as file:
                    text = file.read()
                #print(text)

            elif file_ext == '.docx':
                # Extract text from Word document
                text = extract_text_from_docx(file_path)
                #print(text)
            #print("original Text \n",text)
            stopWords = set(stopwords.words("english"))
            words = word_tokenize(text)      
         
              
            freqTable = dict()
            for word in words:
               word = word.lower()
               if word in stopWords:
                   continue
               if word in freqTable:
                   freqTable[word] += 1
               else:
                   freqTable[word] = 1
              
            sentences = sent_tokenize(text)
            sentenceValue = dict()
              
            for sentence in sentences:
               for word, freq in freqTable.items():
                   if word in sentence.lower():
                       if sentence in sentenceValue:
                           sentenceValue[sentence] += freq
                       else:
                           sentenceValue[sentence] = freq
              
              
              
            sumValues = 0
            for sentence in sentenceValue:
               sumValues += sentenceValue[sentence]          
              
            average = int(sumValues / len(sentenceValue))          
            summary = ''
            for sentence in sentences:
               if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                   summary += " " + sentence
            print("summarized text \n",summary)
              
            wrapper = textwrap.TextWrapper(width=80)
          
            word_list=wrapper.fill(text=summary)
          
            summary=word_list
            ques = summary.encode('latin-1', 'replace').decode('latin-1')
            pdf = fpdf.FPDF(format='letter')
            pdf.add_page()
            pdf.set_font("Arial", size=30)
            pdf.write(30,"                    Summarized Text")
            pdf.ln()
            pdf.set_font("Arial", size=12)


            for i in ques:
              pdf.write(10,str(i))
            #pdf_content = pdf.output(dest='S').encode('latin1')
            file_id = ''.join(random.choices('0123456789', k=4))

            output_pdf_path = f'static/{file_id}.pdf'

            pdf.output(output_pdf_path)

            conn=sqlite3.connect(database)
            cursor=conn.cursor()
            cursor.execute(" SELECT * FROM studentreg WHERE regno=?",(regno,))
            data=cursor.fetchone()
            print(data)
            cursor.execute("insert into assignment(regno,section,name,assignment) values(?,?,?,?)",(data[1],a[-1],data[3],file_id,))
            conn.commit()
            return render_template('studentview.html',show_alert3=True)

@app.route('/service',methods=["GET","POST"])
def service():
    if request.method=='POST':
        StaffId=request.form['StaffId']
        Section=request.form['Section']
        StaffName=request.form['StaffName']
        password=request.form['password']
        conn=sqlite3.connect(database)
        cursor=conn.cursor()
        cursor.execute("SELECT StaffId from staff WHERE StaffId=?",(StaffId,))
        registered=cursor.fetchall()
        if registered:
            return render_template('index.html',show_alert3=True)
        else:
            cursor.execute("INSERT INTO staff(StaffId,Section,StaffName,password) VALUES (?,?,?,?)",(StaffId,Section,StaffName,password))
            conn.commit()
            return render_template('index.html',show_alert2=True)

def extract_text_from_pdf(pdf_content):
    pdf_file = io.BytesIO(pdf_content)
    reader = PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text


staf_sec=[]
@app.route('/service_login', methods=["GET","POST"])
def service_login():
    if request.method == "POST":
        StaffId=request.form['StaffId']
        password=request.form['password']
        conn=sqlite3.connect(database)
        cursor=conn.cursor()
        cursor.execute("select * from staff where StaffId=? AND password=?",(StaffId,password))
        data=cursor.fetchone()
        if data is None:
            return render_template('index.html', show_alert4=True)
         
        
        else:
            staf_sec.append(data[2])
            cursor.execute("select * from assignment where section=?",(data[2],))
            assignments=cursor.fetchall()
            return render_template('staffview.html',data=assignments)



@app.route('/select_complaint', methods=['POST'])
def select_complaint():
    complaint_number = request.form['complaint_number']
    print(complaint_number)
    return render_template('pdfview.html',new=complaint_number)


@app.route('/query', methods=['POST'])
def query():
    query=request.form["query"]
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("select * from query where regno=?",(Sid[-1],))
    data=cursor.fetchall()
    if data:
        cursor.execute("update query set  student=? ,status =? where regno=? ",(query,1,Sid[-1]))
        conn.commit()
    else:
        cursor.execute("insert into query(regno,section, studentname,student,status) values(?,?,?,?,?)",(Sid[-1],sec[-1],sname[-1],query,1))
        conn.commit()
    return render_template('studentview.html', show_alert1=True)   
    
    

@app.route('/feedback', methods=['POST'])
def feedback():
    query=request.form["feedback"]
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("select * from feedback where regno=?",(Sid[-1],))
    data=cursor.fetchall()
    if data:
        cursor.execute("update feedback set  feedback=? where regno=?",(query,Sid[-1]))
        conn.commit()
    else:
        cursor.execute("insert into feedback(regno,section, studentname,feedback) values(?,?,?,?)",(Sid[-1],sec[-1],sname[-1],query))
        conn.commit()
    return render_template('studentview.html', show_alert2=True)   
    

@app.route('/view_feedback')
def view_feedback():
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("select * from feedback where section=? ",(staf_sec[-1],))
    data=cursor.fetchall()
    return render_template('view_feedback.html',data=data)

@app.route('/view_query')
def view_query():
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("select * from query  where section= ? and status=?",(staf_sec[-1],1))
    data=cursor.fetchall()
    return render_template('view_query.html',data=data)
       
reply1=[]
@app.route('/select_reply', methods=['POST'])
def select_reply():
    reply=request.form["reply"]
    reply1.append(reply)
    return render_template('staffreply.html')

    

@app.route('/staffreply', methods=['POST'])
def staffreply():
    query=request.form["query"]
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("update query set  staff=?,status=? where id=?",(query,2,reply1[-1]))
    conn.commit()
    return render_template('staffview.html',show_alert2=True)



@app.route('/answers')
def answers():
    conn=sqlite3.connect(database)
    cursor=conn.cursor()
    cursor.execute("select * from query  where regno=? and status=?",(Sid[-1],2))
    data=cursor.fetchall()
    print(data)
    return render_template('notification.html',data=data)


if __name__ == "__main__":
    app.run(port=800)

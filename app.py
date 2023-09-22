#import library
import sklearn
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from model import load, prediksi_data

#flask dir
app = Flask(__name__)

#connect database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'telekom'
mysql = MySQL(app)

# load model dan scaler
load()

#fungsi menampilkan card Yes
def cardviewyes():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM pelanggan WHERE churn="Yes" ''') #perintah sql menampilkan pelanggan churn Yes
    countyes = str(cursor.rowcount)
    return countyes

#fungsi menampilkan card No
def cardviewno():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM pelanggan WHERE churn="No" ''') #perintah sql menampilkan pelanggan churn No
    cardviewno = str(cursor.rowcount)
    return cardviewno

#route index page
@app.route('/')
def home():
    countyes = cardviewyes()
    countno = cardviewno()
    return render_template('index.html',countyes=countyes,countno=countno)

#route pelanggan_aktif
@app.route('/pelanggan_aktif')
def pelanggan_aktif():
    cursor = mysql.connection.cursor() #connect database 
    cursor.execute('''SELECT * FROM pelanggan WHERE churn="NO"''') #perintah sql menampilkan pelanggan churn no
    pelanggan_aktif = cursor.fetchall() 
    cursor.close()
    return render_template('pelanggan_aktif.html', pelanggan_aktif=pelanggan_aktif)

#route pelanggan_nonaktif
@app.route('/pelanggan_nonaktif')
def pelanggan_nonaktif():
    cursor = mysql.connection.cursor() #connect database 
    cursor.execute('''SELECT * FROM pelanggan WHERE churn="YES" ''') #perintah sql menampilkan pelanggan churn Yes
    pelanggan_nonaktif = cursor.fetchall()
    cursor.close()
    return render_template('pelanggan_nonaktif.html', pelanggan_nonaktif=pelanggan_nonaktif)

#route pelanggan
@app.route('/pelanggan')
def pelanggan():
    cursor = mysql.connection.cursor() #connect database 
    cursor.execute('''SELECT * FROM pelanggan ''') #menampilkan seluruh isi data pelanggan
    pelanggan=cursor.fetchall()
    cursor.close()
    return render_template('pelanggan.html', pelanggan=pelanggan)

#route menambahkan data pelanggan
@app.route('/pelanggan/tambah', methods=['POST'])
def tambahpelanggan():    
        name = request.form['name']
        gender = request.form['gender']
        seniorcitizen = request.form['seniorcitizen']
        partner = request.form['partner']
        tenure = request.form['tenure']
        phoneservice = request.form['phoneservice']
        streamingtv = request.form['streamingtv']
        internetservice = request.form['internetservice']
        papersbiling = request.form['papersbiling']
        monthlycharges = request.form['monthlycharges']
        totalcharges = float(monthlycharges) * int(tenure)
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO pelanggan( Name, Gender, SeniorCitizen, Partner, Tenure, PhoneService, StreamingTV, InternetService, PaperlessBilling, MonthlyCharges, TotalCharges)
                       VALUES(%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (name, gender, seniorcitizen, partner, tenure, phoneservice, streamingtv, internetservice, papersbiling, monthlycharges, totalcharges))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('pelanggan'))

#route menghapus data pelanggan
@app.route('/pelanggan/delete/<int:id>', methods=['GET'])
def deletepelanggan(id):     
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM pelanggan WHERE CustomerID = %s''', (id, ))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('pelanggan'))

#route edit data pelanggan
@app.route('/pelanggan/edit/<int:id>', methods=['GET', 'POST'])
def editpelanggan(id):     
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM pelanggan WHERE CustomerID = %s''', (id, ))
        pelanggan = cursor.fetchone()
        cursor.close()
        return redirect(url_for('pelanggan'))
    else:
        name = request.form['name']
        gender = request.form['gender']
        seniorcitizen = request.form['seniorcitizen']
        partner = request.form['partner']
        tenure = request.form['tenure']
        phoneservice = request.form['phoneservice']
        streamingtv = request.form['streamingtv']
        internetservice = request.form['internetservice']
        papersbiling = request.form['papersbiling']
        monthlycharges = request.form['monthlycharges']
        totalcharges = float(monthlycharges) * int(tenure)
        cursor = mysql.connection.cursor()
        cursor.execute(''' UPDATE pelanggan SET name = %s, Gender = %s, SeniorCitizen= %s,Partner= %s,Tenure= %s,PhoneService= %s,StreamingTV=%s,InternetService=%s, PaperlessBilling= %s,MonthlyCharges=  %s,TotalCharges= %s WHERE customerID = %s
        ''',(name, gender, seniorcitizen, partner, tenure, phoneservice, streamingtv, internetservice, papersbiling, monthlycharges, totalcharges, id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('pelanggan'))

#Prediksi churn data pelanggan 
@app.route("/predict", methods=["POST"])
def predict():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM pelanggan ''')
    pelanggan_predik = cursor.fetchall()
    
    #merubah data kategorik menjadi numerik
    for f in pelanggan_predik:
        if (f[3] == 'Female'):
            gender_pred = 0
        else:
            gender_pred = 1
        if (f[4] == 'No'):
            senior_pred = 0
        else:
            senior_pred = 1
        if (f[5] == 'No'):
            partner_pred = 0
        else:
            partner_pred = 1
        if (f[5] == 'No'):
            phoneservice_pred = 0
        else:
            phoneservice_pred = 1
        if (f[8] == 'No'):
            stream_pred = 0
        else:
            stream_pred = 1
        if (f[9] == 'No'):
            internet_pred = 0
        else:
            internet_pred = 1
        if (f[10] == 'No'):
            papersbil_pred = 0
        else:
            papersbil_pred = 1
        CustomerID = f[1]
        tenure_pred = f[6]
        monthnly_pred = f[11]
        total_pred = f[12]
        
        #memasukan data kedalam array
        data = [[gender_pred, senior_pred, partner_pred, tenure_pred, phoneservice_pred, 
        stream_pred, internet_pred, papersbil_pred, papersbil_pred, monthnly_pred]]
        
        #prediksi data 
        prediction_result = prediksi_data(data)
        
        #memasukan data Yes atau No kedalam kolom churn sesuai dengan ID customer
        cursor.execute('''UPDATE pelanggan SET Churn = %s WHERE CustomerID = %s''',
                       (prediction_result, CustomerID))
        mysql.connection.commit()
    return redirect(url_for('pelanggan'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
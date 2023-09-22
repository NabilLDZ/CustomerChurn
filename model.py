import pickle

# global variable
global model, scaler


#load model dan scaler
def load():
    global model, scaler
    model = pickle.load(open('model/model_knn.pkl', 'rb'))
    scaler = pickle.load(open('model/scaler_churn.pkl', 'rb'))

#fungsi prediksi data dan mereturn hasil 
def prediksi_data(data):
    data = scaler.transform(data)
    prediksi = int(model.predict(data))
    if prediksi == 0:
        hasil_prediksi = "No"
    else:
        hasil_prediksi = "Yes"
    return hasil_prediksi



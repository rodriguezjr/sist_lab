from sklearn.tree import DecisionTreeClassifier
import joblib


archivo = 'gest_lab/static/modelo_tesis.job'
loaded_model = joblib.load(archivo)
#datos = [[0,28,9.3,39,1,60,3.78,11.1,34.8,92.1,29.5,32.0,316,7.1]]
def evaluacion(datos):
    resultados = []
    result = loaded_model.predict_proba([datos])
    for x in result[0]:
        resultados.append("{:.2%}".format(x))

    return resultados

# evaluacion(datos)
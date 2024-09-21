from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def home():
    if request.method =="POST":
        fs = int(request.form["Fasting Sugar"])
        fu = int(request.form["Frequent Urination"])
        with open('my_ml_model_google','rb') as f:
            model = pickle.load(f)
        result = model.predict([[fs,fu]])
        if result[0]== 0:
            return render_template('ml_home.html',data=["Congratulations you dont have diabetes","green"])
        else:
            return render_template('ml_home.html',data=["Sorry you might have diabetes","red"])

    else:
        return render_template('ml_home.html')

@app.route('/about')
def about():
    return render_template('ml_about.html')



if __name__=="__main__":
    app.run(debug=True)
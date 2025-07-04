from flask import Flask,render_template,request,flash
import pickle
import numpy as np

with open('diabetesModel.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

app.secret_key = "sdfkj23klsdf!#@92jlkjLKJ987sdf@@#"

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods=[ 'POST'])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        if len(float_features) != 5:
            flash('Fill all the fields.', 'warning')
            return render_template('index.html')

        final_features = [np.array(float_features)]
        prediction = model.predict(final_features)[0]
        prob = model.predict_proba(final_features)[0][1]
        percentage = round(prob * 100, 2)
        status = "Diabetic" if prediction == 1 else "Not Diabetic"
        output = {
            'percentage':percentage,
            'status':status
        }

        return render_template('index.html', prediction_text=output,form_data=request.form)
    
    except ValueError:
        flash('Invalid input! Please enter numerical values.', 'danger')
        return render_template('index.html')

    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
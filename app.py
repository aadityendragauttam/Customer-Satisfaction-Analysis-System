from flask import Flask, request , url_for , render_template
import joblib
model = joblib.load(r'C:\Users\user\OneDrive\Desktop\Data Science\Customer-Satisfaction-Analysis-System\model\Customer_model.lb')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/history')
def history():
    return render_template('history.html')
@app.route('/project',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        customer_type = request.form['customer_type']
        type_of_travel = request.form['type_of_travel']
        class_type = request.form['class_type']
        age = request.form['age']
        flight_distance = request.form['flight_distance']
        inflight_entertainment = request.form['inflight_entertainment']
        baggage_handling = request.form['baggage_handling']
        cleanliness = request.form['cleanliness']
        departure_delay = request.form['departure_delay']

        gender_dict = {
    'Male':0,
    'Female':1
}
        gender = gender_dict.get(gender)
        cust_type_dict = {
    'Loyal Customer':0,'disloyal Customer':1
}
        customer_type = cust_type_dict.get(customer_type)

        travel_type_dict = {
    'Personal Travel':0,'Business travel':1
}
        type_of_travel = travel_type_dict.get(type_of_travel)

        class_dict =  {
    'Eco Plus':0, 'Business':1, 'Eco':2
}
        class_type = class_dict.get(class_type)
        pred = model.predict([[gender , customer_type , type_of_travel, class_type , age , flight_distance , inflight_entertainment ,baggage_handling,cleanliness , departure_delay]])
        if pred == 0:
            final = 'Not Satisfied'
        else:
            final = 'Satisfied'

        print('prediction :->>>',gender , customer_type , type_of_travel, class_type , age , flight_distance , inflight_entertainment ,baggage_handling,cleanliness , departure_delay)
    
    return render_template('project.html',prediction = final)


if __name__ == '__main__':
    app.run(debug=True)
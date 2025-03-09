from flask import Flask, render_template, request

app = Flask(__name__)

def get_health_advice(bmi):
    """Provides health advice based on BMI value"""
    if bmi < 18.5:
        return "Consider increasing your calorie intake with nutrient-rich foods."
    elif 18.5 <= bmi < 24.9:
        return "Maintain a balanced diet and regular physical activity to stay healthy."
    elif 25 <= bmi < 29.9:
        return "Consider incorporating a healthier diet and more exercise into your routine."
    else:
        return "It’s recommended to consult a healthcare provider for personalized guidance."
    
@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    status = None
    weight = None
    height = None
    advice= None
    if request.method == 'POST':
        try: 
            weight = float(request.form.get("weight", 0))
            height = float(request.form.get("height", 1))
            if height > 0 and weight > 0:
                bmi = round(weight / (height ** 2), 2)
                if bmi < 18.5:
                    status = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    status = "Normal weight"
                elif 25 <= bmi < 29.9:
                    status = "Overweight"
                else:
                    status = "Obese"     
                advice = get_health_advice(bmi)

        except ValueError:
            status = "Invalid input"

    return render_template("bmiweb.html", bmi=bmi, status=status, weight=weight, height=height, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)

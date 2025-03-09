from flask import Flask, render_template, request

app = Flask(__name__)

def get_health_advice(bmi):
    """Provides health advice based on BMI value"""
    if bmi < 18.5:
        return "You are underweight and may need to gain weight. Consider increasing calorie intake with nutrient-dense foods like nuts, avocados, lean proteins, and whole grains.  Include strength training exercises to build muscle mass."
    elif 18.5 <= bmi < 24.9:
        return "You have a healthy weight! Maintain it by continuing a balanced diet rich in vegetables, fruits, proteins, and whole grains. Regular physical activity (at least 150 minutes per week) is recommended."
    elif 25 <= bmi < 29.9:
        return "You are overweight. You may need to lose some weight for better health. Focus on eating more fiber-rich foods such as vegetables and whole grains. Reduce sugar and processed food intake. Increase physical activity (30 minutes daily of moderate exercise)."
    else:
        return "Your BMI indicates obesity. It is recommended to consult a healthcare provider for personalized guidance. Consider adopting a well-balanced diet with portion control and engaging in low-impact activities like swimming or walking daily."
    
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

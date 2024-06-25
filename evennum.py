from flask import Flask, render_template, request

app = Flask(__name__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.points = 0  # Initialize points to 0

people = []

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        person = Person(name, age)

        guess = int(request.form['guess'])
        results = []
        while True:
            if guess % 2 == 0:
                person.points += 2
                results.append(f"{person.name} wins 2 points for {guess} (Total points: {person.points})")
                guess += 2  # Increment by 2 if the number is even
                if person.points >= 100:
                    break
            else:
                results.append(f"{person.name} continues for {guess} (Total points: {person.points})")
                break

        if person.points >= 100:
            results.append(f"{person.name} Winner!!! has reached 100 points!")
        
        return render_template('template.html', results=results)

    return render_template('template.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)

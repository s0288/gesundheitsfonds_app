from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    okrs = [
                {
                    "objective": "Mit aktiven Auszeiten habe ich meine Anspannung reduziert.",
                    "key_results": [
                        "Ich hatte <15 h Termine pro Arbeitswoche.", 
                        "Ich hatte >10 h Deep-Work-Stunden pro Arbeitswoche.",
                        "Montags hatte ich <=1 h Termine.",
                        "Pro Tag war ich >5 Tsd. Schritte spazieren."
                    ]
                },
                {
                    "objective": "Ich habe meine Gesundheit im Blick.",
                    "key_results": [
                        "Ich habe 1 ein großes Blutbild erstellt & 1 MRT gemacht.",
                        ">10x habe ich notiert, was ich spüre, wenn ich Stress oder Anstrengung beobachte."
                    ]
                }
            ]
    return render_template('okrs.html', okrs=okrs)

if __name__ == '__main__':
    app.run(debug=True)

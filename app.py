from flask import Flask, render_template, request, redirect, url_for
from run_flow import run_pipeline
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        return redirect(url_for("recommendations", customer_id=customer_id))
    return render_template("index.html")

@app.route("/recommendations/<string:customer_id>")
def recommendations(customer_id):
    recs = run_pipeline(customer_id)
    return render_template("recommendations.html", customer_id=customer_id, recs=recs)

if __name__ == "__main__":
     app.run(debug=True)

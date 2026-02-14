from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/students"


# ✅ 1. Dashboard Page (List Students)
@app.route("/")
def home():
    students = requests.get(API_URL).json()
    return render_template("index.html", students=students)


# ✅ 2. Add Student Page
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "course": request.form["course"]
        }

        requests.post(API_URL, json=data)
        return redirect("/")

    return render_template("add.html")


# ✅ 3. Delete Student
@app.route("/delete/<int:id>")
def delete_student(id):
    requests.delete(f"{API_URL}/{id}")
    return redirect("/")


# ✅ 4. Edit Student Page (Fetch Student Data)
@app.route("/edit/<int:id>")
def edit_student(id):
    student = requests.get(f"{API_URL}/{id}").json()
    return render_template("edit.html", student=student)


# ✅ 5. Update Student (Submit Edit Form)
@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "course": request.form["course"]
    }

    requests.put(f"{API_URL}/{id}", json=data)
    return redirect("/")


# ✅ Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)

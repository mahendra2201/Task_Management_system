from flask import Flask, render_template, request, redirect
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

verify_otp = "0"
tasks = []
task_id_counter = 1


@app.route("/")
def landingpage():
    return render_template("sample.html")


@app.route("/getdata", methods=["POST", "GET"])
def mainpage():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        otp1 = random.randint(111111, 999999)
        global verify_otp
        verify_otp = str(otp1)

        from_email = 'mannem.mahendra2407@gmail.com'
        to_email = email
        subject = 'OTP For Validation'
        body = f'OTP for Validation is {verify_otp}'

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, 'dsju jftf aqnd wtje')  # Update with actual credentials
            server.send_message(msg)
            server.quit()
        except Exception as e:
            return f"Error in sending email: {e}"

        return render_template("sample2.html", name=name, email=email)
    else:
        return "<h3 style='color: red;'>Data received in an incorrect manner</h3>"


@app.route("/verifyemail", methods=["POST", "GET"])
def verifyemail():
    if request.method == "POST":
        name = request.form["name"]
        otp = request.form["otp"]
        if otp == verify_otp:
            return render_template("sample3.html", name=name, tasks=tasks)
        else:
            return render_template("sample2.html", name=name)
    else:
        return "Data received in an incorrect manner"


@app.route("/addtask", methods=["POST", "GET"])
def addtask():
    global task_id_counter
    global tasks
    taskname = request.form['task']
    name = request.form['username']
    tasks.append({'id': str(task_id_counter), 'content': taskname})
    task_id_counter += 1
    return render_template("sample3.html", tasks=tasks, name=name)


@app.route("/updatedata", methods=["POST", "GET"])
def updatedata():
    id = request.form['updated_id']
    content = request.form['updated_task']
    name = request.form['username']
    for data in tasks:
        if data['id'] == id:
            data['content'] = content
            break
    return render_template("sample3.html", tasks=tasks, name=name)


@app.route("/deletedata", methods=["POST", "GET"])
def deletedata():
    id = request.form['delete_data_id']
    name = request.form['username']
    tasks[:] = [task for task in tasks if task['id'] != id]
    return render_template("sample3.html", tasks=tasks, name=name)


if __name__ == "__main__":
    app.run(port=5001)

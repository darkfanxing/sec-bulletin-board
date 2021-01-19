from flask import Flask, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/api/changeDates", methods=["POST"])
def change_dates():
    dates = request.form["dates"].split(",")

    new_data = {}
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        new_data = data.copy()
        schedules_dates = list(data["schedules"].keys())

        for date in schedules_dates:
            if (date not in dates):
                new_data["schedules"].pop(date)
        
        for date in dates:
            if (date not in schedules_dates):
                new_data["schedules"][date] = {
                    "morning": [],
                    "afternoon": [],
                    "leaveOfficer": {}
                }
    
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(new_data, json_file, ensure_ascii=False)
        
    
    return json.dumps({"test": "123"})

@app.route("/api/addSchedule" ,methods=["POST"])
def add_schedule():
    schedule = request.form["schedule"]
    schedule = json.loads(schedule)
    date = schedule["date"]
    time = schedule["time"]
    schedule = schedule["schedule"]
    
    data = {}
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data["schedules"][date][time].append(schedule)

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    return "", 204

@app.route("/api/removeSchedule" ,methods=["POST"])
def remove_schedule():
    schedule = request.form["schedule"]
    schedule = json.loads(schedule)
    date = schedule["date"]
    time = schedule["time"]
    schedule = schedule["schedule"]
    
    data = {}
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data["schedules"][date][time].remove(schedule)

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    return "", 204

@app.route("/data.json")
def get_data():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data

@app.route("/api/getSchedules", methods=["POST"])
def get_schedules():
    time = request.form["time"]
    time = json.loads(time)
    
    date = time["date"]
    time = time["time"]

    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return json.dumps({"item": data["schedules"][date][time]})

@app.route("/api/getLeaveOfficers", methods=["POST"])
def get_leave_officers():
    leave_officer = request.form["leaveOfficer"]
    leave_officer = json.loads(leave_officer)
    
    date = leave_officer["date"]

    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return json.dumps({"names": list(data["schedules"][date]["leaveOfficer"].keys())})

@app.route("/api/addLeaveOfficer" ,methods=["POST"])
def add_leave_officer():
    data = request.form["leaveOfficer"]
    data = json.loads(data)
    
    date = data["date"]
    time = data["time"]
    name = data["name"]
    
    data = {}
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data["schedules"][date]["leaveOfficer"][name] = time

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    return "", 204

@app.route("/api/removeLeaveOfficer" ,methods=["POST"])
def remove_leave_officer():
    leave_officer = request.form["leaveOfficer"]
    leave_officer = json.loads(leave_officer)
    
    date = leave_officer["date"]
    name = leave_officer["name"]
    
    data = {}
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data["schedules"][date]["leaveOfficer"].pop(name)

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    return "", 204

@app.route("/api/changeReminder", methods=["POST"])
def change_reminder():
    reminder = request.form["reminder"]
    reminder = json.loads(reminder)

    data = {}
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data["reminder"] = reminder["note"]

    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
    
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
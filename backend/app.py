from flask import Flask, request, jsonify
from resume_parser import parse_resume
from matcher import match_skills
from vectorizer import rank_resumes
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["resume_db"]

@app.route("/upload", methods=["POST"])
def upload_resume():
    resume_file = request.files["resume"]
    job_desc = request.form["job_desc"]
    resume_text = parse_resume(resume_file)
    score = match_skills(resume_text, job_desc)
    db.results.insert_one({"resume": resume_text, "score": score})
    return jsonify({"score": score})

@app.route("/rank", methods=["POST"])
def rank():
    resumes = request.json["resumes"]
    job_desc = request.json["job_desc"]
    rankings = rank_resumes(resumes, job_desc)
    return jsonify(rankings)

if __name__ == "__main__":
    app.run()


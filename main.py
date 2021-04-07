from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from save import save_to_file

app = Flask("JobScrapper")

db={}

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  jobs=[]
  word = request.args.get("word")
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html",
  searching_by = word,
  results_number = len(jobs),
  jobs = jobs 
  )

  @app.route("/export")
  def export():
    try:
      word = request.args.get("word")
      if not word:
        raise Exception()
      word = word.lower()
      jobs = db.get(word)
      if not jobs:
        raise Exception()
      save_to_file(jobs)
      # issue : replit에서 not found 404 발생
      return send_file("jobs.csv")

    except:
      print("something is wrong.")
      return redirect("/")

app.run(host="0.0.0.0")

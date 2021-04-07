
from flask import Flask, render_template, request, redirect

def app():

  app = Flask("SuperScrapper")

  # /로 접속요청시 실행
  # @ : decorate. 아래에 있는 함수 실행
  @app.route("/")
  def home():
    # read from template html file
    return render_template("potato.html")

  @app.route("/contact")
  def aaa():
    return "Contact me!"

  # <> : placeholder. for using dynamic url
  @app.route("/<username>")
  def name(username):
    return f"Hello your name is {username}"

  # query arguments
  @app.route("/report")
  def report():
    word = request.args.get("word")
    # word == None일 경우 리다이렉트 처리 # word == None일 경우 리다이렉트 처리
    if word:
        word = word.lower()
    else:
        return redirect("/")
    return render_template("report.html", searching_by=word)

  app.run(host="0.0.0.0")
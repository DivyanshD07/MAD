from distutils.log import debug
from flask import Flask, render_template, request, url_for
from jinja2 import Template
import matplotlib.pylab as plt

app = Flask(__name__)

@app.route("/" , methods = ["POST", "GET"])
def school_program():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":

        d = open('data.csv')
        d.readline()
        data = []
        for l in d:
            data.append(l.strip().split(","))

        sid = [int(e[0]) for e in data]
        cid = [int(e[1]) for e in data]

        id = request.form["ID"]
        info = int(request.form["id_value"])

        if id == "student_id" and info in sid:
          c_id, marks, count = [], [], 0
          for elem in data:
              if int(elem[0]) == info:
                  c_id.append(elem[1])
                  marks.append(int(elem[2]))
                  count += 1
          tot = sum(marks)
          return render_template("s_data.html", c = count, student_id = info, course_id = c_id,
          mark = marks, total = tot)

        elif id == "course_id" and info in cid:
          marks = []
          for elem in data:
              if int(elem[1]) == info:
                  marks.append(int(elem[2]))
  
          avg_marks = sum(marks)/len(marks)
          m = max(marks)

          plt.hist(marks)
          plt.xlabel('Marks')
          plt.ylabel('Frequency')
          plt.savefig('./static/histo.PNG')

          return render_template("c_data.html", Max = m, Avg = avg_marks )

        else:
          return render_template("error.html")

    else:
      return render_template("error.html")



if __name__ == "__main__":
    app.run(debug = True)
    
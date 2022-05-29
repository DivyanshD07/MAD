import sys
from jinja2 import Template
import matplotlib.pyplot as plt

d = open('data.csv')
d.readline()
data = []
for l in d:
    data.append(l.strip().split(","))

sid = [int(e[0]) for e in data]
cid = [int(e[1]) for e in data]

def main():
  global data
  if len(sys.argv) > 2:
      task = sys.argv[1]
      if task == '-s' and int(sys.argv[2]) in sid:
          c_id, marks, count = [], [], 0
          s = sys.argv[2] 
          for elem in data:
              if elem[0] == s:
                  c_id.append(elem[1])
                  marks.append(int(elem[2]))
                  count += 1
          tot = sum(marks)
          temp = Template(TEMPLATE)
          content = temp.render(title = "Student Details", req = task , c = count, student_id = s, course_id = c_id,
          mark = marks, total = tot)
      
      elif task == '-c' and int(sys.argv[2]) in cid:
          marks = []
          s = int(sys.argv[2])
          for elem in data:
              if int(elem[1]) == s:
                  marks.append(int(elem[2]))
  
          avg_marks = sum(marks)/len(marks)
          m = max(marks)
          plt.hist(marks)
          plt.xlabel('Marks')
          plt.ylabel('Frequency')
          plt.savefig('histo.PNG')
          temp = Template(TEMPLATE)
          content = temp.render(title = "Course Data", req = task, Max = m, Avg = avg_marks )
      
      else:
          temp = Template(TEMPLATE)
          content = temp.render(title = "Something Went Wrong")
  
  else:
      temp = Template(TEMPLATE)
      content = temp.render(title = "Something Went Wrong")
                  
  out_doc = open("output.html" , 'w')
  out_doc.write(content)
  out_doc.close()

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
</head>
<body>
    {% if req == "-s" %}
    <h1>Student Data</h1>
    <table border="1">
        <tr>
            <th>Student id</th>
            <th>Course id</th>
            <th>Marks</th>
        </tr>
        {% for i in range(c) %}
        <tr>
          <td>{{student_id}}</td>
          <td>{{course_id[i]}}</td>
          <td>{{mark[i]}}</td>
        </tr>
        {% endfor %}
        <tr>
          <td colspan="2" align="center"> Total Marks </td>
          <td>{{total}}</td>
        </tr>
    </table>   
    {% elif req == "-c" %} 
    <h1>Course Details</h1>
    <table border="1">
      <tr>
        <th>Average Marks</th>
        <th>Maximum Marks</th>
      </tr>
      <tr>
        <td>{{Avg}}</td>
        <td>{{Max}}</td>
      </tr>
    </table>
    <img src="histo.PNG">
    {% else %}
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
    {% endif %}
</body>
</html>

 """

if __name__ == "__main__":
  main()



    
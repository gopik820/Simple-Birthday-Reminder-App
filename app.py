from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import requests
import json
import time
import sqlalchemy
import csv


app = Flask(__name__)


@app.route('/')
def index():
    
        return render_template('index.html')
    
  

@app.route('/list')
def get():
        bday=[]
        with open('data.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                        if row : 
                                row[1].replace(row[1][:4],'2020')
                                print(row[1])
                                bday.append(row)
        month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']        
        bday.sort(key = lambda date: datetime.strptime(str(date[1]), '%Y-%m-%d')) 

        
        for i in bday:
                mon=(month[int(i[1][5:7])-1])
                i[1]=mon+'-'+i[1][8:]
                
        return render_template('list.html',data=bday,len=len(bday))
    
@app.route('/add',methods=['GET','POST'])
def registration():
        if request.method == 'POST':
                with open('data.csv','a') as f:
                        obj=csv.writer(f)
                        obj.writerow([request.form["name"],request.form["DOB"]])
                        f.close() 
                return redirect('list')
        else:
                return render_template('add.html', pagetitle='Add Item')
    


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,request
from flask import render_template
import psycopg2
import psycopg2.extras

connection = psycopg2.connect("host=localhost dbname= user= password=")

app = Flask(__name__)

@app.route("/")
def top():
    return render_template('toppage.html')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/result', methods=['POST'])
def result():
    cur = connection.cursor()
    gender=request.form['gender']
    relation=request.form['relation']
    age=request.form['age']
    price=request.form['price']
    obejct=request.form['obejct']

    cur.execute("select gender,relation,age,price,obejct,item from present \
        where gender='%s' and relation='%s' and age='%s' and price='%s' \
        and obejct='%s';" % (gender,relation,age,price,obejct))
    res = cur.fetchall()
    cur.close()
    return render_template('result.html', result=res)


@app.route('/post', methods=['GET','POST'])
def po():
        cur= connection.cursor()
        gender=request.form['gender']
        relation=request.form['relation']
        age=request.form['age']
        price=request.form['price']
        obejct=request.form['obejct']
        item=request.form['item']

        cur.execute("insert into present(gender, relation, age, price, obejct, item) \
            values('%s','%s','%s','%s','%s','%s');" % (gender,relation,age,price,obejct,item)) 
        connection.commit()
        cur.close()
        return render_template('toppage.html')
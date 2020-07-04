from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
	return render_template('index.html')
@app.route('/<string:page_name>')

def work(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv',mode='a',newline='') as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv.write=csv.writer(database2,delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
		csv.write.writerow([email,subject,message])


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method =='POST':
		data=request.form.to_dict()
		write_to_csv(data)
		return redirect('Thankyou.html')
	else:
		return 'something went wrong!!'

#to get info in python file.



#@app.route('/go')
#def sec_page():
#	return render_template('sec_pg.html')

   


 #debugger help se hum chnges yha krenge appear vhi hoge without runnning again n again

#@app.route('/blog')
#def blog():
#	return 'Welcome guys!! my first folder'


#@app.route('/blog1')
#def blog1():
#	return 'hope uh liked it!'
	
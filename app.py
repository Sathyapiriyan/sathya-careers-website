from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Developer',
    'salary': 'Rs. 12,00,000',
    'location': 'Bengaluru',
    'responsibilities': ['HTML', 'CSS', 'JavaScript'],
    'requirements': ['Graduate', '2 years of experience'],
    'link': 'https://example.com/job3',
    'logo': 'https://example.com/job3_logo.png',
    'description':'We are looking for a talented and passionate Data Analyst to join our team. The role will be' 
  
}]


@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS, company_name='Sathya')

@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

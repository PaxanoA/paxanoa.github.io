from flask import Flask, render_template, request

app= Flask(__name__, template_folder="templates")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact-me')
def contact():
	return render_template('contact.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/donations')
def donations():
	return render_template('donations.html')


if __name__ == '__main__':
	app.run(debug=True, port=2025)
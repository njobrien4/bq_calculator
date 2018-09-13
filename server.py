from flask import Flask, render_template, request
from urllib import request as r
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('running.html')

@app.route('/my-link/')
def my_link():
	print ('I got clicked!')

	return 'Click.'

@app.route('/', methods=['POST'])
def my_form_post():
	url = request.form['url']
	f = r.urlopen(url)
	soup = BeautifulSoup(f.read())
	article_text = ''
	article = soup.findAll('p')
	article = [''.join(element.findAll(text=True)) for element in article]
	texts = soup.findAll(text=True)
	for text in texts:
		if text in article:
			article_text+='\n' + text
	print(len(texts), "is text len", texts, '\n')
	print(len(article), "is article", article)

	# for element in article:
	# 	article_text += '\n' + ''.join(element.findAll(text = True))
	return article_text


if __name__ == '__main__':
  app.run(debug=True)
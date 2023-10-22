from flask import Flask, request, render_template, redirect, url_for
import shortuuid

app = Flask(__name__)

url_mapping = {}  # In-memory storage for URL mapping

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form.get('long_url')
    short_url = shortuuid.ShortUUID().random(length=7)
    url_mapping[short_url] = long_url
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_url(short_url):
    if short_url in url_mapping:
        long_url = url_mapping[short_url]
        return redirect(long_url)
    else:
        return "URL not found"

if __name__ == '__main__':
    app.run(debug=True)

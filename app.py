from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def display_posts():
   try:
       url = "https://linkedin-data-api.p.rapidapi.com/get-profile-posts"
       querystring = {"username": "adamselipsky"}
       headers = {
           "x-rapidapi-key": "09720d47e1msh294d1bfc94be7b4p1d2280jsn1924b50801db",
           "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
       }
       response = requests.get(url, headers=headers, params=querystring)
       response.raise_for_status()
       posts_data = response.json()    

       # If the API returns a list directly
       if isinstance(posts_data, list):
        posts = posts_data
       # If the API wraps posts in a 'data' key
       elif isinstance(posts_data, dict) and 'data' in posts_data:
           posts = posts_data['data']
       else:
           posts = []
       return render_template('index.html', posts=posts)
   except requests.exceptions.RequestException as e:
       return render_template('index.html', posts=[], error=str(e))


if __name__ == '__main__':
   app.run(debug=True,port=5001)
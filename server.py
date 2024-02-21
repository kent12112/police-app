from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 6
post_data = [
  {
    "id": 1,
    "username": "ko Yanagishita",
    "title": "school shooting in Columbia U",
    "location": "Columbia University",
    "text": "Today, while on campus, I witnessed a horrifying incident. I saw an individual carrying a gun and randomly started shooting near the main entrance of Columbia University. The situation was chaotic, and everyone around was trying to find shelter and stay safe.",
    "image": "columbia.jpeg",
  },
  { 
    "id":2,
    "username": "Naoto Oka",
    "title": "sexual assault in subway nyc",
    "location": "nyc subway",
    "text": "In the crowded NYC subway, I unfortunately observed a distressing event. A person was sexually assaulting others in the subway car. It was a horrifying experience, and I hope that swift action is taken to ensure the safety of everyone using public transportation.",
    "image": "newyork-subway.jpeg",
  },
  { 
    "id":3,
    "username": "Norika Shigemura",
    "title": "Assault in union station",
    "location": "Union station",
    "text": "At Union Station today, I witnessed a disturbing incident. A person was assaulting random individuals within the station premises. It was a scary situation, and I hope that security measures are strengthened to prevent such incidents in the future.",
    "image": "union-station.jpeg"
  }, 
  { 
    "id":4,
    "username": "Asumi Yamamoto",
    "title": "Burglary in apple store nyc",
    "location": "Apple store, midtown",
    "text": "While shopping at the Apple Store in Midtown NYC, I observed a theft in progress. A person was stealing the latest iPhone model from the display. Store staff and security responded swiftly, but it was a concerning incident that highlights the need",
    "image": "apple-store-New-York.jpeg",
  }, 
  { "id":5,
    "username": "Sakuta Tokumoto",
    "title": "trafic accident in highway",
    "location": "Highway",
    "text": "Today, as I was driving on the highway, I witnessed a major traffic accident that brought traffic to a standstill. Multiple vehicles were involved, and emergency services were on the scene to provide assistance. It was a chaotic situation, and I hope everyone involved is safe and receives the necessary support.",
    "image": "highway.jpeg"
  }, 
  { 
    "id":6,
    "username": "Jonathan Barkat",
    "title": "Missing Person",
    "location": "unknown",
    "text": "I am reaching out to the community with a heavy heart. My younger brother has gone missing, and we are desperately seeking any information about his whereabouts. He was last seen at our home yesterday evening. If anyone has seen him or has any information, please contact the local authorities immediately. Your help is crucial in bringing my brother back safely. Thank you.",
    "image": "missing.jpeg",
  },
]

# ROUTES

@app.route('/')
def home():
    return render_template("main.html", post_data=post_data)


@app.route('/people')



# AJAX FUNCTIONS



@app.route('/save_post', methods=['POST'])
def save_post():
    global post_data
    global current_id

    username = "Kento Yanagishita"  # You might want to get the username from the session or elsewhere
    title = request.form['title']
    location = request.form['location']
    text = request.form['text']

    # Save the file
    image = None
    if 'image' in request.files:
        image_file = request.files['image']
        if image_file.filename != '':
            image_file = request.files['image']
            image_file.save(f'static/profile-image/{image_file.filename}')
    current_id += 1
    new_id = current_id
    new_post_entry = {
        "id": current_id,
        "username": username,
        "title": title,
        "location": location,
        "text": text,
        "image": image_file.filename if 'image' in request.files else None
    }
    post_data.insert(0, new_post_entry)

    return jsonify({"post_data": post_data})
 


if __name__ == '__main__':
   app.run(debug = True)





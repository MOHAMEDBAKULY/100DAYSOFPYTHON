from my_flask_file import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = """ <html>
       <body>
       <p><a href = "/home">Take me Home</a></p>
       </body>
    </html>
    """
    return page

@app.route('/home') # Creates the path to the home page
def home(): # Subroutine to create the home page
  today = datetime.date.today()
  # Three quotes followed by the html for the baldies site. Three more quotes to close. All the HTML is assigned to the 'page' variable
  page = f"""<html>

  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <div>{today}</div>
  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="static/images/day69.PNG" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>

</body>

</html>

  """

  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
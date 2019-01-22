Running Locally

With your Django App and Redis running, open two new terminal windows/tabs. 
In each new window, navigate to your project directory, activate your virtualenv, 
and then run the following commands (one in each window):

$ celery -A picha worker -l info

$ celery -A picha beat -l info

When you visit the site on http://127.0.0.1:8000/ you should now see one image.
Our app gets one image from Flickr every 15 minutes.

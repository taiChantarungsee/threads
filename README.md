# threads
Project for test from threads styling.

## Instructions

I recommend using either virtualenv or pyenv.

Run:
```
pip install -r requirements.txt
```
To install required libraries. 

Then run:
```
python manage.py migrate
```

To run database migrations. 

Then finally:
```
python manage.py runserver
```
And go to localhost:8000 to see the main page.

The website first displays a graph showing the average internet connection speed by place. Use the zoom tool on the left of the graph
to zoom in. Click on the button, under the title, to be taken to a similar graph that shows the average internet connection by district.

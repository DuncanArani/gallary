     Gallery
===================
## Description
This is a personal gallery application that enables you to dispay various photos of ```workout,Fashion and Travel.```

------------------------------------------------------------------------

## User Requirements

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos.
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Features

+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Bootstrap image model and copy link button.
+ [x] Filter images based on category and location.
+ [x] search functionality based on image description.




## Models
### Image Model
* Fields: Image, Image Name, Image Description, Image Location Foreign Key and Image category Foreign Key.

* `save_image()` - Save an image to the database.
* `delete_image()` - Delete image from the database.
* `update_image()` - Update image in the database.
* `get_image_by_id(id)` - Allows us to get an image using its ID.
* `search_image(category)` - Allows us to search for an image using its category.
* `filter_by_location(location)` - Allows us to filter images by the location.

### Location and Category models
* Location and category that link to the Image model.
* `save`, `update` and `delete` methods in both models

## Admin Dashboard
Use django admin to post photos to the database and manage the photos

## Setup

### Requirements
This project should be able to work on different kind of platforms
* Tested on Debian Linux
* Python3.6

### Cloning the repository
```bash
git clone git@github.com:https://github.com/DuncanArani/gallary
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```
pip3 install -r requirements
```




### Database migrations

``
python manage.py migrate
```


```

### Running the server 
```
python manage.py runserver
```



## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11]
* [Heroku](https://heroku.com)




### License
Copyright (c) {year} **{Morings School}**
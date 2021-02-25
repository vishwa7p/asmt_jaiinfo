# asmt_jaiinfo

# Employee CURD operations process.
This is the code repository for project [my_project using Django rest framework](https://github.com/vishwa7p/asmt_jaiinfo)

I have used Django rest framework to create CURD operations

I have also uses alternate method to create CRUD interfaces for a `Employee` model do please check...


## Setup Instructions

First make sure that you have the following installed.

* Python 3, and virtualenv

Now do the following to setup project

```

```
here I have used mysql database so plz make sure to make database setup 
```

# assuming that the project is already cloned.

cd my_project

# To create venv
python3 -m venv myenv

source pyenv/bin/activate

# one time or whenever any new package is added.
pip install -r requirements/dev.txt


# run makemigrations
python3 manage.py makemigrations employee

# run migrate
cd my_project
python3 manage.py migrate employee

```


```
cd my_project
python manage.py runserver
```



# Pizza Django Web App

A Django web application developed as an introductory project to explore the core concepts of web development with Django.

The application allows users to register and log in, create customised pizzas, view their saved pizzas, and complete a simple mock ordering process.

## Features

- User registration, login and logout
- User authentication using Django's built-in authentication system
- Protected routes using `@login_required`
- Custom pizza creation
- Multiple pizza configuration options:
  - Size
  - Crust
  - Sauce
  - Cheese
  - Toppings
- User-specific pizza history
- Basic order and confirmation flow
- Django forms and form validation
- Relational data modelling using Django ORM
- Template-based frontend using Django templates

## Technologies Used

- Python
- Django
- HTML
- CSS
- Django ORM
- SQLite

## Project Structure

The application follows Django's Model-View-Template architecture.

### Models

The project includes models for:

- `Pizza`
- `Size`
- `Crust`
- `Sauce`
- `Cheese`
- `Topping`
- `Payment`

Relationships between these models are implemented using Django `ForeignKey` and `ManyToManyField` relationships.

Each pizza is associated with the user who created it, allowing users to view only their own pizzas.

### Authentication

The application uses Django's built-in authentication functionality for:

- User registration
- Login
- Logout
- Restricting access to authenticated users

### Pizza Ordering Flow

A logged-in user can:

1. Create a customised pizza.
2. Select size, crust, sauce, cheese and toppings.
3. Save the pizza to their account.
4. Enter mock payment and delivery information.
5. View an order confirmation.

## What I Learned

This project provided practical experience with several fundamental Django concepts, including:

- Django project and application structure
- URL routing and views
- Django templates
- Forms and form validation
- User authentication
- Database models and relationships
- Django ORM queries
- Handling GET and POST requests
- Restricting data based on the authenticated user
- Building a simple end-to-end web application workflow

## Running the Project

Clone the repository:

```bash
git clone https://github.com/theorob284/Pizza-Django-Webapp.git
cd Pizza-Django-Webapp
```

Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate # On Windows
pip install django

python manage.py migrate

python manage.py runserver
```

Then open http://127.0.0.1:8000/
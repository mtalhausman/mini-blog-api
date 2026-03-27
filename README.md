## Live Demo

Base URL: https://muhammadtalhausman.pythonanywhere.com
Swagger Docs: https://muhammadtalhausman.pythonanywhere.com/api/docs/

# Mini Blog API

A Django REST Framework API for a simple blog platform with posts and comments.

## Tech Stack

- Python / Django 6.0
- Django REST Framework
- drf-spectacular (Swagger)
- SQLite

## Setup Instructions

```bash
# Clone the repo
git clone <your-repo-url>
cd Duseca_Django_Task

# Install dependencies
pip install django djangorestframework drf-spectacular django-cors-headers

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## API Endpoints

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| GET    | /api/posts/                    | List all posts           |
| POST   | /api/posts/                    | Create a post            |
| GET    | /api/posts/{id}/               | Get single post          |
| GET    | /api/posts/{post_id}/comments/ | List comments for a post |
| POST   | /api/posts/{post_id}/comments/ | Add comment to a post    |
| GET    | /api/top-posts/                | Top 3 posts by comments  |
| GET    | /api/most-active-user/         | Most active user         |

## Sample Requests & Responses

### Create a Post

**POST** `/api/posts/`

```json
{
  "title": "My First Post",
  "content": "This is the content.",
  "user": 1
}
```

**Response:**

```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content.",
  "created_at": "2026-03-27T10:00:00Z",
  "user": 1,
  "user_name": "Ali",
  "comment_count": 0
}
```

### Add a Comment

**POST** `/api/posts/1/comments/`

```json
{
  "user": 2,
  "comment_text": "Great post!"
}
```

## ORM Query Explanations

- **Top 3 posts:** Uses `annotate(Count)` to count comments per post, ordered by `-comment_count`
- **Active users:** Uses `annotate` + `filter(total_comments__gt=3)` to find heavy commenters
- **Most active user:** Annotates comment count and returns the first after descending sort
- **Comments for post:** Filters by `post_id`, ordered by `-created_at` for newest first

## Swagger Docs

Visit `/api/docs/` after running the server.

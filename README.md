# Employee Skills (Flask + MongoDB Atlas) ✅

**Simple employee skills creation and search tool** built with **Flask** and **MongoDB Atlas**. Use the app to enter employee details (first name, last name, skills, city, country) and to query employees by name, skill, city or any other field.

---

## Features

- Enter employee details (skills can be comma-separated) ✅
- Store employee records in MongoDB Atlas ✅
- Query employees by any field (name, skill, city, country, or a free-text search) ✅

---

## Requirements

- Python 3.8+ (3.11 recommended)
- A MongoDB Atlas connection string (see Environment)

The project uses the packages listed in `requirements.txt`.

---

## Environment

Create a `.env` file in the project directory and set your MongoDB connection string:

```
MONGO_DB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
```

Notes:
- If using MongoDB Atlas, ensure your IP is allowed in the Atlas network access and that the user has appropriate privileges.
- The app uses TLS for Atlas; the code imports `certifi` when connecting.

---

## Run locally

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your `MONGO_DB_URL` to `.env` in the project root.

4. Start the app:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000/ in your browser to enter employees or go to `/query` to search.

---

## File overview

- `app.py` — Flask application and MongoDB integration
- `templates/` — Jinja2 templates (`home.html`, `entry.html`, `query.html` etc.)

---

## Security & Notes

- Do not commit your `.env` containing credentials.
- This is a simple demo app; consider adding authentication and input validation for production use.

---

## License

MIT

# REST API with Flask
REST API intended to save and retrieve stores and items from those stores.

# Endpoints
- `GET /store`: Get a list of stores.
- `GET /store/:name`: Get a specific store by name.
- `GET /store/:name/item`: Get items from a specific store by name.
- `POST /store`: Create a new store.
- `POST /store/:name/item`: Create and item for a specific store by name.

# Project structure
The following is the file structure of the project.
```
├── src
│  ├── templates
│  │  └── index.html
│  └── app.py
├── .gitignore
└── README.md
```

# Picxam

A full-stack quiz platform that generates multi-choice and open-ended questions from images extracted from uploaded documents.

## Tech Stack

- **Backend**: Django 6.0 (Python)
- **Frontend**: Vue 3, TypeScript, Tailwind CSS 4, Vite
- **ORM**: Django ORM with PostgreSQL
- **Auth**: Email-based authentication via Django Allauth
- **Rendering**: Inertia.js (Vue 3 adapter)

## Getting Started

### Prerequisites

- Python 3.x
- Node.js
- pnpm (or npm)

### Setup

1. **Clone the repo and install Python dependencies:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Install frontend dependencies:**

   ```bash
   pnpm install
   ```

3. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

### Development

Start both the Vite dev server and Django dev server:

```powershell
.\dev.ps1
```

This will run the Vite HMR server and Django's development server concurrently.

### Production Build

```powershell
.\build.ps1
```

Builds Vite assets, collects Django static files, and starts the production server.

## Project Structure

```
picxam/
├── app/              # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
├── core/             # Main Django app
│   ├── models.py     # CustomUser, Document, Quiz, Question, etc.
│   ├── views.py
│   └── admin.py
├── resources/        # Frontend source
│   ├── css/app.css
│   └── js/
│       ├── components/
│       ├── composables/
│       ├── layouts/
│       ├── pages/
│       └── types/
├── manage.py
├── dev.ps1           # Development launcher
└── build.ps1         # Production build script
```

> > > > > > > 2738653 (chore: picxam v1.0)

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from datetime import datetime
from forms import EventForm, RegisterForm
from data import events, categories, next_id
from utils import slugify, parse_datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-me"

# Inject categories globally for navbar filters
@app.context_processor
def inject_globals():
    return {"CATEGORIES": categories}

def get_event_or_404(slug):
    for e in events:
        if e["slug"] == slug:
            return e
    abort(404)

@app.route("/")
def index():
    # Upcoming events sorted by datetime
    upcoming = sorted(
        [e for e in events if parse_datetime(e["date"], e["time"]) >= datetime.now()],
        key=lambda e: parse_datetime(e["date"], e["time"])
    )
    featured = [e for e in upcoming if e.get("featured")]
    return render_template("index.html", events=upcoming, featured=featured)

@app.route("/event/<slug>/")
def event_detail(slug):
    e = get_event_or_404(slug)
    remaining = e["max_attendees"] - len(e["attendees"])
    return render_template("event_detail.html", event=e, remaining=remaining)

@app.route("/admin/event/", methods=["GET", "POST"])
def admin_event():
    form = EventForm()
    form.category.choices = [(c, c) for c in categories]

    if request.method == "POST" and form.validate_on_submit():
        # avoid duplicate slugs
        slug = form.slug.data.strip() or slugify(form.title.data)
        if any(ev["slug"] == slug for ev in events):
            flash("El slug ya existe. Elige otro.", "error")
            return render_template("admin_event.html", form=form), 400

        new_event = {
            "id": next_id(),
            "title": form.title.data.strip(),
            "slug": slug,
            "description": form.description.data.strip(),
            "date": form.date.data.strftime("%Y-%m-%d"),
            "time": form.time.data.strftime("%H:%M"),
            "location": form.location.data.strip(),
            "category": form.category.data,
            "max_attendees": form.max_attendees.data,
            "attendees": [],
            "featured": bool(form.featured.data),
        }
        events.append(new_event)
        flash("Evento creado exitosamente ✅", "success")
        return redirect(url_for("event_detail", slug=new_event["slug"]))

    # GET or validation errors
    return render_template("admin_event.html", form=form)

@app.route("/event/<slug>/register/", methods=["GET", "POST"])
def register(slug):
    e = get_event_or_404(slug)
    form = RegisterForm()
    remaining = e["max_attendees"] - len(e["attendees"])

    if request.method == "POST" and form.validate_on_submit():
        # capacity check
        if remaining <= 0:
            flash("El evento alcanzó el cupo máximo.", "error")
            return redirect(url_for("event_detail", slug=slug))

        # duplicate email check
        email = form.email.data.strip().lower()
        if any(a["email"].lower() == email for a in e["attendees"]):
            flash("Este correo ya está registrado para este evento.", "error")
            return redirect(url_for("event_detail", slug=slug))

        e["attendees"].append({"name": form.name.data.strip(), "email": email})
        flash("Registro exitoso 🎉", "success")
        return redirect(url_for("event_detail", slug=slug))

    return render_template("register.html", form=form, event=e, remaining=remaining)

@app.route("/events/category/<category>/")
def by_category(category):
    if category not in categories:
        flash("Categoría no válida.", "error")
        return redirect(url_for("index"))
    filtered = [e for e in events if e["category"] == category]
    filtered = sorted(filtered, key=lambda e: parse_datetime(e["date"], e["time"]))
    return render_template("index.html", events=filtered, featured=[e for e in filtered if e.get("featured")], selected_category=category)

# Friendly 404
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)

from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import os
import random

# Instancia de Markdown para convertir el contenido
markdowner = Markdown()

def index(request):
    # Página de inicio que muestra todas las entradas
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    
    if entry is None:
        # Si la entrada no existe, mostrar página de error
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    
    # Convertir el contenido de Markdown a HTML
    content = markdowner.convert(entry)
    
    # Renderizar la página de la entrada con el contenido convertido
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    # Captura el término de búsqueda ingresado por el usuario
    query = request.GET.get('q', '').strip()

    # Verifica si el término de búsqueda coincide exactamente con una entrada
    entry_content = util.get_entry(query)

    if entry_content:
        # Si hay coincidencia exacta, redirige a la página de la entrada
        return HttpResponseRedirect(reverse('entry', args=[query]))
    else:
        # Si no hay coincidencia exacta, busca coincidencias parciales
        matching_entries = [entry for entry in util.list_entries() if query.lower() in entry.lower()]

        # Renderiza los resultados de coincidencias parciales
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "results": matching_entries
        })

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea, label="Content")

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Verificar si ya existe una entrada con ese título
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/error.html", {
                    "message": "An entry with this title already exists."
                })

            # Guardar la nueva entrada
            util.save_entry(title, content)

            # Redirigir a la nueva página
            return redirect("entry", title=title)

    else:
        form = NewPageForm()

    return render(request, "encyclopedia/new_page.html", {
        "form": form
    })

def delete_page(request, title):
    # Verificar si la entrada existe
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The page you're trying to delete does not exist."
        })

    # Eliminar la entrada si existe
    entry_path = f"entries/{title}.md"
    if os.path.exists(entry_path):
        os.remove(entry_path)

    # Redirigir al índice después de la eliminación
    return redirect("index")

class EditPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea, label="Content")

def edit_page(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The page you are trying to edit does not exist."
        })

    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect("entry", title=title)
    else:
        form = EditPageForm(initial={"title": title, "content": entry})

    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "form": form
    })

def random_page(request):
    # Obtener todas las entradas disponibles
    entries = util.list_entries()
    # Elegir una entrada aleatoria
    random_entry = random.choice(entries)
    # Redirigir a la página de la entrada aleatoria
    return redirect("entry", title=random_entry)

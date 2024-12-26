# %% [markdown]
# **Task 08: Completing missing data**

# %%
#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

# %% [markdown]
# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# %%
from rdflib.namespace import RDF, FOAF

for s in g1.subjects(RDF.type, FOAF.Person):
  given_name = g1.value(subject=s, predicate=FOAF.givenName)
  family_name = g1.value(subject=s, predicate=FOAF.familyName)
  email = g1.value(subject=s, predicate=FOAF.mbox)

  if not given_name:
    given_name = g2.value(subject=s, predicate=FOAF.givenName)
    if given_name:
      g1.add((s, FOAF.givenName, given_name))

  if not family_name:
    family_name = g2.value(subject=s, predicate=FOAF.familyName)
    if family_name:
      g1.add((s, FOAF.familyName, family_name))

  if not email:
    email = g2.value(subject=s, predicate=FOAF.mbox)
    if email:
      g1.add((s, FOAF.mbox, email))



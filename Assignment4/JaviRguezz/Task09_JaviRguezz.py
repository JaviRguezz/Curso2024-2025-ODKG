# %% [markdown]
# **Task 09: Data linking**

# %%
#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials/"

# %%
from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")

# %% [markdown]
# Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.

# %%
from rdflib import RDF, OWL

# Define namespaces
ns1 = Namespace("http://data.org#")
ns2 = Namespace("http://data2.org#")
owl = Namespace("http://www.w3.org/2002/07/owl#")


for s1, p1, o1 in g1.triples((None, ns1.givenName, None)):
  for s2, p2, o2 in g2.triples((None, ns2.givenName, o1)):
    familyName1 = list(g1.objects(s1, ns1.familyName))
    familyName2 = list(g2.objects(s2, ns2.familyName))
    if familyName1 and familyName2 and familyName1[0] == familyName2[0]:
      g3.add((s1, owl.sameAs, s2))




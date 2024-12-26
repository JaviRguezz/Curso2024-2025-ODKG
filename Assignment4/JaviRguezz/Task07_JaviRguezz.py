# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

# %% [markdown]
# First let's read the RDF file

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# %% [markdown]
# **TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**

# %%
# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
  SELECT ?subclass WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing.
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns}
)
# Visualize the results

for r in g.query(q1):
  print(r)

# %% [markdown]
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# %%
# TO DO
q2 = prepareQuery('''
  SELECT ?individual WHERE {
    { ?individual rdf:type ns:Person. }
    UNION
    { ?subclass rdfs:subClassOf ns:Person. ?individual rdf:type ?subclass.}
  }
  ''',
  initNs = { "rdf": RDF, "rdfs": RDFS, "ns": ns}
)
# Visualize the results
for r in g.query(q2):
  print(r)

# %% [markdown]
# **TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**
# 

# %%
# TO DO
q3 = prepareQuery('''
  SELECT ?individual WHERE {
    { ?individual rdf:type ns:Person. }
    UNION
    { ?individual rdf:type ns:Animal. }
  }
  ''',
  initNs = { "rdf": RDF, "ns": ns}
)
# Visualize the results
for r in g.query(q3):
  print(r)

# %% [markdown]
# **TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**

# %%
# TO DO
q4 = prepareQuery('''
  SELECT ?name WHERE {
    ?person vcard:FN ?name.
    ?person ns:knows ns:RockySmith.
  }
  ''',
  initNs = { "vcard": Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), "ns": ns}
)
# Visualize the results
for r in g.query(q4):
  print(r)

# %% [markdown]
# **Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**

# %%
# TO DO
q5 = prepareQuery('''
  SELECT ?name WHERE {
    ?animal rdf:type ns:Animal.
    ?animal vcard:FN ?name.
    ?animal ns:knows ?otherAnimal.
    ?otherAnimal rdf:type ns:Animal.
  }
  ''',
  initNs = { "rdf": RDF, "vcard": Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), "ns": ns}
)
# Visualize the results
for r in g.query(q5):
  print(r)

# %% [markdown]
# **Task 7.6: List the age of all living things in descending order (in SPARQL only)**

# %%
# TO DO
q6 = prepareQuery('''
  SELECT ?age WHERE {
    ?livingThing rdf:type ?type.
    ?type rdfs:subClassOf* ns:LivingThing.
    ?livingThing ns:age ?age.
  } ORDER BY DESC(?age)
  ''',
  initNs = { "rdf": RDF, "rdfs": RDFS, "ns": ns}
)
# Visualize the results
for r in g.query(q6):
  print(r)



from train_cypher import examples
def get_schema_text(node_props, rels):
    return f"""
  This is the schema representation of the Neo4j database.
  Node properties are the following:
  {node_props}
  Relationships from source to target nodes:
  {rels}
  Make sure to respect relationship types and directions
  """
  
def get_system_message(schema_text):
    return f"""
        You are an assistant with an ability to generate Cypher queries.
        Task: Generate Cypher queries to query a Neo4j graph database based on the provided schema definition.
        Instructions:
        Use only the provided relationship types.
        Do not use any other relationship types or properties that are not provided.
        If you cannot generate a Cypher statement based on the provided schema, explain the reason to the user.
        Schema:
        {schema_text}
        Example cypher queries are:
        {examples}
        """

def get_graph_model_metadata():
    return get_schema_text(node_props=node_properties,rels=relationships_props)

def get_sys_prompts():
    schema_txt = get_graph_model_metadata()
    return get_system_message(schema_txt)
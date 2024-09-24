from neo4j import GraphDatabase

# Database connection details
host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'admin1234'

# Create the driver connection
driver = GraphDatabase.driver(host, auth=(user, password))

# Cypher query to create nodes and relationships
def create_nodes_and_relationships(tx):
    # Create 10 Assembly nodes
    for i in range(1, 11):
        tx.run(f"CREATE (a:Assembly {{name: 'Assembly{i}'}})")

    # Create 10 CPP nodes
    for i in range(1, 11):
        tx.run(f"CREATE (c:CPP {{name: 'CPP{i}'}})")

    # Create 10 Function nodes
    for i in range(1, 11):
        tx.run(f"CREATE (f:Function {{name: 'Function{i}'}})")

    # Create relationships as per the examples provided
    query = """
    MATCH (a1:Assembly {name: 'Assembly1'}), (cpp1:CPP {name: 'CPP1'}), 
          (a2:Assembly {name: 'Assembly2'}), (cpp3:CPP {name: 'CPP3'}), 
          (f5:Function {name: 'Function5'})
    CREATE (a1)-[:LINKED_TO]->(cpp1)-[:LINKED_TO]->(a2)-[:LINKED_TO]->(cpp3)-[:LINKED_TO]->(f5)
    WITH a1, cpp1, a2, cpp3, f5
    MATCH (a2:Assembly {name: 'Assembly2'}), (cpp4:CPP {name: 'CPP4'}), 
          (cpp3:CPP {name: 'CPP3'}), (f5:Function {name: 'Function5'})
    CREATE (a2)-[:LINKED_TO]->(cpp4)-[:LINKED_TO]->(cpp3)-[:LINKED_TO]->(f5)
    WITH a2, cpp4, cpp3, f5
    MATCH (a9:Assembly {name: 'Assembly9'}), (a3:Assembly {name: 'Assembly3'}), 
          (cpp3:CPP {name: 'CPP3'}), (f5:Function {name: 'Function5'})
    CREATE (a9)-[:LINKED_TO]->(a3)-[:LINKED_TO]->(cpp3)-[:LINKED_TO]->(f5)
    """
    tx.run(query)

    # Generate 10 more relationships similar to the provided examples
    query_10_more = """
    MATCH (a1:Assembly {name: 'Assembly1'}), (cpp2:CPP {name: 'CPP2'}), 
          (a3:Assembly {name: 'Assembly3'}), (cpp5:CPP {name: 'CPP5'}), 
          (f7:Function {name: 'Function7'})
    CREATE (a1)-[:LINKED_TO]->(cpp2)-[:LINKED_TO]->(a3)-[:LINKED_TO]->(cpp5)-[:LINKED_TO]->(f7)
    WITH a1, cpp2, a3, cpp5, f7
    MATCH (a4:Assembly {name: 'Assembly4'}), (cpp6:CPP {name: 'CPP6'}), 
          (cpp7:CPP {name: 'CPP7'}), (f8:Function {name: 'Function8'})
    CREATE (a4)-[:LINKED_TO]->(cpp6)-[:LINKED_TO]->(cpp7)-[:LINKED_TO]->(f8)
    WITH a4, cpp6, cpp7, f8
    MATCH (a5:Assembly {name: 'Assembly5'}), (cpp8:CPP {name: 'CPP8'}), 
          (a6:Assembly {name: 'Assembly6'}), (cpp9:CPP {name: 'CPP9'}), 
          (f9:Function {name: 'Function9'})
    CREATE (a5)-[:LINKED_TO]->(cpp8)-[:LINKED_TO]->(a6)-[:LINKED_TO]->(cpp9)-[:LINKED_TO]->(f9)
    WITH a5, cpp8, a6, cpp9, f9
    MATCH (a7:Assembly {name: 'Assembly7'}), (cpp10:CPP {name: 'CPP10'}), 
          (a8:Assembly {name: 'Assembly8'}), (f6:Function {name: 'Function6'})
    CREATE (a7)-[:LINKED_TO]->(cpp10)-[:LINKED_TO]->(a8)-[:LINKED_TO]->(f6)
    WITH a7, cpp10, a8, f6
    MATCH (a10:Assembly {name: 'Assembly10'}), (cpp3:CPP {name: 'CPP3'}), 
          (a2:Assembly {name: 'Assembly2'}), (f1:Function {name: 'Function1'})
    CREATE (a10)-[:LINKED_TO]->(cpp3)-[:LINKED_TO]->(a2)-[:LINKED_TO]->(f1)
    WITH a10, cpp3, a2, f1
    MATCH (a1:Assembly {name: 'Assembly1'}), (cpp4:CPP {name: 'CPP4'}), 
          (cpp7:CPP {name: 'CPP7'}), (f2:Function {name: 'Function2'})
    CREATE (a1)-[:LINKED_TO]->(cpp4)-[:LINKED_TO]->(cpp7)-[:LINKED_TO]->(f2)
    WITH a1, cpp4, cpp7, f2
    MATCH (a3:Assembly {name: 'Assembly3'}), (cpp1:CPP {name: 'CPP1'}), 
          (a4:Assembly {name: 'Assembly4'}), (f3:Function {name: 'Function3'})
    CREATE (a3)-[:LINKED_TO]->(cpp1)-[:LINKED_TO]->(a4)-[:LINKED_TO]->(f3)
    WITH a3, cpp1, a4, f3
    MATCH (a6:Assembly {name: 'Assembly6'}), (cpp2:CPP {name: 'CPP2'}), 
          (a5:Assembly {name: 'Assembly5'}), (f4:Function {name: 'Function4'})
    CREATE (a6)-[:LINKED_TO]->(cpp2)-[:LINKED_TO]->(a5)-[:LINKED_TO]->(f4)
    WITH a6, cpp2, a5, f4
    MATCH (a7:Assembly {name: 'Assembly7'}), (cpp6:CPP {name: 'CPP6'}), 
          (a9:Assembly {name: 'Assembly9'}), (f10:Function {name: 'Function10'})
    CREATE (a7)-[:LINKED_TO]->(cpp6)-[:LINKED_TO]->(a9)-[:LINKED_TO]->(f10)
    WITH a7, cpp6, a9, f10
    MATCH (a8:Assembly {name: 'Assembly8'}), (cpp10:CPP {name: 'CPP10'}), 
          (a1:Assembly {name: 'Assembly1'}), (f5:Function {name: 'Function5'})
    CREATE (a8)-[:LINKED_TO]->(cpp10)-[:LINKED_TO]->(a1)-[:LINKED_TO]->(f5)
    """
    tx.run(query_10_more)

# Function to run the query
def insert_nodes_and_relationships():
    with driver.session() as session:
        session.write_transaction(create_nodes_and_relationships)

# Insert nodes and relationships
insert_nodes_and_relationships()



# Function to create attributes for a specific node
def create_attributes_to_node(tx, node_id):
    set_query = """
    MATCH (a:Assembly) 
    WHERE id(a) = $node_id
    SET a.type = 'Assembly Object',
        a.weight = '-9',
        a.specs = 'Card transaction code',
        a.description = 'An assembly class contains card transaction objects',
        a.return_type = 'binary object'
    RETURN a
    """
    # Run the query with the passed node_id
    tx.run(set_query, node_id=node_id)

# Function to insert attributes for a node within a session transaction
def insert_node_attributes(session, node_id):
    session.write_transaction(create_attributes_to_node, node_id)

# Function to get all Assembly node IDs and store them in a list
def get_assembly_node_ids(tx):
    # Cypher query to retrieve all Assembly node IDs
    query = "MATCH (a:Assembly) RETURN id(a) AS node_id"
    result = tx.run(query)
    
    # Store all node IDs in a list
    node_ids = [record["node_id"] for record in result]
    return node_ids

# Function to run the query and process the list
def fetch_assembly_nodes():
    with driver.session() as session:
        # Get the list of Assembly node IDs
        node_ids = session.read_transaction(get_assembly_node_ids)
        
        # Loop through each node ID and update its attributes
        for node_id in node_ids:
            insert_node_attributes(session, node_id)

# Fetch Assembly node_id and insert attributes
fetch_assembly_nodes()


# Function to fetch all relationships of type "LINKED_TO"
def fetch_all_relationships(tx):
    query = """
    MATCH (n)-[r:LINKED_TO]->(m)
    RETURN id(n) AS start_node_id, id(m) AS end_node_id, type(r) AS relationship_type
    """
    result = tx.run(query)
    
    # Store all relationships in a list of dictionaries
    relationships = []
    for record in result:
        relationships.append({
            "start_node_id": record["start_node_id"],
            "end_node_id": record["end_node_id"],
            "relationship_type": record["relationship_type"]
        })
    return relationships

# Function to execute the transaction and fetch the relationships
def get_all_relationships():
    with driver.session() as session:
        relationships = session.read_transaction(fetch_all_relationships)
        return relationships

# Example usage: Fetch all relationships and print them
relationships = get_all_relationships()
for rel in relationships:
    print(f"Start Node ID: {rel['start_node_id']}, End Node ID: {rel['end_node_id']}, Relationship: {rel['relationship_type']}")




# Function to fetch the node ID where the name is 'CPP7'
def fetch_node_id(tx):
    query = """
    MATCH (c:CPP {name: 'CPP7'}) 
    RETURN id(c) AS node_id
    """
    result = tx.run(query)
    
    # Return the node ID of CPP7 (if it exists)
    record = result.single()  # Fetch the single result
    if record:
        return record["node_id"]
    else:
        return None  # Return None if no matching node is found

# Function to execute the transaction and get the CPP7 node ID
def get_node_id():
    with driver.session() as session:
        node_id = session.read_transaction(fetch_node_id)
        return node_id

# Function to edit attributes for a specific node
def edit_attributes_to_node(tx, node_id):
    edit_query = """
    MATCH (c:CPP) 
    WHERE id(c) = $node_id
    SET c.type = 'CPP Object',
        c.weight = '3',
        c.specs = 'Card holder details',
        c.description = 'A CPP class contains card holder details objects',
        c.return_type = 'string'
    RETURN c
    """
    # Run the query with the passed node_id
    tx.run(edit_query, node_id=node_id)

# Function to insert attributes for a node within a session transaction
def insert_edit_node_attributes(node_id):
    with driver.session() as session:
        session.write_transaction(edit_attributes_to_node, node_id)

# Example usage: Fetch the node ID where name is 'CPP7' and update its attributes
node_id = get_node_id()
if node_id:
    insert_edit_node_attributes(node_id)
    print(f"Node ID {node_id} attributes updated successfully.")
else:
    print("No node with the name 'CPP7' found.")



# Function to update relationships
def update_relationships(tx):
    query = """
    MATCH (a1:Assembly {name: 'Assembly1'}), (a4:Assembly {name: 'Assembly4'}), 
          (cpp9:CPP {name: 'CPP9'}), (f4:Function {name: 'Function4'}), 
          (cpp8:CPP {name: 'CPP8'}), (f2:Function {name: 'Function2'})
    // Create bidirectional relationships between Assembly1 and Assembly4
    CREATE (a1)-[:LINKED_TO]->(a4)
    CREATE (a4)-[:LINKED_TO]->(a1)
    
    // Create unidirectional relationships for the rest
    CREATE (a4)-[:LINKED_TO]->(cpp9)-[:LINKED_TO]->(f4)-[:LINKED_TO]->(cpp8)-[:LINKED_TO]->(f2)
    """
    # Run the query
    tx.run(query)

# Function to execute the transaction to update relationships
def execute_update_relationships():
    with driver.session() as session:
        session.write_transaction(update_relationships)

# Run the relationship update
execute_update_relationships()

 
# Close the driver connection
driver.close()





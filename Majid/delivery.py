

import sqlite3

# Connect to the database using a properly formatted path.
connection = sqlite3.connect("C:/Users/becod/AI/projects/07-delivery_market_analysis_with_SQL/databases/takeaway.db")

cursor = connection.cursor()

# Execute the SQL query to fetch rows.
cursor.execute("""
               SELECT price FROM menuItems LIMIT 10;
               """)

# Fetch all results and store them in a variable.
results = cursor.fetchall()

# Print the fetched results.
print(results)

# Close the connection when done.
connection.close()



# query1 = f"SELECT artistId FROM artists WHERE name = 'Aerosmith';"
# cursor.execute(query1)
# artist_id = cursor.fetchone()[0]

# artist_id
# print(artist_id)

# query2 = f"""
#     SELECT 
#         albumId 
#     FROM 
#         albums
#     WHERE 
#         artistId = '{artist_id}';
        
# """
# albums_ids = []
# for row in cursor.execute(query2):
#     albums_ids.append(str(row[0]))

# print(albums_ids)

# query3 = f"""
#     SELECT 
#         DISTINCT name 
#     FROM 
#         tracks 
#     WHERE 
#         albumId IN ({','.join(albums_ids)});
# """
# for row in cursor.execute(query3):
#     print(row[0])

# query4 = f"""
#     SELECT
#         DISTINCT(tracks.name)
#     FROM
#         artists
#         JOIN albums ON artists.artistId = albums.artistId
#         JOIN tracks ON albums.albumId = tracks.albumId
#     WHERE 
#         artists.name = 'Aerosmith';
# """
# songs = set()
# for row in cursor.execute(query4):
#     print(row[0])

import sqlite3

# connect to database
conn = sqlite3.connect('backend/database/DatasetVectors.db')
cursor = conn.cursor()

# create table for the DatasetImages
cursor.execute('''
CREATE TABLE IF NOT EXISTS DatasetImages (
    image_id INTEGER PRIMARY KEY,
    data BLOB,   
    )
''')

# create table for the DatasetVectors
cursor.execute('''
CREATE TABLE IF NOT EXISTS DatasetVectors (
    vector_id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (image_id)
        REFERENCES DatasetImages (image_id),
    plot_x REAL,
    plot_y REAL
)
''')

### populating the Dataset Images
'''
def populate_DatasetImages(given a image dataset?):
    image_id is arrayIndex,
    data is the byteStream or Image file?
'''

# poulating the Dataset Vectors
def populate_DatasetVectors(vstack):

    for i in range(vstack):
        query = "INSERT INTO 'DatasetVectors' ('image_id', 'plot_x', 'plot_y') VALUES ('" + i + "', '')"
        cursor.execute(query)




# commit and close
conn.commit()
conn.close()

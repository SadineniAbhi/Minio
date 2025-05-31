from fastavro import reader

with open("records/users.avro", "rb") as fo:
    for record in reader(fo):
        print(record)

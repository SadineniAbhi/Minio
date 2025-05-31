from minio import Minio
from PyPDF2 import PdfReader
import io

client = Minio(
    "localhost:9000",
    access_key="ROOTUSER",
    secret_key="CHANGEME123",
    secure=False  # Important for local setup without HTTPS
)

# geting buckets
# my_buks = client.list_buckets()
# for buck in my_buks:
#     print(buck)

# geting objs
# my_objs = client.list_objects(bucket_name="abhibuck")
# for obj in my_objs:
#     print(obj)

# response = client.get_object("abhibuck", "python.pdf")
# pdf_bytes = io.BytesIO(response.read())
# reader = PdfReader(pdf_bytes)  
# page = reader.pages[0]
# print(page.extract_text())
# response.close()
# response.release_conn()


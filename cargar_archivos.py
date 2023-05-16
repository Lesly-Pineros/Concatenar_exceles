# %%
from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
import shutil
from os import listdir
from os import scandir, getcwd
from os.path import join
from os.path import dirname
from os.path import basename
import numpy as np


# %%
def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""
     
    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'key.json')

    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    
    #returns a public url
    return blob.public_url


# %%
#nombres para el bucket
def nombres(ruta = '.'):
    return listdir(ruta)

#ruta del documento
def ls(ruta = getcwd()):
    return [join(dirname(arch.path),basename(arch.path)) for arch in scandir(ruta) if arch.is_file()]


# %%
a=np.array(nombres("archivos"))
b=np.array(ls("archivos"))

# %%
for i in range (len(a)):
    upload_to_bucket(a[i],b[i],"demo-stratus" )
    shutil.move(b[i], "historico")




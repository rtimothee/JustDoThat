from django.conf import settings

def handle_uploaded_file(file):
    path = settings.IMAGE_UPLOAD_PATH
    destination = open(path + file.name, 'wb+')
    
    for chunk in file.chunks():
        destination.write(chunk)
    
    destination.close()
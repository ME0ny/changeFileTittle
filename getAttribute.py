import hachoir
import subprocess
import datetime
def get_media_properties(filename):

    result = subprocess.Popen(['hachoir-metadata', filename, '--raw', '--level=9'],
        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

    results = result.stdout.read().decode('utf-8').split('\r\n')

    properties = {}
    for item in results:
        if '- creation_date:' in item:
            return(item[16:])

path = 'D:/Users/79143/видео Артём/5 секунд/данные/март/IMG_20200711_020001_427.mp4'

print(get_media_properties(path))
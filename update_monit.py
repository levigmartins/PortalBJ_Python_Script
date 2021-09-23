import requests

downloadUrl = 'https://uploads.brasiljunior.org.br/uploads/report/file/38950/ejs_202120210923-17253-kymigd.xlsx'

req = requests.get(downloadUrl)
filename = req.url[downloadUrl.rfind('/')+1:]

with open("C:/Users/levig/Downloads/" + filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
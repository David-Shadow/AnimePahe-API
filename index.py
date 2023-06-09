from app import app
from scrappers.pahe.download import pahe_download
if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
    print(pahe_download('3ab9a35e-3cc4-6dac-6c47-042da51a20bf$0e9ac900494c3e18df6fcdd39c8fc0f978a05436745df190c0b734108d1963b3'))

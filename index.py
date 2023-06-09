from app import app
from scrappers.pahe.download import pahe_download
if __name__ == '__main__':
    app.run(debug=True)
    print(pahe_download('f9825cf8-ac20-a4bf-9530-951fe7e38032$642492e502f5afba06ce1c206bc5be18cb28b685796f9712e955f0fe38867ac7'))

from flask import Flask, render_template

app = Flask(__name__)

# Пример списка рекламных блоков
ads = [
    {"width": 10, "height": 10, 
     "image": "/static/images/thd.jpeg", 
     "title": "Величайший паблик про Доту", "url": "http://vk.com/thd322"}
]

# Расчёт проданных и доступных пикселей -- сейчас кажется неправильно
total_pixels = 1000000  # Всего пикселей
sold_pixels = sum(ad['width'] * ad['height'] for ad in ads)  # Суммарная площадь проданных пикселей
available_pixels = total_pixels - sold_pixels  # Доступные пиксели

@app.route('/')
def home():
    return render_template('index.html', ads=ads, sold_pixels=sold_pixels, available_pixels=available_pixels)

if __name__ == '__main__':
    app.run(debug=True)

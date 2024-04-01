from flask import Flask, render_template

app = Flask(__name__)

# Пример списка рекламных блоков
ads = [
    {"x": 0, "y": 0, "width": 100, "height": 100, 
     "image": "/static/images/thd.jpeg", 
     "title": "Подпись 1", "url": "http://example.com"},
    # Добавь другие рекламные блоки по аналогии
]

# Расчёт проданных и доступных пикселей
total_pixels = 1000000  # Всего пикселей
sold_pixels = sum(ad['width'] * ad['height'] for ad in ads)  # Суммарная площадь проданных пикселей
available_pixels = total_pixels - sold_pixels  # Доступные пиксели

@app.route('/')
def home():
    return render_template('index.html', ads=ads, sold_pixels=sold_pixels, available_pixels=available_pixels)

if __name__ == '__main__':
    app.run(debug=True)

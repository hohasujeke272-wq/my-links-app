from flask import Flask, redirect
import os

app = Flask(__name__)

# ضع رابط صفحة X ورابط الصورة هنا
PAGE_X_URL = "https://your-page-x-link.com" 
IMAGE_URL = "https://waterlearndream.ams3.digitaloceanspaces.com/paintnatureart"

# تحميل الكلمات من الملف
def load_words():
    with open('words.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

all_words = load_words()
half = len(all_words) // 2
# تقسيم الكلمات: النصف الأول لصفحة X والنصف الثاني للصورة
route_map = {word: PAGE_X_URL for word in all_words[:half]}
route_map.update({word: IMAGE_URL for word in all_words[half:]})

@app.route('/<word>')
def redirect_logic(word):
    target = route_map.get(word)
    if target:
        return redirect(target, code=301)
    return "Link not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
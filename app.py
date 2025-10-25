from flask import Flask, request, render_template, send_file, redirect, url_for, flash
import os
import uuid
from yt_dlp import YoutubeDL

app = Flask(__name__)
app.secret_key = 'secret_key'  # ضروري لو استخدمنا flash messages

DOWNLOAD_FOLDER = 'downloads'
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('url')
        if not video_url:
            flash("الرجاء إدخال رابط الفيديو")
            return redirect(url_for('index'))

        # اسم فريد للملف
        output_filename = f"{uuid.uuid4()}.mp4"
        output_path = os.path.join(DOWNLOAD_FOLDER, output_filename)

        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path,
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            # يرجع تحميل الملف مباشرة
            return send_file(output_path, as_attachment=True)
        
        except Exception as e:
            flash(f"حدث خطأ أثناء التحميل: {str(e)}")
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

services_data = [
    {
        'id': 1,
        'title': 'Hukum Pidana',
        'icon': 'fa-gavel',
        'image': 'https://pusatdapodik.com/wp-content/uploads/2024/01/Hukum-Pidana.jpg',
        'description': 'Pendampingan perkara pidana dari konsultasi hingga persidangan.'
    },
    {
        'id': 2,
        'title': 'Hukum Perdata',
        'icon': 'fa-handshake',
        'image': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQxdTNd6pbytanzwNpHaanamu8OBZGNp1xC9NUF8T89insqG36KSLh0KOa9mFwdC-jzaYVvIo83OOwpg_tG4ucr8IFub8mrGFoyV4gK6MQpJPcuB3jhJgxdgH6ceKU7NIlLr6VRUIJG3j4zMYfBdGPGazvv_tUAkrdetkfnIBfKicwPkN6sdmcJhSw/s694/Hukum%20perdata%202022-11-21%20122953.png',
        'description': 'Penyelesaian sengketa perdata, kontrak, wanprestasi, dan utang piutang.'
    },
    {
        'id': 3,
        'title': 'Perceraian & Keluarga',
        'icon': 'fa-heart-crack',
        'image': 'https://uag.ac.id/images/Berita/2025/september/Ketika-Perceraian-Mengguncang-Bisnis-Keluarga.jpg',
        'description': 'Pendampingan perceraian, hak asuh anak, nafkah, dan harta bersama.'
    },
    {
        'id': 4,
        'title': 'Sengketa Tanah & Properti',
        'icon': 'fa-map',
        'image': 'https://remax.co.id/_next/image?url=https%3A%2F%2Fremax-files-pr0d.s3.ap-southeast-1.amazonaws.com%2Fremax%2Farticles%2F9f07169c-3de2-44ff-a392-829f392c9e03.jpg&w=3840&q=75',
        'description': 'Penyelesaian sengketa tanah, sertifikat, jual beli, dan properti.'
    },
    {
        'id': 5,
        'title': 'Konsultasi Hukum',
        'icon': 'fa-comments',
        'image': 'https://www.perajanusa.id/wp-content/uploads/2019/07/Pengacara-hukum.jpg',
        'description': 'Konsultasi hukum untuk kebutuhan pribadi, bisnis, dan keluarga.'
    },
    {
    'id': 6,
    'title': 'Hak Waris',
    'icon': 'fa-scale-balanced',
    'image': 'https://anaksholeh.net/wp-content/uploads/2021/02/hak-waris-1-1.jpg',
    'description': 'Pendampingan pembagian warisan, ahli waris, dan sengketa waris.'
    },
    {
        'id': 7,
        'title': 'Bisnis & Perusahaan',
        'icon': 'fa-building',
        'image': 'https://tandahijau.com/wp-content/uploads/2024/10/company-profile-bisnis.jpg',
        'description': 'Layanan hukum bisnis, kontrak, badan usaha, dan perusahaan.'
    },
    {
        'id': 8,
        'title': 'Perlindungan Konsumen',
        'icon': 'fa-shield',
        'image': 'https://images.suarapembaca.com/data/2025/05/image-20250519191223.jpg',
        'description': 'Pendampingan sengketa konsumen dan pengajuan ganti rugi.'
    },
    {
        'id': 9,
        'title': 'Hukum Ketenagakerjaan',
        'icon': 'fa-briefcase',
        'image': 'https://www.legalnow.co.id/wp-content/uploads/2023/11/hukum-ketenagakerjaan.jpg',
        'description': 'Pendampingan PHK, hak karyawan, dan hubungan industrial.'
    },
    {
        'id': 10,
        'title': 'Hukum Perbankan & Keuangan',
        'icon': 'fa-landmark',
        'image': 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghH_NTBXy3wvcHx6aFNbLW0zhXACsAC-snGYHXQcSUKtNZQfTWcMqhiM7WTwF6Zs12YtLTAg4S0ZIFYvhexyVU8brPqLx4W4loaoQclGx4QLzv3BWMrU43hbWG1f5bccsCgnS4LWVGF4I/s400/Keuangan.jpg',
        'description': 'Sengketa kredit, pembiayaan, utang piutang, dan restrukturisasi.'
    },
    {
    'id': 11,
    'title': 'Hukum Tata Usaha Negara',
    'icon': 'fa-user-shield',
    'image': 'https://fjp-law.com/id/wp-content/uploads/2020/05/Pengadilan-Tata-Usaha-Negara-1024x675.png',
    'description': 'Gugatan PTUN, sengketa izin, dan keputusan administrasi pemerintah.'
    },
    {
        'id': 12,
        'title': 'Hukum Kontrak & Perjanjian',
        'icon': 'fa-file-contract',
        'image': 'https://izinesia.id/wp-content/uploads/2021/07/asas-asas-hukum-kontrak-perjanjian-768x384.jpg',
        'description': 'Pembuatan, pemeriksaan, dan penyelesaian sengketa perjanjian.'
    },
    {
        'id': 13,
        'title': 'Hukum Pidana Khusus',
        'icon': 'fa-user-lock',
        'image': 'https://tse3.mm.bing.net/th/id/OIP.A89m599Z2BInvLUTsbBzVgHaE8?pid=Api&h=220&P=0',
        'description': 'Pendampingan perkara narkotika, ITE, korupsi, dan pidana khusus.'
    },
    {
        'id': 14,
        'title': 'Hukum Administrasi Negara',
        'icon': 'fa-landmark-dome',
        'image': 'https://i.pinimg.com/1200x/2b/64/55/2b6455fdb76fb44294b30603ea7913aa.jpg',
        'description': 'Pendampingan masalah administrasi negara dan kebijakan pemerintahan.'
    },
    {
        'id': 15,
        'title': 'Hukum Investasi',
        'icon': 'fa-chart-line',
        'image': 'https://iblam.ac.id/wp-content/uploads/2024/04/Hukum-Investasi-untuk-Kesejahteraan-Masyarakat-di-Era-Globalisasi-2-980x654.jpg',
        'description': 'Konsultasi investasi, legalitas usaha, dan perlindungan investor.'
    },
    {
        'id': 16,
        'title': 'Layanan Hukum Umum Lainnya',
        'icon': 'fa-balance-scale',
        'image': 'https://www.perajanusa.id/wp-content/uploads/2019/07/Pengacara-hukum.jpg',
        'description': 'Pendampingan hukum untuk berbagai kebutuhan klien.'
    }
]

articles_data = [
    {
        'id': 1,
        'title': 'Pentingnya Konsultasi Hukum Sebelum Mengambil Keputusan',
        'category': 'Konsultasi Hukum',
        'date': '2026-05-29',
        'author': 'Kantor Hukum Arman',
        'thumbnail': 'https://www.perajanusa.id/wp-content/uploads/2019/07/Pengacara-hukum.jpg',
        'excerpt': 'Konsultasi hukum membantu masyarakat memahami risiko, hak, dan langkah yang tepat sebelum mengambil keputusan penting.'
    },
    {
        'id': 2,
        'title': 'Langkah Awal Jika Menghadapi Sengketa Tanah',
        'category': 'Sengketa Tanah',
        'date': '2026-05-29',
        'author': 'Kantor Hukum Arman',
        'thumbnail': 'https://remax.co.id/_next/image?url=https%3A%2F%2Fremax-files-pr0d.s3.ap-southeast-1.amazonaws.com%2Fremax%2Farticles%2F9f07169c-3de2-44ff-a392-829f392c9e03.jpg&w=3840&q=75',
        'excerpt': 'Sengketa tanah perlu ditangani dengan bukti dokumen yang kuat, kronologi jelas, dan pendampingan hukum yang tepat.'
    },
    {
        'id': 3,
        'title': 'Memahami Perbedaan Hukum Pidana dan Perdata',
        'category': 'Edukasi Hukum',
        'date': '2026-05-29',
        'author': 'Kantor Hukum Arman',
        'thumbnail': 'https://pusatdapodik.com/wp-content/uploads/2024/01/Hukum-Pidana.jpg',
        'excerpt': 'Hukum pidana dan perdata memiliki tujuan, proses, dan akibat hukum yang berbeda. Masyarakat perlu memahami perbedaannya.'
    }
]

testimonials_data = [
    {
        'id': 1,
        'name': 'Klien Google Maps',
        'position': 'Klien Konsultasi',
        'company': 'Bandung',
        'rating': 5,
        'content': 'Pelayanan konsultasi hukumnya sangat membantu, penjelasannya jelas, dan prosesnya profesional.'
    },
    {
        'id': 2,
        'name': 'Klien Google Maps',
        'position': 'Klien Pendampingan',
        'company': 'Bandung',
        'rating': 5,
        'content': 'Respon cepat dan arahan hukumnya mudah dipahami. Sangat membantu dalam mengambil keputusan.'
    },
    {
        'id': 3,
        'name': 'Klien Google Maps',
        'position': 'Klien Hukum',
        'company': 'Bandung',
        'rating': 5,
        'content': 'Kantor hukum terpercaya, komunikatif, dan memberikan solusi yang sesuai dengan kebutuhan klien.'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html', services=services_data)

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=articles_data)

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html', testimonials=testimonials_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/consultation')
def consultation():
    return render_template('consultation.html')

@app.route('/api/submit-consultation', methods=['POST'])
def submit_consultation():
    return jsonify({
        'success': True,
        'message': 'Konsultasi Anda telah diterima. Kami akan menghubungi Anda dalam 24 jam.'
    })

@app.route('/api/submit-contact', methods=['POST'])
def submit_contact():
    return jsonify({
        'success': True,
        'message': 'Pesan Anda telah dikirim. Terima kasih telah menghubungi kami.'
    })

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, render_template_string, request

views = Blueprint("views", __name__)

# Data nomor darurat
emergency_numbers = {
    "Polisi": "110",
    "Ambulans": "118",
    "Pemadam Kebakaran": "113",
    "SAR": "115",
    "Nomor Darurat Nasional": "112",
    "Nomor Kekerasan Anak dan Perempuan": "129",
    "PLN (Listrik)": "123",
    "Jasa Marga": "14080",
    "Posko COVID-19": "119",
    "Posko Bencana Alam": "129",
    "PMI (Palang Merah Indonesia)": "021-7992325",
    "Komnas HAM": "021-3925230",
    "BNPB (Badan Nasional Penanggulangan Bencana)": "117",
    "Layanan Derek": "02542078787",
}

navbar = """
<nav class="nav-box">
    <a href="/">🏠 Beranda</a>
    <a href="/tentang">✨ Tentang</a>
</nav>
"""


@views.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").lower()
    show_all = request.args.get("show_all", "").lower() == "true"
    
    if query:
        filtered = {k: v for k, v in emergency_numbers.items() if query in k.lower()}
    else:
        filtered = emergency_numbers
    
    displayed = filtered if show_all else dict(list(filtered.items())[:5])

    descriptions = {
        "Polisi": "untuk melaporkan tindak kriminal, perampokan, kecelakaan lalu lintas, atau gangguan keamanan di lingkunganmu.",
        "Ambulans": "untuk kondisi medis darurat, orang pingsan, serangan jantung, atau butuh transportasi cepat ke rumah sakit.",
        "Pemadam Kebakaran": "selain untuk kebakaran, nomor ini juga berfungsi untuk penyelamatan teknis seperti evakuasi hewan liar atau cincin yang tersangkut.",
        "SAR": "untuk pencarian dan pertolongan pada kecelakaan besar, orang hilang di alam (hutan/gunung), atau musibah pelayaran.",
        "Nomor Darurat Nasional": "ini adalah nomor tunggal (mirip 911) yang bisa dihubungi meski HP tanpa kartu SIM atau terkunci untuk diarahkan ke layanan bantuan terdekat.",
        "Nomor Kekerasan Anak dan Perempuan": "layanan SAPA untuk perlindungan dan pengaduan jika terjadi kekerasan dalam rumah tangga atau pelecehan.",
        "PLN (Listrik)": "untuk melaporkan mati lampu total, kabel PLN yang putus/terbakar, atau gangguan pada gardu listrik.",
        "Jasa Marga": "untuk meminta bantuan saat mobil mogok, ban pecah, atau butuh informasi kemacetan saat berada di jalan tol.",
        "Posko COVID-19": "layanan informasi terkait penanganan virus, jadwal vaksin, atau prosedur isolasi mandiri.",
        "Posko Bencana Alam": "untuk melaporkan situasi bencana seperti banjir, tanah longsor, atau gempa bumi di suatu wilayah.",
        "PMI (Palang Merah Indonesia)": "untuk kebutuhan stok darah darurat atau bantuan kemanusiaan lainnya.",
        "Komnas HAM": "untuk pengaduan jika ada pelanggaran hak asasi manusia yang dilakukan oleh pihak tertentu.",
        "BNPB (Badan Nasional Penanggulangan Bencana)": "pusat informasi dan koordinasi penanggulangan bencana skala besar secara nasional.",
        "Layanan Derek": "untuk menderek kendaraan yang tidak bisa berjalan akibat kerusakan mesin atau kecelakaan.",
    }
    logos = {
        "Polisi": "/static/polisi.png",
        "Ambulans": "/static/Ambulans.jpg",
        "Pemadam Kebakaran": "/static/Damkar.png",
        "SAR": "/static/Sar.png",
        "Nomor Darurat Nasional": "/static/Darurat nasional Indonesia.jpg",
        "Nomor Kekerasan Anak dan Perempuan": "/static/kekerasan anak & perempuan.png",
        "PLN (Listrik)": "/static/Pln.png",
        "Jasa Marga": "/static/Jasa marga.png",
        "Posko COVID-19": "/static/Covid19.png",
        "Posko Bencana Alam": "/static/Posko.png",
        "PMI (Palang Merah Indonesia)": "/static/Pmi.png",
        "Komnas HAM": "/static/komnas ham.png",
        "BNPB (Badan Nasional Penanggulangan Bencana)": "/static/Bnpb.jpg",
        "Layanan Derek": "/static/Layanan derek.jpg",
    }

    html = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>My Savior Web</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            /* Default Light Mode */
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
                margin: 0;
                background: #fdfdfd;
                color: #1c1c1e;
            }
            .header {
                background: #ffffff;
                text-align: center;
                padding: 50px 20px;
                font-size: 42px;
                font-weight: 700;
                border-bottom: 1px solid #e5e5ea;
            }
            .header span {
                color: #007aff;
            }
            .nav-box {
                margin: 20px auto;
                display: flex;
                gap: 20px;
                justify-content: center;
            }
            .nav-box a {
                text-decoration: none;
                font-weight: 600;
                color: #007aff;
                padding: 8px 14px;
                border-radius: 8px;
                transition: background 0.3s;
            }
            .nav-box a:hover {
                background: rgba(0,122,255,0.1);
            }
            .search-bar {
                text-align: center;
                margin: 30px;
            }
            .search-bar input {
                width: 60%;
                padding: 12px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 8px;
                transition: 0.3s;
            }
            .search-bar input:focus {
                border-color: #007aff;
                outline: none;
                box-shadow: 0 0 8px rgba(0,122,255,0.3);
            }
            ul {
                list-style: none;
                padding: 0;
                max-width: 500px;
                margin: 20px auto;
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }
            li {
                padding: 16px 20px;
                border-bottom: 1px solid #e5e5ea;
                font-size: 18px;
                transition: background 0.2s;
                cursor: pointer;
                display: flex;
                align-items: center;
                gap: 12px;
            }
            .logo {
                width: 40px;
                height: 40px;
                min-width: 40px;
            }
            .logo img {
                width: 100%;
                height: 100%;
                object-fit: contain;
            }
            li:hover {
                background: rgba(0,122,255,0.05);
            }
            li:last-child {
                border-bottom: none;
            }
            .description-box {
                background: #f2f2f7;
                padding: 12px 20px;
                font-size: 14px;
                color: #5a5a5c;
                border-bottom: 1px solid #e5e5ea;
                display: none;
                animation: slideDown 0.3s ease-out;
                margin-left: 52px;
            }
            .description-box.active {
                display: block;
            }
            @keyframes slideDown {
                from {
                    opacity: 0;
                    max-height: 0;
                }
                to {
                    opacity: 1;
                    max-height: 200px;
                }
            }
            .show-more-btn {
                text-align: center;
                margin: 20px;
                display: flex;
                gap: 10px;
                justify-content: center;
            }
            .show-more-btn a {
                display: inline-block;
                background: #007aff;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                transition: background 0.3s;
            }
            .show-more-btn a:hover {
                background: #0051d5;
            }
            footer {
                text-align: center;
                padding: 30px;
                background: #f9f9f9;
                border-top: 1px solid #e5e5ea;
                margin-top: 60px;
                font-size: 14px;
                color: #8e8e93;
            }

            /* Dark Mode otomatis mengikuti sistem */
            @media (prefers-color-scheme: dark) {
                body {
                    background: #1c1c1e;
                    color: #fdfdfd;
                }
                .header {
                    background: #2c2c2e;
                    color: #fdfdfd;
                    border-bottom: 1px solid #3a3a3c;
                }
                ul {
                    background: #2c2c2e;
                    box-shadow: 0 4px 12px rgba(255,255,255,0.05);
                }
                li {
                    border-bottom: 1px solid #3a3a3c;
                }
                li:hover {
                    background: rgba(0,122,255,0.1);
                }
                .description-box {
                    background: #3a3a3c;
                    color: #a1a1a6;
                    border-bottom: 1px solid #3a3a3c;
                }
                footer {
                    background: #2c2c2e;
                    color: #d1d1d6;
                    border-top: 1px solid #3a3a3c;
                }
            }
        </style>
    </head>
    <body>
        <header class="header">My <span>Savior</span> Web</header>
        """ + navbar + """
        <div class="search-bar">
            <form method="get" action="/">
                <input type="text" name="q" placeholder="Cari layanan darurat..." value="{{ query }}">
            </form>
        </div>
        <ul id="emergency-list">
        {% for layanan, nomor in displayed.items() %}
            <li onclick="toggleDescription(this)" data-description="{{ descriptions.get(layanan, '') }}">
                <div class="logo"><img src="{{ logos.get(layanan, '/static/default.png') }}" alt="{{ layanan }}"></div>
                <span><b>{{ layanan }}</b>: {{ nomor }}</span>
            </li>
            <div class="description-box"></div>
        {% endfor %}
        </ul>
        {% if filtered|length > 5 %}
        <div class="show-more-btn">
            {% if not show_all %}
                <a href="/?q={{ query }}&show_all=true">Tampilkan Lebih Banyak</a>
            {% else %}
                <a href="/?q={{ query }}">Tampilkan Lebih Sedikit</a>
            {% endif %}
        </div>
        {% endif %}
        <footer>&copy; 2026 My Savior Web. Semua Hak ga dilindungi.</footer>
        <script>
            function toggleDescription(element) {
                const descBox = element.nextElementSibling;
                const isActive = descBox.classList.contains('active');
                
                // Tutup semua deskripsi yang aktif
                document.querySelectorAll('.description-box.active').forEach(box => {
                    box.classList.remove('active');
                });
                
                // Buka deskripsi jika belum aktif
                if (!isActive) {
                    descBox.textContent = element.getAttribute('data-description');
                    descBox.classList.add('active');
                }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html, displayed=displayed, filtered=filtered, query=query, show_all=show_all, descriptions=descriptions, logos=logos)


@views.route("/tentang", methods=["GET"])
def tentang():
    html = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Tentang - My Savior Web</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            /* Default Light Mode */
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
                margin: 0;
                background: #fdfdfd;
                color: #1c1c1e;
            }
            .header {
                background: #ffffff;
                text-align: center;
                padding: 50px 20px;
                font-size: 42px;
                font-weight: 700;
                border-bottom: 1px solid #e5e5ea;
            }
            .header span {
                color: #007aff;
            }
            .nav-box {
                margin: 20px auto;
                display: flex;
                gap: 20px;
                justify-content: center;
            }
            .nav-box a {
                text-decoration: none;
                font-weight: 600;
                color: #007aff;
                padding: 8px 14px;
                border-radius: 8px;
                transition: background 0.3s;
            }
            .nav-box a:hover {
                background: rgba(0,122,255,0.1);
            }
            .content {
                max-width: 600px;
                margin: 40px auto;
                padding: 20px;
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }
            .content h1 {
                color: #007aff;
                margin-top: 0;
            }
            .content p {
                line-height: 1.6;
                font-size: 16px;
            }
            footer {
                text-align: center;
                padding: 30px;
                background: #f9f9f9;
                border-top: 1px solid #e5e5ea;
                margin-top: 60px;
                font-size: 14px;
                color: #8e8e93;
            }
            
            @media (prefers-color-scheme: dark) {
                body {
                    background: #1c1c1e;
                    color: #fdfdfd;
                }
                .header {
                    background: #2c2c2e;
                    color: #fdfdfd;
                    border-bottom: 1px solid #3a3a3c;
                }
                .content {
                    background: #2c2c2e;
                    box-shadow: 0 4px 12px rgba(255,255,255,0.05);
                }
                .content p {
                    color: #d1d1d6;
                }
                footer {
                    background: #2c2c2e;
                    color: #d1d1d6;
                    border-top: 1px solid #3a3a3c;
                }
            }
        </style>
    </head>
    <body>
        <header class="header">My <span>Savior</span> Web</header>
        """ + navbar + """
        <div class="content">
            <h1>Tentang Web ✨</h1>
            <p>Web ini dibuat oleh anak anak</p>
        </div>
        <footer>&copy; 2026 My Savior Web. Semua Hak ga dilindungi.</footer>
    </body>
    </html>
    """
    return render_template_string(html)
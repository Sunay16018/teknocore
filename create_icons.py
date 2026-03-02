from PIL import Image, ImageDraw, ImageFilter
import math

def create_icon1():
    """Gelişmiş Yıldız - Anti-aliasing + Gradyan"""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Ana yıldız
    points = []
    for i in range(10):
        angle = (i * 36 - 90) * 3.14159 / 180
        r = 200 if i % 2 == 0 else 100
        x = 256 + r * math.cos(angle)
        y = 256 + r * math.sin(angle)
        points.append((x, y))
    
    # Gradyan efekti için çoklu katman
    draw.polygon(points, fill=(65, 105, 225, 255))  # Royal Blue
    
    # İç katman
    points2 = []
    for i in range(10):
        angle = (i * 36 - 90) * 3.14159 / 180
        r = 150 if i % 2 == 0 else 70
        x = 256 + r * math.cos(angle)
        y = 256 + r * math.sin(angle)
        points2.append((x, y))
    draw.polygon(points2, fill=(30, 144, 255, 255))  # Dodger Blue
    
    # Merkez
    draw.ellipse((226, 226, 286, 286), fill=(135, 206, 250, 255))
    draw.ellipse((241, 241, 271, 271), fill=(255, 255, 255, 255))
    
    # Hafif blur = anti-aliasing efekti
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save('icon-1-yildiz-p.png', 'PNG', quality=100)

def create_icon2():
    """3D Küp + Gölge"""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Ön yüz
    draw.polygon([(156, 156), (356, 156), (356, 356), (156, 356)], 
                 fill=(30, 60, 114, 255))
    
    # Üst yüz
    draw.polygon([(356, 156), (456, 256), (456, 456), (356, 356)], 
                 fill=(42, 82, 152, 255))
    
    # Yan yüz
    draw.polygon([(156, 356), (356, 356), (456, 456), (256, 456)], 
                 fill=(75, 108, 176, 255))
    
    # Alt gölge
    draw.ellipse((306, 296, 326, 316), fill=(255, 215, 0, 200))
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save('icon-2-kup-p.png', 'PNG', quality=100)

def create_icon3():
    """Gelişmiş Atom"""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Çekirdek katmanları
    draw.ellipse((106, 106, 406, 406), fill=(0, 0, 128, 255))
    draw.ellipse((136, 136, 376, 376), fill=(65, 105, 225, 255))
    draw.ellipse((166, 166, 346, 346), fill=(30, 144, 255, 255))
    draw.ellipse((196, 196, 316, 316), fill=(135, 206, 250, 255))
    draw.ellipse((226, 226, 286, 286), fill=(255, 255, 255, 255))
    draw.ellipse((241, 241, 271, 271), fill=(255, 215, 0, 255))
    
    # Yörüngeler (anti-aliasing için çizgi kalınlığı arttır)
    for i in range(3):
        offset = i * 40
        draw.ellipse((106+offset, 206, 406-offset, 306), 
                     outline=(255, 255, 255, 200), width=3)
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save('icon-3-atom-p.png', 'PNG', quality=100)

def create_icon4():
    """Sonsuzluk - Smooth eğriler"""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Arkaplan
    draw.ellipse((56, 56, 456, 456), fill=(25, 25, 112, 255))
    draw.ellipse((86, 86, 426, 426), fill=(65, 105, 225, 255))
    draw.ellipse((116, 116, 396, 396), fill=(30, 144, 255, 255))
    
    # Sonsuzluk sembolü (elle çizim zor, basit tutalım)
    draw.ellipse((156, 156, 256, 256), outline=(255, 215, 0, 255), width=8)
    draw.ellipse((256, 156, 356, 256), outline=(255, 215, 0, 255), width=8)
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save('icon-4-sonsuz-p.png', 'PNG', quality=100)

def create_icon5():
    """Dişli Çark - Detaylı"""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Merkez
    draw.ellipse((156, 156, 356, 356), fill=(30, 60, 114, 255))
    draw.ellipse((186, 186, 326, 326), fill=(42, 82, 152, 255))
    draw.ellipse((216, 216, 296, 296), fill=(75, 108, 176, 255))
    draw.ellipse((241, 241, 271, 271), fill=(255, 215, 0, 255))
    
    # Dişler
    for i in range(8):
        angle = i * 45 * 3.14159 / 180
        x1 = 256 + 200 * math.cos(angle) - 15
        y1 = 256 + 200 * math.sin(angle) - 15
        x2 = 256 + 200 * math.cos(angle) + 15
        y2 = 256 + 200 * math.sin(angle) + 15
        draw.ellipse((x1, y1, x2, y2), fill=(65, 105, 225, 255))
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save('icon-5-cark-p.png', 'PNG', quality=100)

def create_icon6():
    """Güneş Patlaması"""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Merkez
    draw.ellipse((156, 156, 356, 356), fill=(65, 105, 225, 255))
    draw.ellipse((186, 186, 326, 326), fill=(30, 144, 255, 255))
    draw.ellipse((216, 216, 296, 296), fill=(135, 206, 250, 255))
    draw.ellipse((241, 241, 271, 271), fill=(255, 215, 0, 255))
    
    # Işınlar
    for i in range(12):
        angle = i * 30 * 3.14159 / 180
        x = 256 + 220 * math.cos(angle)
        y = 256 + 220 * math.sin(angle)
        draw.line((256, 256, x, y), fill=(255, 255, 255, 180), width=3)
    
    img = img.filter(ImageFilter.SMOOTH)
    img.save('icon-6-gunes-p.png', 'PNG', quality=100)

print("🎨 Python Pillow ile ikonlar oluşturuluyor...")
create_icon1()
create_icon2()
create_icon3()
create_icon4()
create_icon5()
create_icon6()
print("✅ 6 ikon Pillow ile oluşturuldu!")

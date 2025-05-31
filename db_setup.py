from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Classroom
import os
from dotenv import load_dotenv

# Göreceli yol kullanarak veritabanı dosyasını mevcut dizinde oluştur
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ders_programi.db')

app = Flask(__name__)
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def setup_database():
    with app.app_context():
        # Veritabanı tablolarını sil ve yeniden oluştur
        print("Veritabanı tabloları siliniyor...")
        db.drop_all()
        print("Veritabanı tabloları yeniden oluşturuluyor...")
        db.create_all()
        
        # Sadece derslikleri ekle
        classrooms = [
            {'code': 'M101', 'capacity': 66, 'type': 'NORMAL'},
            {'code': 'M201', 'capacity': 141, 'type': 'NORMAL'},
            {'code': 'M301', 'capacity': 141, 'type': 'NORMAL'},
            {'code': 'S101', 'capacity': 138, 'type': 'NORMAL'},
            {'code': 'S201', 'capacity': 60, 'type': 'NORMAL'},
            {'code': 'S202', 'capacity': 60, 'type': 'NORMAL'},
            {'code': 'D101', 'capacity': 87, 'type': 'NORMAL'},
            {'code': 'D102', 'capacity': 87, 'type': 'NORMAL'},
            {'code': 'D103', 'capacity': 88, 'type': 'NORMAL'},
            {'code': 'D104', 'capacity': 56, 'type': 'NORMAL'},
            {'code': 'D201', 'capacity': 87, 'type': 'NORMAL'},
            {'code': 'D202', 'capacity': 56, 'type': 'NORMAL'},
            {'code': 'D301', 'capacity': 88, 'type': 'NORMAL'},
            {'code': 'D302', 'capacity': 56, 'type': 'NORMAL'},
            {'code': 'D401', 'capacity': 88, 'type': 'NORMAL'},
            {'code': 'D402', 'capacity': 56, 'type': 'NORMAL'},
            {'code': 'D403', 'capacity': 56, 'type': 'NORMAL'},
            {'code': 'AMFİ A', 'capacity': 143, 'type': 'NORMAL'},
            {'code': 'AMFİ B', 'capacity': 143, 'type': 'NORMAL'},
            {'code': 'BİL.LAB 1', 'capacity': 40, 'type': 'LAB'},
            {'code': 'BİL.LAB.2', 'capacity': 30, 'type': 'LAB'},
            {'code': 'KÜÇÜK LAB', 'capacity': 20, 'type': 'LAB'},
            {'code': 'Online', 'capacity': 999, 'type': 'LAB'}
        ]
        
        for classroom_data in classrooms:
            existing_classroom = Classroom.query.filter_by(code=classroom_data['code']).first()
            if not existing_classroom:
                classroom = Classroom(**classroom_data)
                db.session.add(classroom)
        
        db.session.commit()
        print("Derslikler başarıyla oluşturuldu!")

if __name__ == '__main__':
    setup_database() 
# !/usr/bin/python3
import time
import Adafruit_DHT
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = 'mysql+pymysql://root:123456@localhost:3306/iot'

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class Humiture(Base):
    __tablename__ = 'humiture'

    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float)
    humidity = Column(Float)
    create_time = Column(String(20))


Base.metadata.create_all()


# 保存到数据库
def save_humiture(temperature, humidity):
    # 获取当前时间
    create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 创建温湿度对象
    humiture = Humiture(temperature=temperature, humidity=humidity, create_time=create_time)
    # 添加到session
    session.add(humiture)
    # 提交到数据库
    session.commit()
    print(create_time, temperature, humidity)


if __name__ == '__main__':
    while True:
        # 从传感去获取温湿度信息
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        save_humiture(temperature, humidity)
        time.sleep(1)

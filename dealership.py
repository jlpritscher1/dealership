from sqlalchemy import create_engine,Column,String,DATE,NUMERIC,INTEGER, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


db_string = 'postgres://jlpritscher1:Pm77er..@popular-movie.csrmvxoau93j.us-east-2.rds.amazonaws.com:5432/popular_movies'
db = create_engine(db_string) 
Base = declarative_base()


class salesPerson(Base):
    __tablename__ = 'sales_person'
    sales_person_id = Column(INTEGER, primary_key = True)
    sales_person_name = Column(String)
    invoice = relationship('invoice', backref='salesperson')

class mechanic(Base):
    __tablename__ = 'mechanic'
    mechanic_id = Column(INTEGER, primary_key = True)
    mechanic_name = Column(String)
    service_center = relationship('serviceCenter', backref='mechanic')    

class customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(INTEGER, primary_key = True)
    customer_car = relationship('customerCar', backref='customer')
    invoice = relationship('invoice', backref='customer')

class customerCar(Base):
    __tablename__ = 'customer_car'
    customer_car_id = Column(INTEGER, primary_key = True)
    customer_id = Column(INTEGER,ForeignKey('customer.customer_id'))
    service_center = relationship('serviceCenter', backref='customercar')
    service_ticket = relationship('serviceTicket', backref='customercar')
    

class inventory(Base):
    __tablename__ = 'inventory'
    lot_car_id = Column(INTEGER, primary_key = True)
    car_model = Column(String)
    lot_car_price = Column(NUMERIC(19,0))
    invoice = relationship('invoice', backref='inventory')

class parts(Base):
    __tablename__ = 'parts'
    part_id = Column(INTEGER, primary_key = True)
    part_name = Column(String)
    part_price = Column(NUMERIC(19,0))
    service_center = relationship('serviceCenter',backref='parts')

class invoice(Base):
    __tablename__ = 'invoice'
    invoice_id = Column(INTEGER, primary_key = True)
    amount = Column(NUMERIC(19,0))
    lot_car_id = Column(INTEGER,ForeignKey('inventory.lot_car_id'))
    sales_person_id = Column(INTEGER,ForeignKey('sales_person.sales_person_id'))
    customer_id = Column(INTEGER,ForeignKey('customer.customer_id'))
    transaction_history = relationship('transactionHistory', backref='invoice')

class transactionHistory(Base):
    __tablename__ = 'transaction_history'
    transaction_id = Column(INTEGER, primary_key = True)
    invoice_id = Column(INTEGER,ForeignKey('invoice.invoice_id'))

class serviceCenter(Base):
    __tablename__ = 'service_center'
    work_order_id = Column(INTEGER, primary_key = True)
    customer_car_id = Column(INTEGER,ForeignKey('customer_car.customer_car_id'))
    mechanic_id = Column(INTEGER,ForeignKey('mechanic.mechanic_id'))
    part_id = Column(INTEGER,ForeignKey('parts.part_id'))
    service_ticket = relationship('serviceTicket', backref='servicecenter')

class serviceTicket(Base):
    __tablename__ = 'service_ticket'
    service_id = Column(INTEGER, primary_key = True)
    work_order_id = Column(INTEGER,ForeignKey('service_center.work_order_id'))
    customer_car_id = Column(INTEGER,ForeignKey('customer_car.customer_car_id'))


Session = sessionmaker(db)
create_session = Session()

Base.metadata.create_all(db)


jackson = salesPerson(sales_person_name='Jackson Pritscher')
create_session.add(jackson)
create_session.commit() 


sales_person = create_session.query(salesPerson)
for person in sales_person:
    print(person.sales_person_name)



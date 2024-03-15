from database.database import get_db


class PhoneService:

    @staticmethod
    def get_all():
        db = get_db()

        sql = "SELECT * FROM phone WHERE 1=1 "

        return db.execute(sql).fetchall()

    @staticmethod
    def insert_product(name, price, type, img=None):
        db = get_db()
        db.execute(
            'INSERT INTO phone (name, price, type, img) VALUES (?, ?, ?, ?)',
            [name, price, type, img]
        )
        db.commit()

    @staticmethod
    def get_product_price():
        db = get_db()
        
        sql = """SELECT p.name as phone_name, img, id_phone as id, round(sum(price)*1.1) as price, c.name as components FROM phone p
            JOIN phoneComponent pc ON (p.id_phone = pc.PHONECOMPONENT_PHONE_FK)
            JOIN component c ON (pc.PHONECOMPONENT_COMPONENT_FK = c.id_component)
            GROUP BY p.id_phone"""
        
        return db.execute(sql).fetchall()

    @staticmethod
    def add_phone(new_img,new_name, new_type, new_workload):
        db = get_db()
        db.execute('''INSERT INTO phone (img,workload,type,name,company_company_id) 
                      VALUES (?, ?, ?, ?, 1)''',
                   [new_img,new_name, new_type, new_workload]
                   )
        db.commit()
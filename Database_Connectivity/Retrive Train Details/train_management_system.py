import mysql.connector
from train import Train

class TrainManagementSystem:
    def __init__(self, db_config):
        self.conn = mysql.connector.connect(**db_config)

    def retrieve_train_details(self, coach_type, source, destination):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT train_number, train_name, source, destination, ac1, ac2, ac3, sleeper, seater
            FROM train
            WHERE source = %s AND destination = %s
            """, (source, destination)
        )
        
        rows = cursor.fetchall()
        trains = []

        for row in rows:
            train = Train(*row)
            if train.has_coach(coach_type):
                trains.append(train)

        # Sort trains by train number
        trains.sort(key=lambda x: x.get_train_number())
        return trains

    def close(self):
        self.conn.close()

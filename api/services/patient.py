from hl7parser.parser import Parser
from api.db import MysqlDatabase

db = MysqlDatabase('localhost', 'root', '', 'sih')


class PatientService:

    def save(self, hl7_message):
        parser = Parser()
        parser.parse(hl7_message)
        msg_type = parser.getMessageType()

        # traiter le message selon son type
        obx = parser.obx
        pid = parser.pid
        sch = parser.sch

        if msg_type == 'ORU^R01':
            query = "insert into obx (set_id, value, units, references_range, result, pid) values('%s', '%s', '%s', '%s', '%s', '%s')" % (obx.set_id, obx.value, obx.units, obx.references_range, obx.result, pid.ip )
            print(query)
            db.insert(query)

            updateAppointmentQuery = "update rendez_vous set etat = 'finalise' where id = '%s'" % sch.id
            print(updateAppointmentQuery)
            return db.insert(updateAppointmentQuery)

        elif msg_type == 'toto':
            pass
        else:
            print('Désolé ! votre message n\'est pas reconnu par notre API')
import time
class IntraReportPatient():
    def __init__(self, number, date, num_case, room, building, arrivePlace, departPlace, Pre_evaluateNurse,
                 Post_Diagnose, Operation, typeofOperation, department, surgeon, note,
                 Pre_anesthesia_evaluation, service, ASAD, Dormicum, Ephedrine, Ketamine, Anesthesia_technique,Combined_technique, airwayManagement,
                 Anesthesia_start_time, Anesthesia_finish_time, Anesthesia_time, reason, Anesthetistnurse):

        self.number = number ## int
        self.date = date  ## string
        self.num_case = num_case  ## int
        self.room = room  ## Admin access this variable string
        self.building = building  ## string
        self.Pre_evaluateNurse = Pre_evaluateNurse  ## list string 1-2 nurse

        self.arrivePlace = arrivePlace  ## string
        self.departPlace = departPlace  ## string

        self.post_diagnose = Post_Diagnose  ##string
        self.operation = Operation
        self.typeofOperation = typeofOperation  ## string
        self.department = department  ## string
        self.surgeon = surgeon  ## string
        self.note = note  ## string

        self.pre_anesthesia_evaluation = Pre_anesthesia_evaluation  ##string
        self.service = service  ##string
        self.ASAD = ASAD  ## string
        self.agent = ['Dormicum', 'Ephedrine', 'Ketamine']  ## list of agent
        self.agent_dose = [Dormicum, Ephedrine, Ketamine]  ## list dose of each agents
        self.Anesthesia_technique = Anesthesia_technique  ## list
        self.Combined_technique = Combined_technique  ## list
        self.airwayManagement = airwayManagement  ## string
        self.Anesthesia_time = [Anesthesia_start_time, Anesthesia_finish_time, Anesthesia_time]  ## ['Anesthesia start time', 'Anesthesia finish time', 'Anesthesia time']
        self.reason = reason  ## string The reason that the patient cannot suit for operation
        self.Anesthetistnurse = Anesthetistnurse  ## list 1-5 nurse
        print("success created intra")

    def getNum_case(self):
        return self.num_case

    def setDate(self, d):
        self.date = d

    def getDate(self):
        return self.date

    def setRoom(self, r):
        self.room = r

    def getRoom(self):
        return self.room

    def setBuilding(self, b):
        self.building = b

    def getBuillding(self):
        return self.building

    def setPlace(self, new_building, new_evaluation, new_arrivePlace, new_departPlace):
        self.building = new_building
        self.evaluation = new_evaluation  ## string
        self.arrivePlace = new_arrivePlace  ## string
        self.departPlace = new_departPlace  ## string

    def getPlace(self):
        return [self.building, self.evaluation, self.arrivePlace, self.departPlace]

    def setPre_evaluateNurse(self, new_Pre_evaluateNurse):
        self.Pre_evaluateNurse = new_Pre_evaluateNurse

    def getPre_evaluateNurse(self):
        return self.Pre_evaluateNurse

    def setTypeofOperation(self, new_typeofOperation):
        self.typeofOperation = new_typeofOperation  ## string

    def getTypeofOperation(self):
        return self.typeofOperation

    def setDepartment(self, new_department):
        self.department = new_department  ## string

    def getDepartment(self):
        return self.department

    def setService(self, new_service):
        self.service = new_service  ##string

    def getService(self):
        return self.service

    def setASA(self, new_ASA):
        self.ASA = new_ASA  ## string

    def getASA(self):
        return self.ASA

    def setagent_dose(self, new_agent_dose):
        self.agent_dose = new_agent_dose  ## list dose of each agents

    def getagent_dose(self):
        return self.agent_dose

    def setAnesthesia_technique(self, new_Anesthesia_technique):
        self.Anesthesia_technique = new_Anesthesia_technique  ## list

    def getAnesthesia_technique(self):
        return self.Anesthesia_technique

    def setCombined_technique(self, new_Combined_technique):
        self.Combined_technique = new_Combined_technique  ## list

    def getCombined_technique(self):
        return self.Combined_technique

    def setairwayManagement(self, new_airwayManagement):
        self.airwayManagement = new_airwayManagement  ## string

    def getairwayManagement(self):
        return self.airwayManagement

    def setAnesthesia_time(self, new_Anesthesia_time):
        self.Anesthesia_time = new_Anesthesia_time

    def getAnesthesia_time(self):
        return self.Anesthesia_time

    def setAnesthetistnurse(self, new_Anesthetistnurse):
        self.Anesthetistnurse = new_Anesthetistnurse  ## list 1-5 nurse

    def getAnesthetistnurse(self):
        return self.Anesthetistnurse

    def setReason(self, new_reason):
        self.reason = new_reason  ## string The reason that the patient cannot suit for operation

    def getReason(self):
        return self.reason

    def getInfo(self):
        print("in")
        data = []
        data = []
        data.append(self.number)
        data.append(self.date)
        data.append(str(self.num_case))
        data.append(str(self.room))
        data.append(self.building)
        data.append(self.arrivePlace)
        data.append(self.departPlace)
        data.append(self.Pre_evaluateNurse[0])
        data.append(self.Pre_evaluateNurse[1])

        data.append(self.post_diagnose)
        data.append(self.operation)
        data.append(self.typeofOperation)
        data.append(self.department)
        data.append(self.surgeon)
        data.append(self.note)

        data.append(self.pre_anesthesia_evaluation)
        data.append(self.service)
        data.append(self.ASAD)
        for i in self.agent_dose:
            data.append(str(i))
        data.append(self.Anesthesia_technique)
        data.append(self.Combined_technique)
        data.append(self.airwayManagement)
        for i in self.Anesthesia_time:
            data.append(i)
        data.append(self.reason)
        for i in self.Anesthetistnurse:
            data.append(str(i))
        return data, data
    
    def getHistory(self):
        print("in")
        data = []
        data.append(self.number)
        data.append(self.date)
        data.append(str(self.num_case))
        data.append(str(self.room))
        data.append(self.building)
        data.append(self.arrivePlace)
        data.append(self.departPlace)
        data.append(self.Pre_evaluateNurse[0])
        data.append(self.Pre_evaluateNurse[1])

        data.append(self.post_diagnose)
        data.append(self.operation)
        data.append(self.typeofOperation)
        data.append(self.department)
        data.append(self.surgeon)
        data.append(self.note)

        data.append(self.pre_anesthesia_evaluation)
        data.append(self.service)
        data.append(self.ASAD)
        for i in self.agent_dose:
            data.append(str(i))
        data.append(self.Anesthesia_technique)
        data.append(self.Combined_technique)
        data.append(self.airwayManagement)
        for i in self.Anesthesia_time:
            data.append(i)
        data.append(self.reason)
        for i in self.Anesthetistnurse:
            data.append(str(i))
        return data







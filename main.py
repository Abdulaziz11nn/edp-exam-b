class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload
class CompanyAppointmentRequestEvent(Event):
    def __init__(self, student_name, date):
        super().__init__("company_appointment_request", {"student_name": student_name, "date": date})
class AppointmentConfirmationEvent(Event):
    def __init__(self, student_name, is_confirmed):
        super().__init__("appointment_confirmation", {"student_name": student_name, "is_confirmed": is_confirmed})
communication_queue = []
class Student:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
    def ask_for_company_appointment(self, date):
        event = CompanyAppointmentRequestEvent(self.first_name, date)
        communication_queue.append(event)
        print('Event', event.name, 'emitted!')
class Company:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
    def handle_appointment_request(self, event):
        print(f"Received appointment request from {event.payload['student_name']} on {event.payload['date']}")
        confirmation_event = AppointmentConfirmationEvent(event.payload["student_name"], is_confirmed=True)
        communication_queue.append(confirmation_event)
        print('Event', confirmation_event.name, 'emitted!')
# Example Usage
student1 = Student("Dinara", "Brown", '12.05.2007', 'Paris', '334567890')
student2 = Student("Abdu", "kmith", '22.08.1978', 'Kazakistan', '6987654321')
student3 = Student("Dima", "Johnson", '30.11.1990', 'Mongoila', '0578901234')
student1.ask_for_company_appointment('15.01.2025')
student2.ask_for_company_appointment('16.01.2025')
student3.ask_for_company_appointment('17.01.2025')
tech_company = Company('TechCorp', '892 Silicon Valley', '278-TECH', 'info@techcorp.com')
while communication_queue:
    event = communication_queue.pop(0)
    if isinstance(event, CompanyAppointmentRequestEvent):
        tech_company.handle_appointment_request(event)

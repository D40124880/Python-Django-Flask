class Call(object):
    def __init__(self, unique_id, caller_name, caller_number, time_call, reason_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_call = time_call
        self.reason_call = reason_call
    def display(self):
        print "Id: ", unique_id
        print "Caller Name: ", caller_name
        print "Caller Number: ", caller_number
        print "Time of call: ", time_call
        print "Reason for call: ", reason_call
        return self

class CallCenter(Call):
    def __init__(self, calls, queue_size, caller_name):
        self.calls = calls
        self.queue_size = []
    def add(self):
        super
        self.queue_size.append(self.calls)
        return self
    def remove(self):
        self.queue_size.remove(self.queue_size[0])
        return self
    def info(self):
        super
        print "Name: ", self.caller_name
        print "Caller number: ", self.caller_number, "Called about: {} times".format(len(call_list))
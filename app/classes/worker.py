import sys, traceback, logging, os
from classes.logger import Logger
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMessageBox

#This file handle the execute of thread to contact with API SCADA
# wiil call and request executing a thread to avoid program freezing

class WorkerSignals(QObject): # Class to emit signals at execute a thread

    finished = pyqtSignal() # returns no data
    error = pyqtSignal(Exception) # return a tuple with error
    result = pyqtSignal(object) # if success return data, json object
    #progress = pyqtSignal(int) # returns an int with progress, not should be used

class Worker(QRunnable): # Class to execute a function inside a thread

    def __init__(self,fn,*args,**kwargs): # fn:  Function to be executed

        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals() 
        #self.kwargs['progress_callback'] = self.signals.progress 

    @pyqtSlot()
    def run(self):   
        # Retrieve args/kwargs here; and processing using them
        try:
            result = self.fn(*self.args, **self.kwargs) #Execute function, passing args and kwargs, always recibe **kwargs as json object
        except Exception as e:
            Logger.log_error(e)
            traceback.print_exc()
            #print(sys.exc_info)
            #exctype, value = sys.exc_info()[:2]
            self.signals.error.emit(e)
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

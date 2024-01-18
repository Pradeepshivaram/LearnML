import sys

def error_message_detail(error, error_details:sys):
    _,_,tb_info = error_details.exc_info()
    file_name = tb_info.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,tb_info.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details)
    
    def __str__(self) -> str:
        return self.error_message 
        
    
## Excutes this as script
# if __name__ == '__main__':  
#     try:
#         a=1/0
#     except Exception as e:
#         raise CustomException(error_message=e, error_details=sys)
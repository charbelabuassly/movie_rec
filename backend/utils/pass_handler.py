import bcrypt
import re

def verify_password(request_pass: str, real_pass: str) -> bool:
    if isinstance(real_pass, str):
        real_pass = real_pass.strip().encode('utf-8')
    
    return bcrypt.checkpw(request_pass[:72].encode('utf-8'), real_pass)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password[:72].encode('utf-8'), bcrypt.gensalt(rounds=4)).decode('utf-8')

def validate_pass(request_pass : str) -> bool:
    if ( len(request_pass) >=8 
        and re.search("[a-z]",request_pass) #Atleast one small letter
        and re.search("[A-Z]",request_pass) #Atleast one capital letter
        and re.search("[0-9]",request_pass) #Atleast one number
        and re.search(r"[!@#$%^&*()_+=\-]", request_pass)  # at least one special char
        and not re.search("\s",request_pass)): #No white spaces
        return True;
    else:
        return False;
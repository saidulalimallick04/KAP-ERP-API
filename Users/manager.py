from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    '''
    create any user or superuser using this UserManager
    '''
    
    def create_user(self,phone_number,password = None, **extra_fields):
        
        user = self.model(phone_number = phone_number, **extra_fields)
        
        user.set_password(password)
        user.save(using = self._db)
        
        return user


    def create_superuser(self,phone_number,password = None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(phone_number = phone_number,password=password,**extra_fields)
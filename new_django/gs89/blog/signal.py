from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.backends.signals import connection_created
from django.db.models.signals import post_migrate,pre_migrate
from django.core.signals import request_started,request_finished,got_request_exception
@receiver(pre_migrate)
def conn_db(sender,connection,**kwargs):
        print(".................")
        print("pre delete signal")
        print("sender ",sender)
        print('connection :'  ,connection)      
        print(f"Kwargs  ,{kwargs}")     
@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
        print(".................")
        print("pre delete signal")
        print("sender ",sender)
        print("app_config ",app_config)
        print('verbosity :'  ,verbosity)     
        print('interactive :'  ,interactive)     
        print('using :'  ,using)     
        print('plan :'  ,plan)     
        print('apps :'  ,apps) 
        print(f"Kwargs  ,{kwargs}")  
@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("....... .......")
    print("sender ",sender)
    print(f"Kwargs  ,{kwargs}")
@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print("....... .......")
    print("sender ",sender)
    print("request ",request)
    print(f"Kwargs  ,{kwargs}")
    # else:
    #     print(".................")
    #     print("pre save signal")
    #     print("sender ",sender)
    #     print("Instance ",instance)
    #     print("created ",created)
    #     print(f"Kwargs  ,{kwargs}")
   
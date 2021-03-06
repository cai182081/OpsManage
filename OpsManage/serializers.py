#!/usr/bin/env python  
# _#_ coding:utf-8 _*_  
from rest_framework import serializers
from OpsManage.models import *
from django.contrib.auth.models import Group,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','username',
                  'first_name','last_name','email','is_staff',
                  'is_active','date_joined')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Assets
        fields = ('id','service_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')
          
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone_Assets
        fields = ('id','zone_name','zone_contact','zone_number')         

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_Assets
        fields = ('id','line_name')          

class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid_Assets
        fields = ('id','raid_name')         
        
# class AssetStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assets_Satus
#         fields = ('id','status_name') 
        
class CronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cron_Config
        fields = ('id','cron_minute','cron_hour','cron_day',
                  'cron_week','cron_month','cron_user',
                  'cron_name','cron_desc','cron_server',
                  'cron_command','cron_script','cron_status') 
        

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('id','assets_type','name','sn','buy_time','expire_date',
                  'buy_user','management_ip','manufacturer','provider',
                  'model','status','put_zone','group','business')  
        
# class VmServerAssetsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assets
#         fields = ('id','assets_type','name','status','put_zone','group','business')         

class AssetsLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Assets
        fields = ('id','assets_id','assets_user','assets_content','assets_type','create_time') 
        

class ProjectConfigSerializer(serializers.ModelSerializer): 
    project_number = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project_Config
        fields = ('id','project_env','project_name','project_local_command',
                  'project_repo_dir','project_dir','project_exclude',
                  'project_address','project_repertory','project_status',
                  'project_remote_command','project_number')   

class DeployLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Project_Config
        fields = ('id','project_id','project_user','project_name',
                  'project_content','project_branch','create_time') 

class AnbiblePlaybookSerializer(serializers.ModelSerializer): 
    server_number = serializers.StringRelatedField(many=True)
    class Meta:
        model =  Ansible_Playbook
        fields = ('id','playbook_name','playbook_desc','playbook_vars',
                  'playbook_uuid','playbook_file','playbook_auth_group',
                  'playbook_auth_user','server_number')   
        
class AnsibleModelLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Ansible_Model
        fields = ('id','ans_user','ans_model','ans_args',
                  'ans_server','create_time') 
        
class AnsiblePlaybookLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Ansible_Playbook
        fields = ('id','ans_user','ans_name','ans_content','ans_id',
                  'ans_server','ans_content','create_time') 

class CronLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_Cron_Config
        fields = ('id','cron_id','cron_user','cron_name','cron_content',
                  'cron_server','create_time') 

class ServerSerializer(serializers.ModelSerializer): 
    assets = AssetsSerializer(required=False)
#     keyfile = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Server_Assets
        fields = ('id','ip','hostname','username','port','passwd',
                  'line','cpu','cpu_number','vcpu_number','keyfile',
                  'cpu_core','disk_total','ram_total','kernel',
                  'selinux','swap','raid','system','assets') 

    def create(self, data):
        if(data.get('assets')):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets;
        server = Server_Assets.objects.create(**data)  
        return server 
           
         
class NetworkSerializer(serializers.ModelSerializer): 
    assets = AssetsSerializer(required=False)
    class Meta:
        model = Network_Assets
        fields = ('id','ip','bandwidth','port_number','firmware',
                  'cpu','stone','configure_detail','assets')    
    def create(self, data):
        if(data.get('assets')):
            assets_data = data.pop('assets')
            assets = Assets.objects.create(**assets_data)
        else:
            assets = Assets()
        data['assets'] = assets;
        server = Network_Assets.objects.create(**data)  
        return server   
    
class DeployOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Order
        fields = ('id','order_project','order_subject','order_content',
                  'order_branch','order_comid','order_tag','order_audit',
                  'order_status','order_level','order_cancel','create_time',
                  'order_user')   
        
class InceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inception_Server_Config
        fields = ('id','db_name','db_host','db_user','db_passwd','db_port',
                  'db_backup_host','db_backup_user','db_backup_port',
                  'db_backup_passwd')   

class AuditSqlOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SQL_Audit_Order
        fields = ('id','order_desc','order_status','order_cancel')         
        
class DataBaseServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataBase_Server_Config
        fields = ('id','db_env','db_name','db_host','db_user',
                  'db_passwd','db_port','db_mark','db_service',
                  'db_group')  
        
        
class CustomSQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_High_Risk_SQL
        fields = ('id','sql')
        
class HistroySQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = SQL_Execute_Histroy
        fields = ('id','exe_sql','exe_user','exec_status','exe_result')
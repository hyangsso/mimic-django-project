from django.db import models

# Create your models here.
class PatientInformation(models.Model):
    subjectid = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    height = models.FloatField(max_length=3)
    weight = models.FloatField(max_length=3)
    bmi = models.FloatField(max_length=2)
    
    def __str__(self):
        return self.sex
    
class OperationInformation(models.Model):
    id = models.ForeignKey(PatientInformation, primary_key=True, on_delete=models.CASCADE, unique=True)
    casestart = models.IntegerField(default=0)
    caseend = models.IntegerField()
    anestart = models.IntegerField()
    aneend = models.IntegerField()
    opstart = models.IntegerField()
    opend = models.IntegerField()
    emop = models.CharField(max_length=1)
    department = models.CharField(max_length=20)
    optype = models.CharField(max_length=15)
    dx = models.CharField(max_length=50)
    opname = models.CharField(max_length=20)
    approach = models.CharField(max_length=12)
    position = models.CharField(max_length=25)
    ane_type = models.CharField(max_length=10)
    
    
class PreopInformation(models.Model):
    id = models.ForeignKey(PatientInformation, primary_key=True, on_delete=models.CASCADE, unique=True)
    preop_htn = models.CharField(max_length=1)
    preop_dm = models.CharField(max_length=1)
    preop_ecg = models.CharField(max_length=100)
    preop_pft = models.CharField(max_length=30)
    preop_hb = models.FloatField(max_length=4)
    preop_plt = models.FloatField(max_length=6)
    preop_pt = models.FloatField(max_length=5)
    preop_aptt = models.FloatField(max_length=5)
    preop_na = models.FloatField(max_length=5)
    preop_k = models.FloatField(max_length=4)
    preop_gluc = models.FloatField(max_length=5)
    preop_alb = models.FloatField(max_length=4)
    preop_ast = models.FloatField(max_length=6)
    preop_alt = models.FloatField(max_length=6)
    preop_bun = models.FloatField(max_length=5)
    preop_cr = models.FloatField(max_length=5)
    preop_ph = models.FloatField(max_length=6)
    preop_hco3 = models.FloatField(max_length=4)
    preop_be = models.FloatField(max_length=4)
    preop_pao2 = models.FloatField(max_length=5)
    preop_paco2 = models.FloatField(max_length=4)
    preop_sao2 = models.FloatField(max_length=5)
    
    
class IntraopInformation(models.Model):
    id = models.ForeignKey(PatientInformation, primary_key=True, on_delete=models.CASCADE, unique=True)
    intraop_ebl = models.FloatField(max_length=7)
    intraop_uo = models.FloatField(max_length=6)
    intraop_rbc = models.FloatField(max_length=3)
    intraop_ffp = models.FloatField(max_length=2)
    intraop_crystalloid = models.FloatField(max_length=7)
    intraop_colloid = models.FloatField(max_length=4)
    intraop_ppf = models.FloatField(max_length=3)
    intraop_mdz = models.FloatField(max_length=3)
    intraop_ftn = models.FloatField(max_length=3)
    intraop_rocu = models.FloatField(max_length=3)
    intraop_vecu = models.FloatField(max_length=2)
    intraop_eph = models.FloatField(max_length=3)
    intraop_phe = models.FloatField(max_length=4)
    intraop_epi = models.FloatField(max_length=5)
    intraop_ca = models.FloatField(max_length=5)
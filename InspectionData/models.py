from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


# Common Abstract Base Form
class BaseForm(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    class Meta:
        abstract = True


#----------------------------------------- For Wheel Specifications Data --------------------------------------
# Wheel Specification Form
class Wheel_Specification_Data(models.Model):
    treadDiameterNew = models.CharField(max_length=100)
    lastShopIssueSize = models.CharField(max_length=100)
    condemningDia = models.CharField(max_length=100)
    wheelGauge = models.CharField(max_length=100)
    variationSameAxle = models.CharField(max_length=50)
    variationSameBogie = models.CharField(max_length=50)
    variationSameCoach = models.CharField(max_length=50)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=100)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)


class Wheel_Specification_Form(BaseForm):
    
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    
    fields = models.ForeignKey(Wheel_Specification_Data, verbose_name=_("Fields"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.formNumber} submitted by {self.submittedBy} on {self.submittedDate}"


#---------------------------- For Bogie Data ---------------------------------------------------------

# Bogie Details
class Bogie_Details_Data(models.Model):
    bogieNo = models.CharField(max_length=50)
    makerYearBuilt = models.CharField(max_length=100)
    incomingDivAndDate = models.CharField(max_length=100)
    deficitComponents = models.TextField()
    dateOfIOH = models.DateField()


# Bogie Checksheet Items
class Bogie_Check_Sheet_Data(models.Model):
    bogieFrameCondition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolsterSuspensionBracket = models.CharField(max_length=100)
    lowerSpringSeat = models.CharField(max_length=100)
    axleGuide = models.CharField(max_length=100)
    
    
# BMBC Checksheet Items
class BMBC_Check_Sheet_Data(models.Model):
    cylinderBody = models.CharField(max_length=100)
    pistonTrunnion = models.CharField(max_length=100)
    adjustingTube = models.CharField(max_length=100)
    plungerSpring = models.CharField(max_length=100)


# 🚃 Bogie Checksheet Form
class Bogie_Check_Sheet_Form(BaseForm):
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    
    bogieDetails = models.ForeignKey(Bogie_Details_Data, verbose_name=_("Bogie Details"), on_delete=models.CASCADE)
    bogieChecksheet = models.ForeignKey(Bogie_Check_Sheet_Data, verbose_name=_("Bogie Check Sheet"), on_delete=models.CASCADE)
    bmbcChecksheet = models.ForeignKey(BMBC_Check_Sheet_Data, verbose_name=_("BMBC Check Sheet"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.formNumber} inspection by {self.inspectionBy} on {self.inspectionDate}'

from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=250)
    phone = models.BigIntegerField()

#  To save the user information in the database

    def register(self):
        self.save()

# Custom validation to check if the mobile number is already exists or not per user

    def PhoneIsExists(self):
        if Information.objects.filter(phone=self.phone):
            return True
        else:
            return False

# Custom validation to check the mobile number is 10 digit or not

    def ValiadteUser(self):

        error_message = None

        if self.PhoneIsExists():
            error_message = 'Phone number is already exists'

        elif not len(self.phone) == 10:
            error_message = 'Mobile number should be always a 10 digit number'

        return error_message

    @staticmethod
    def get_user_by_name(name):
        try:
            return Information.objects.get(name=name)
        except:
            return False






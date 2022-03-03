from rest_framework import serializers
from accounts.models import Account

class RegisterSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    def save(self):
        account = Account(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


# class VerificationSerializer(serializers.ModelSerializer):
#     verification_code = serializers.IntegerField()

#     class Meta:
#         model = Account
#         fields = ['id_ref', 'verifiaction_code']
        
#         def verifyAccount(self):
#             verification_code = self.validated_data['verification_code']
#             account = Account.objects.get(id_ref=self.validated_data['id_ref'])
#             if verification_code != 1234:
#                 raise serializers.ValidationError({'verification_code':'verification code is incorrect'})
#             account.verifyAccount()

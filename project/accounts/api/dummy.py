# import phonenumbers
# def validate_phone_number(value, field_name):
#     if not value:
#         return value

#     parsed = phonenumbers.parse(value, 'IN')
#     if not phonenumbers.is_possible_number(parsed):
#         raise serializers.ValidationError("{} is not a valid US phone number.".format(field_name))
#     return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)


# address = serializers.CharField(max_length=255)
# phone_number = serializers.CharField(required=True,label="Phone Number")
# def save(self):
    #     account = Account(
    #         email = self.validated_data['email'],
    #         username = self.validated_data['username'],
    #     )
    #     account.address = self.validated_data['address']
    #     password = self.validated_data['password']
    #     val = self.validated_data['phone_number']
    #     var = validate_phone_number(val,'Phone Number')
    #     account.phone_number = var
    #     account.set_password(password)
    #     account.save()
    #     return account


# def create(self,validated_data):
#         username = self.validated_data['username']
#         email = self.validated_data['email']
#         address = self.validated_data['address']
#         password = self.validated_data['password']
#         phone_number = self.validated_data['phone_number']  
#         user_obj = User(
#             email = email,
#             username = username,
#             address = address,
#             phone_number = phone_number
#         )
         
#         user_obj.set_password(password)
#         usr_obj.save()
#         return validated_data
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        Token.objects.filter(user=user).delete()
        # print(resltdata)
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        print(created)
        try:
            return Response({
               'status': status.HTTP_200_OK,
                'token': token.key,
                'email': user.email,
                "message": "LoggedIn successfully"
            })
        except Exception as err:
         return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error': str((err)),
                     'success': ''}
                    )

   #     {
#     "username":"sunil",
#     "password":"135"
# } 
# {"username": "amit",
#  "password": "abcd",
#  "email": "amit@gmail.com"
#  }


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import connection
from .custom_serialize_value import serialize_value

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_CategoryList(request):
    try:
        cursor = connection.cursor()
        cursor.execute('CALL usp_Get_category (%s,%s);', (request.data['userName'], request.data['passWord']))
        reslt = []
        columns = [col[0] for col in cursor.description]
        for row in cursor.fetchall():
            row_dict = {col: serialize_value(val) for col, val in zip(columns, row)}
            reslt.append(row_dict)
        content =  {'Category_List': reslt}
        rsltmessage = reslt[0].get('Message', '')
        if 'error' in rsltmessage.lower() or 'invalid' in rsltmessage.lower():
          return Response({ 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,'Error': (reslt[0]['Message']),
                     'success': ''})
        else:
         return Response({'status': status.HTTP_200_OK,
                            'success':(content),'Error':""})

    except Exception as err:
     return Response({'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'Error': str((err)),
                     'success': ''}
                    )
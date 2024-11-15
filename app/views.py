from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from .tasks import ingest_data

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        approved_limit = round(36 * data['monthly_income'] / 1e5) * 1e5
        customer = Customer.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            monthly_salary=data['monthly_income'],
            approved_limit=approved_limit,
        )
        return Response(CustomerSerializer(customer).data)

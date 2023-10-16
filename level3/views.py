from django.shortcuts import render, get_object_or_404
from level1.models import Certificate
from level3.utils import decode_jwt_token

def verify_certificate(request, token):
    data = decode_jwt_token(token)
    if data:
        certificate_id = data.get('certificate_id')
        certificate = get_object_or_404(Certificate, pk=certificate_id)
        return render(request, 'verify_certificate.html', {'certificate': certificate, 'token_valid': True})
    else:
        return render(request, 'verify_certificate.html', {'token_valid': False})

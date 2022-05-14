import ssl
from cryptography import x509

with open('ip_list.txt') as file:
    for ip in map(lambda line: line.rstrip('\n'), file):
        try:
            cert = ssl.get_server_certificate((ip, 443))
        except:
            print(ip + " - ERROR")
            continue
        cert_decoded = x509.load_pem_x509_certificate(str.encode(cert))
        common_name = cert_decoded.subject.get_attributes_for_oid(x509.OID_COMMON_NAME)[0].value.strip()
        print(ip + " - " + common_name)

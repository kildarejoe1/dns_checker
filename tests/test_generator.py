import unittest

from app import app

def test_dns_check_button():
    fqdn="csc.iii.com"
    result=app.externaldns(fqdn)
    result_should_be="100.27.9.100"
    assert result_should_be == result

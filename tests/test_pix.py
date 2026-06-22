import sys
sys.path.append("../")

import pytest
import os
from db_models import payment
from payments.pix import Pix

def test_pix_ceate_payment():
    pix_instance = Pix()

    #create a payment
    payment_info = pix_instance.create_payment()

    print(payment_info)

    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info

    qr_code_path = payment_info["qr_code_path"]

    assert os.path.isfile(f"../static/img/{qr_code_path}.png")
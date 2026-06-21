import uuid
import qrcode
import os
from pathlib import Path

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        bank_payment_id = str(uuid.uuid4())
        hash_payment = f'hash_payment_{bank_payment_id}'

        base_dir = Path(__file__).resolve().parent.parent
        img_dir = base_dir / "static" / "img"
        img_dir.mkdir(parents=True, exist_ok=True)

        file_name = f"qr_code_payment_{bank_payment_id}"
        file_path = img_dir / f"{file_name}.png"

        img = qrcode.make(hash_payment)
        img.save(file_path)

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": file_name
}